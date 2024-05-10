#! C:\Users\divya\AppData\Local\Programs\Python\Python312\python.exe
print ("Content-Type: text/html\r\n\r\n")
print()
import cgi
import cgitb
import mysql.connector as connector
from DBHelper import *
from datetime import datetime
import json
import os
from io import BytesIO
from PIL import Image
import base64


cgitb.enable()  #activates a special exception handler that tell to browser
# cgitb.enable(display=0, logdir="/path/to/logdir")


 

# con = connector.connect(host="localhost",user="introdec",passwd="data73063", database="infotech")
# creating object of DBHelper which contain connection data
x = DBHelper()
# print(x)

f = cgi.FieldStorage()

# getting the value from signup.js to what to do
d = f.getvalue("what")

items=[]


# inserting product details into database

try:
    prod_id = f.getvalue("prod_id")
    prod_name = f.getvalue("prod_name")
    prod_cat_id = f.getvalue("prod_cat_id")
    prod_stock =f.getvalue("prod_stock")
    prod_ori_price = f.getvalue("prod_ori_price")
    prod_dis_price = f.getvalue("prod_dis_price")
    prod_width = f.getvalue("prod_width")
    prod_height = f.getvalue("prod_height")
    prod_size = f.getvalue("prod_size")
    prod_image1 = f.getvalue("prod_file1")
    prod_image2 = f.getvalue("prod_file2")
    prod_image3 = f.getvalue("prod_file3")
    prod_desc = f.getvalue("prod_desc")
        
    
    prod_dimension = f"{prod_width} x {prod_height}"

    


    print(prod_dimension)
    # # if(prod_id != None and prod_name !=None and prod_cat_id != None and prod_stock !=None and prod_ori_price != None and prod_image1 !=None and prod_image2 != None and prod_image3 !=None and prod_desc != None):
    insert_prod_query = f"insert into product(product_id, product_name, category_id, stock_quant, original_price, discount_price, dimension, size, image_url1) values('{prod_id}','{prod_name}','{prod_cat_id}','{prod_stock}','{prod_ori_price}','{prod_dis_price}','{prod_dimension}','{prod_size}','{prod_image1}')"
    print(insert_prod_query)
    cur = x.conn.cursor()
    cur.execute(insert_prod_query)
    x.conn.commit()
    print("product inserted")
    # else:
        # raise Exception("Error !!! One of the field is empty")
except Exception as e:
    print(e)



