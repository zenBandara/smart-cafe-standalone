import db
import update


def delete(user):
    sql_del = "DELETE FROM realtime_dash_user"
    con1 = db.get_db_connection(user)
    if con1:
        try:
            cursor1 = con1.cursor()  # Create a cursor from the connection
            cursor1.execute(sql_del)
            con1.commit()
            return True
        except Exception as e:
            return False


def update_dashboard(order_id, food_count, user):
    sql = "select * from realtime_dash_user"

    con = db.get_db_connection(user)

    if con:
        try:
            cursor = con.cursor()  # Create a cursor from the connection
            cursor.execute(sql)  # Pass API and user as parameters
            data = cursor.fetchone()
            if data:
                if len(data) > 0:
                    # Delete all rows in realtime DB
                    delete_fun = delete(user)

                    # get foods variants count
                    for key, value in food_count.items():
                        update_process = update.update(order_id, str(key), int(value), user)
                    if update_process[0]:
                        return True
                    else:
                        return False

                else:
                    # add data to the database
                    for key, value in food_count.items():
                        update_process = update.update(order_id, str(key), int(value), user)
                    if update_process[0]:
                        return True
                    else:
                        return False
            else:
                for key, value in food_count.items():
                    update_process = update.update(order_id, str(key), int(value), user)
                if update_process[0]:
                    return True
                else:
                    return False
        except Exception as e:
            return False
        finally:
            con.close()  # Close the connection
    else:
        return False

