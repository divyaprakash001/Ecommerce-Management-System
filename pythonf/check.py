#! C:\Users\divya\AppData\Local\Programs\Python\Python312\python.exe
print ("Content-Type: text/html\r\n\r\n")
# print("Content-Type: application/json")
# print()
import cgi
# import cgitb
# import mysql.connector as connector
# from DBHelper import *
# from datetime import datetime
import json
# import random
# import string
# import sys
# import os 
# import os
# from io import BytesIO
#!/usr/bin/env python3

# import cgi
# import json


# print("Content-Type: application/json")  # JSON response
# print()  # Blank line required after Content-Type header
# Parse the incoming form data
form = cgi.FieldStorage()
# Extract fields
# order_data = {
#     "what": form.getvalue("what"),
#     "user_id": form.getvalue("user_id"),
#     "order_id": form.getvalue("order_id"),
#     "order_date": form.getvalue("order_date"),
#     "country": form.getvalue("country"),
#     "state": form.getvalue("state"),
#     "district": form.getvalue("district"),
#     "city": form.getvalue("city"),
#     "pincode": form.getvalue("pincode"),
#     "landmark": form.getvalue("landmark"),
#     "products": json.loads(form.getvalue("products"))
# }
# # Print all data (for debugging purposes)
# print(json.dumps({"status": "success", "data": order_data}, indent=4))





# cgitb.enable(display=0, logdir="/path/to/logdir")


 


# Get the JSON data from the request
# form = cgi.FieldStorage()
# userid = form.getvalue('user_id')
# order_id = form.getvalue('order_id')
# order_date = form.getvalue('order_date')
# country = form.getvalue('country')
# state = form.getvalue('state')
# district = form.getvalue('district')
# city = form.getvalue('city')
# pincode = form.getvalue('pincode')
# landmark = form.getvalue('landmark')
print("------------------------")
data = form.getvalue('formData')
print(data)
print(type(data))

jsdta = json.loads(data)
print(type(jsdta))
print(jsdta.get("what"))
print(jsdta.get("user_id"))
print(jsdta.get("order_id"))
print(jsdta.get("order_date"))
print(jsdta.get("country"))
print(jsdta.get("state"))
print(jsdta.get("district"))
print(jsdta.get("city"))
print(jsdta.get("pincode"))
print(jsdta.get("landmark"))
print(jsdta.get("products"))
print(jsdta.get("products")[0].get("prod_cat"))

# Print the dictionary
# print(jsdta)
# print(type(jsdta))
# prod = jsdta.get('products')
# product = json.loads(prod)
# print(type(product))
# prod_data = json.loads(products)

# print(products.order_id)
# # print(order_date,order_id,country)

# print(prod_data)
# print(type(products))

# print(json_data)
# Parse JSON data
# data = json.loads(json_data)

# Now you can use the data dictionary in your Python script
# print("Content-Type: application/json") # Set the content type of the response
# print()  # Blank line, end of headers
# print(json.dumps({"success": True, "text": json_data}))  # Send back some data (echo)