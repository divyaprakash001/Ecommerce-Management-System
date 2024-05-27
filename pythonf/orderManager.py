#! C:\Users\divya\AppData\Local\Programs\Python\Python312\python.exe
print ("Content-Type: text/html\r\n\r\n")

import cgi
import cgitb
import mysql.connector as connector
from DBHelper import *
from datetime import datetime
import json
import random
import string
import sys
# import os
# from io import BytesIO



cgitb.enable()  #activates a special exception handler that tell to browser
# cgitb.enable(display=0, logdir="/path/to/logdir")


 

conn = connector.connect(host='localhost',user='introdec',password='data73063',database='infotech')
cur = conn.cursor()

f = cgi.FieldStorage()

def generate_order_id():
        length = 8
        chars = string.ascii_uppercase + string.digits
        return ''.join(random.choice(chars) for _ in range(length))


# getting the value from signup.js to what to do
d = f.getvalue("what")
if(d == "insert_order"):

    def generate_order_id():
        length = 8
        chars = string.ascii_uppercase + string.digits
        return ''.join(random.choice(chars) for _ in range(length))

    try:
        # Function to generate a random order ID
 

        # Get form data
        # form = cgi.FieldStorage()
        user_id = f.getvalue('user_id')
        order_id = generate_order_id()
        order_date = f.getvalue('order_date')
        country = f.getvalue('country')
        state = f.getvalue('state')
        district = f.getvalue('district')
        city = f.getvalue('city')
        pincode = f.getvalue('pincode')
        landmark = f.getvalue('landmark')

        # Parse product data
        products_json = f.getvalue('products')
        products = json.loads(products_json)

        total_amount = 0
        product_details = []
        for product in products:
            prod_id = product['prod_id']
            quantity = product['quantity']

        # Fetch product details from database
            cur.execute("SELECT category_id, discount_price FROM product WHERE product_id = %s", (prod_id,))
            product_data = cur.fetchone()

            # Calculate amount for current product
            if product_data is not None:
            # Calculate amount for current product
                price = product_data[1]
                product_amount = price * quantity
                total_amount += product_amount

                # Construct product details including amount
                product_detail = {
                    "prod_cat": product_data[0],
                    "prod_id": prod_id,
                    "quantity": quantity,
                    "amount": product_amount
                }
                product_details.append(product_detail)

        if(user_id != None and order_id != None and order_date != None and country != None
        and state != None  and district != None  and city != None and pincode != None and landmark != None):
            cur.execute(f'select * from order_info where order_id="{order_id}"')
            if cur.fetchall()==[]:
                insert_order_query = "INSERT INTO order_info (order_id, user_id, order_date, country, state, district, city, pincode, landmark, total_amount, product_details) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                order_data = (order_id, user_id, order_date, country, state, district, city, pincode, landmark, total_amount, json.dumps(product_details))
                cur.execute(insert_order_query, order_data)
                conn.commit()
                print("Content-Type: application/json")
                print()
                print(json.dumps({"success": True, "order_id": order_id, "message":"ho rha hai"}))
            else:
                print("Content-Type: application/json")
                print()
                print(json.dumps({"success": False, "error": "hshsh"}))
                # print("order already exists")
                # print()
        else:
            print("Content-Type: application/json")
            print()
            print(json.dumps({"success": False, "error": "nhi hua"}))
            # print("one of the field is empty")
    except Exception as e:
        conn.rollback()
        print("Content-Type: application/json")
        print()
        print(json.dumps({"success": False, "error": str(e)}))
        # Rollback changes if an error occurs
        # print(e)


elif(d=="generateOrderId"):
    print(generate_order_id())
    # print("Content-Type: application/json")
    # print()
    # print(json.dumps({"success": True, "order_id": generate_order_id()}))
                
