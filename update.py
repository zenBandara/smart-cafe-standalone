import db


def get_price(food_id,user):
    sql_get_price = "select price from product where description = %s"
    con_get_price = db.get_db_connection(user)
    if con_get_price:
        try:
            get_price_cursor = con_get_price.cursor()
            get_price_cursor.execute(sql_get_price, (food_id,))
            price_data = get_price_cursor.fetchone()
            if price_data:
                return True, price_data[0]
            else:
                return False, ""

        except Exception as e:
            return False, e


def update(order_id, food, qnt, user):
    con_update = db.get_db_connection(user)

    if con_update:
        try:
            cursor_update = con_update.cursor()
            got_price, price = get_price(food,user)
            if got_price:
                sql_update = "insert into realtime_dash_user (order_id, Item_ID, Item_qty, price) values ('" + str(order_id) + "','" + str(food) + "'," + str(qnt) + "," + str(price) + ")"

                cursor_update.execute(sql_update)
                row_count = cursor_update.rowcount
                if row_count > 0:
                    con_update.commit()
                    return True, "Success.."
                else:
                    return False, "Data Add Error.."
            else:
                return False, "Price Not Available for this food."
        except Exception as e:
            return False, e
