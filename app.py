from flask import Flask, jsonify, request
from uuid import uuid4
import os

import clear
import food_detector
import update_dashboard

app = Flask(__name__)


def generate_unique_id():
    return uuid4().hex


def api_validator(api_key, user):
    import db
    # Validate API key and user
    sql = "SELECT `info` FROM `users` WHERE `api`=%s and `user`=%s"
    

    con = db.get_init_db_connection()

    if con:
        try:
            cursor = con.cursor()  # Create a cursor from the connection
            cursor.execute(sql, (api_key, user))  # Pass API and user as parameters
            info_tuple = cursor.fetchone()
            if info_tuple and info_tuple[0] == 'v':
                return True

            else:
                return False

        except Exception as e:
            return False

        finally:
            cursor.close()  # Close the cursor
            con.close()  # Close the connection
    else:
        return False


@app.route('/sc', methods=['POST'])
def smart_cafe():  # put application's code here
    # Authenticate user using API key
    api_key = request.headers.get('API')
    user = request.headers.get('User')

    if api_validator(api_key, user):

        # Save passed image
        image_id = generate_unique_id()
        image = request.files.get("image")
        if image:
            image.save(os.path.join("image", image_id + ".jpg"))
            if os.path.exists("image/" + image_id + ".jpg"):
                food_count = food_detector.process(image_id)
                clear.clear(image_id)
                # Update dashboard
                update = update_dashboard.update_dashboard(image_id, food_count, user)
                if update:
                    return jsonify(food_count), 201
                else:
                    return jsonify({"msg": "Data save error."}), 500
            else:
                clear.clear(image_id)
                return jsonify({"msg": "Image save error."}), 500

        else:
            clear.clear(image_id)
            return jsonify({"error": "No image provided."}), 400  # 400 Bad Request

    else:
        return jsonify({"error": "Invalid API key or user."}), 401  # 401 Unauthorized


if __name__ == '__main__':
    app.run(port=8080)
