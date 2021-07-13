# all the imports
import sqlite3
from model.Order import Order
from sqlite3 import Error
from flask import Flask, render_template

# configuration
DATABASE = './data.db'
DEBUG = True


# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

def fetch_restaurants():
  conn = None
  try:
    conn = sqlite3.connect(DATABASE)
    curs = conn.cursor()
    curs.execute("SELECT rest_id, rest_name from tb_restaurant")
    rows = curs.fetchall()
    #print(rows)
    return rows
  except Error as e:
    print(e)
  finally:
    if conn:
      conn.close()

def fetch_menu_by_restaurantid(rest_id):
    conn = None
    try:
        conn = sqlite3.connect(DATABASE)
        curs = conn.cursor()
        curs.execute("""SELECT menu_id, item_name from tb_menu where rest_id=? """,(rest_id))
        rows = curs.fetchall()
        print(rows)
        return rows
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def insert_order(order):
    conn = None
    try:
        conn = sqlite3.connect(DATABASE)
        curs = conn.cursor()
        curs.execute("""INSERT INTO TB_ORDER(cust_id, items, quantity, price) values (?, ?, ?, ?)""",
                     (order.cust_id, order.items, order.quantity, order.price))
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()



### Flask Code ###

@app.route("/restaurants", methods=['GET'])
def get_restaurants():
    # Get items from the helper
    restaurant_list = fetch_restaurants()
    print('list:')
    print(restaurant_list)
    #todo: need to convert rows into list or dict

    # Return response for JSON
    #response = Response(json.dumps({'tasks': restaurant_list}), mimetype='application/json')
    #return response

    # Return as html template
    return render_template("main.html")


@app.route("/menu/{{restid}}", methods=['GET'])
def get_menu_by_rest():
    #todo: fetch logic
    # menu_list = fetch_menu_by_restaurantid()
    return


@app.route("/order", methods=['POST'])
def create_order():
  #todo: full
  return



## MAIN ##

if __name__ == '__main__':
  ##tests
  #fetch_restaurants()
  #fetch_menu_by_restaurantid("2")
  order = Order("1", "1", 1, 1)
  insert_order(order)

  #web-application
  #app.run()
