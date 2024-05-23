#! C:\Users\divya\AppData\Local\Programs\Python\Python312\python.exe
print ("Content-Type: text/html\r\n\r\n")
# print()
import cgi
import cgitb
import mysql.connector as connector
from DBHelper import *
from datetime import datetime
# import json
# import os
# from io import BytesIO



cgitb.enable()  #activates a special exception handler that tell to browser
# cgitb.enable(display=0, logdir="/path/to/logdir")


 

conn = connector.connect(host='localhost',user='introdec',password='data73063',database='infotech')
cur = conn.cursor()

f = cgi.FieldStorage()

# getting the value from signup.js to what to do
d = f.getvalue("what")
image1=''
image2=''
image3=''

items=[]

# code for signup page into database
if(d=="insert"):
    try:
        usertype = f.getvalue("usertype")
        userid = f.getvalue("userid")
        username = f.getvalue("username")
        useremail = f.getvalue("useremail")
        mobno = f.getvalue("mobno")
        upass = f.getvalue("upass")
        uagree = f.getvalue("uagree")

        print(d)

        now = datetime.now()
        formatted_date = now.strftime('%Y-%m-%d') 
        registration_date = formatted_date

        last_formatted_date = now.strftime('%Y-%m-%d %H:%M:%S') 
        last_login  = last_formatted_date


        # print(registration_date)
        # print(uagree)
        if(uagree == 'on'):
            if(usertype != None and userid != None and username != None and useremail != None and mobno != None and upass != None and registration_date != None and last_login != None):
                insert_query = f"insert into user_info(userid, username,email, phone_number, password,registration_date,last_login,role) values('{userid}','{username}','{useremail}','{mobno}','{upass}','{registration_date}','{last_login}','{usertype}')"
                cur.execute(insert_query)
                conn.commit()
                print(insert_query)
                # x.insert_data(userid,username,useremail,mobno,upass,registration_date,last_login,usertype)  
                print('inserted')
            else:
                raise Exception("Error !!! One of the field is empty")
        else:
            raise Exception("Error !!! please agree the term and conditions")

    except Exception as e:
        print(e)

# code for fetching regno into option from database   
elif (d=="fetchuserid"):
    try:
        cur.execute("select distinct userid from user_info")
        res = cur.fetchall()
        # lst = set()
        if res != []:
            for row in res:
                # print(row[0])
                print(f"<option value='{row[0]}'>{row[0]}</option>")
        else:
            print()
    except Exception as e:
        print("some error",e)

# fetching data on click of search button or searching single data
elif(d=="fetch_by_id_name"):
    # print("fetch_by_id_name")
    try:
        userid = f.getvalue("userid")
        username = f.getvalue("username")
        if(userid != None and username != None):
            fetch_query = f"select * from user_info where userid='{userid}' and username = '{username}'"
            # print(fetch_query)
            cur.execute(fetch_query)
            srr = cur.fetchall()
            if srr != []:
                # print("<br>yes")
                for row in srr:
                    # print(row)
                    print("<table id='tab'>")
                    print("<tr>")
                    print("<th>user id</th>")
                    print("<th>user name</th>")
                    print("<th>user email</th>")
                    print("<th>phone</th>")
                    print("<th colspan='2'>Action</th>")
                    print("</tr>")
                    print("<tr>")
                    print(f'<td>{row[0]}</td>')
                    print(f'<td>{row[1]}</td>')
                    print(f'<td>{row[2]}</td>')
                    print(f'<td>{row[4]}</td>')
                    print(f'<td>{row[12]}</td>')
                    print(f"<td><button type='button' class='update' value='update'>update</button><button type='button' class='del' value='delete'>delete</button></td>")
                    print("</tr>")
                    print("</table>")
            else:
                # print("no")
                print("<table class='nodatatable'><tr><td>no data available</td></tr></table>")
        else:
            raise Exception("please enter remaining field")
    except Exception as e:
        print(e)

# code for fetching all records from the database
elif(d=="fetch_all"):
    # print(d)
    try:
        fetch_all_query = f"select * from user_info"
        # print(fetch_all_query)
        cur.execute(fetch_all_query)
        srr  = cur.fetchall()
        if srr != []:
            print("<table id='tab'>")
            print("<tr>")
            print("<th>User Id</th>")
            print("<th>User Name</th>")
            print("<th>User email</th>")
            print("<th>phone number</th>")
            print("<th>reg date</th>")
            print("<th>role</th>")
            print("<th class='action_th' colspan='2'>action</th>")
            print("<tr>")
            for row in srr:
                # print(row)
                print("<tr>")
                print(f'<td>{row[0]}</td>')
                print(f'<td>{row[1]}</td>')
                print(f'<td>{row[2]}</td>')
                print(f'<td>{row[4]}</td>')
                print(f'<td>{row[10]}</td>')
                print(f'<td>{row[12]}</td>')
                print(f"<td><button type='button' class='update' value='update'>update</button><button type='button' class='del' value='delete'>delete</button></td>")
                print("</tr>")

                # Creating JSON data
                # data = {
                #     "userid": row[0],
                #     "username": row[1],
                #     "email": row[2],
                #     "phone_number":row[4],
                # }

                # items.append(data)

            # Write the JSON string to a file
            # file_name = 'C:\\xampp\\htdocs\\Crazyhomes\\datas\\data.js'
            # with open(file_name, 'w') as js_file:
            #     js_file.write('const userData = ')
            #     json.dump(items, js_file, indent=4)
            #     js_file.write(';\n')

                # print("</tr>")
            print("</table>")
        else:
            print("<table><tr><td>no data available</td></td></table>")
    except Exception as e:
        print(e)

elif(d == "delete"):
    # print(d)
    try:
        userid = f.getvalue("userid")
        # print(userid + " have gotten")
        delete_query = f"delete from user_info where userid = '{userid}'"
        # print(delete_query)
        cur.execute(delete_query)
        conn.commit()
        print("data deleted successfully")
    except Exception as e:
        print(e)

elif(d == "fetchForUpdate"):
    # print(d)
    try:
        userid = f.getvalue("userid")
        # print(userid + " have gotten")
        if(userid != None):
            fetch_query_one = f"select * from user_info where userid='{userid}'"
            # print(fetch_query_one)
            cur.execute(fetch_query_one)
            res = cur.fetchall()
            if res != []:
                print("<div style='display:none;'>data fetching successfully</div>")
                # print(res)
                print("<form>")
                for row in res:
                    print(f"<label for='uid'>User Id </label><input id='uid' type='text' value='{row[0]}' disabled><br>")
                    print(f"<label for='uname'>User Name </label><input id='uname' type='text' value='{row[1]}'><br>")
                    print(f"<label for='uemail'>Email Id </label><input id='uemail' type='text' value='{row[2]}'><br>")
                    print(f"<label for='umob'>Phone No </label><input id='umob' type='text' value='{row[4]}'><br>")                    
                    print(f"<input id='save' type='button' value='save'><br>")  

                    # Creating JSON data
                    # data = {
                    #     "userid": row[0],
                    #     "username": row[1],
                    #     "email": row[2],
                    #     "phone_number":row[4],
                    # }

                    # items.append(data)

                # Serialize the data to a JSON formatted string
                # json_data = json.dumps(data, indent=4)  # 'indent' parameter for pretty printing

                # Write the JSON string to a file
                # with open('data.json', 'w') as json_file:
                    # json_file.write(json_data)                

                print("</form>")
            else:
                print("no data available")
    except Exception as e:
        print(e)


elif(d == "savetheupdate"):
    try:
        userid = f.getvalue("uid")
        username = f.getvalue("uname")
        useremail = f.getvalue("uemail")
        mobno = f.getvalue("umob")
        
        if(userid != None and username != None and useremail != None and mobno != None):
            saveTheUpdate_query = f"update user_info SET username = '{username}', email = '{useremail}', phone_number = '{mobno}' where userid = '{userid}'"
            cur.execute(saveTheUpdate_query)
            conn.commit()
            print("successfully saved")
        else:
            print("no field should be empty")
    except Exception as e:
        print(e)

elif (d=="insert_pro_cat"):
    print("product category")
    try:
        pro_cat_id = f.getvalue("pro_cat_id")
        pro_cat_name =f.getvalue("pro_cat_name")
        pro_cat_desc =f.getvalue("pro_cat_desc")

        if(pro_cat_id != None and pro_cat_name !=None and pro_cat_desc != None):
            insert_pro_cat_query = f"insert into product_category(prodcat_id, prodcat_name, prodcat_desc)  values('{pro_cat_id}','{pro_cat_name}','{pro_cat_desc}')"
            cur.execute(insert_pro_cat_query)
            conn.commit()
            print("product category inserted")
        else:
            raise Exception("Error !!! One of the field is empty")

    except Exception as e:
        print(e)
# code for fetching product cat id into option from database   
elif (d=="fetchcatid"):
    try:
        cur.execute("select distinct prodcat_id from product_category")
        res = cur.fetchall()
        # lst = set()
        if res != []:
            for row in res:
                # print(row[0])
                print(f"<option value='{row[0]}'>{row[0]}</option>")
        else:
            print()
    except Exception as e:
        print("some error",e)



# fetching data on click of search button or searching data
elif(d=="fetch_by_catid_catname"):
    # print(d)
    try:
        pro_cat_id = f.getvalue("pro_cat_id")
        pro_cat_name = f.getvalue("pro_cat_name")

        # Construct conditions for the SQL query
        conditions = []
        if pro_cat_id != None:
            conditions.append(f"prodcat_id = '{pro_cat_id}'")
        if pro_cat_name is not None:
            conditions.append(f"prodcat_name = '{pro_cat_name}'")
        

        # Construct the SQL query
        fetch_cat_query = "SELECT * FROM product_category"
        if conditions:
            fetch_cat_query += " WHERE " + " AND ".join(conditions)
       
        # print(fetch_cat_query)

        # print(fetch_cat_query)
        cur.execute(fetch_cat_query)
        srr = cur.fetchall()
        if srr != []:
            # print("<br>yes")
            print("<table class='tab'>")
            print("<tr>")
            print("<th>Product Category Id</th>")
            print("<th>Product Category Name</th>")
            print("<th>Product Category Desc</th>")
            print("<th colspan='2' style='text-align:center;'>Action</th>")
            print("</tr>")
            for row in srr:
                # print(row)
                print("<tr>")
                print(f'<td>{row[0]}</td>')
                print(f'<td>{row[1]}</td>')
                print(f'<td>{row[2]}</td>')
                print(f"<td><i class='fa-solid fa-pen-to-square fa-xl update'></i></td>")
                print(f"<td><i class='fa-solid fa-trash-can fa-xl del'></i></td>")
                print("</tr>")
            print("</table>")
            print("<p style='display:none;'>product category fetched successfully</p>")
        else:
            # print("no")
            print("no data available")
    except Exception as e:
        print(e)

# deleting product category on click of delete button
elif(d == "deletecat"):
    try:
        pro_cat_id = f.getvalue("pro_cat_id")
        print(pro_cat_id + " have gotten")
        delete_cat_query = f"delete from product_category where prodcat_id = '{pro_cat_id}'"
        print(delete_cat_query)
        cur.execute(delete_cat_query)
        conn.commit()
        print("data deleted successfully")
    except Exception as e:
        print(e)

elif(d == "fetchForcatUpdate"):
    # print(d)
    try:
        pro_cat_id = f.getvalue("pro_cat_id")
        # print(userid + " have gotten")
        if(pro_cat_id != None):
            fetch_query_cat_one = f"select * from product_category where prodcat_id='{pro_cat_id}'"
            # print(fetch_query_cat_one)
            cur.execute(fetch_query_cat_one)
            res = cur.fetchall()
            if res != []:
                print("<div style='display:none;'>data fetching successfully</div>")
                # print(res)
                print(f"<div class='updcard'>")
                print(f"<div class='cut'><i class='fa-solid fa-xmark fa-xl'></i></div>")
                print(f"<div>Update Product Category</div>")
                print("<form class='catupform'>")
                for row in res:
                    print(f"<label for='pcid'>Product Category Id </label><input id='pcid' type='text' value='{row[0]}' disabled><br>")
                    print(f"<label for='pcname'>Product Category Name </label><input id='pcname' type='text' value='{row[1]}'><br>")
                    print(f"<label for='pcdesc'>Product Category Desc </label><input id='pcdesc' type='text' value='{row[2]}'><br>")
                    print(f"<input class='save' type='button' value='save'><br>")  
              
                print("</form>")
                print("</div>")
                print("</div>")

            else:
                print("no data available")
    except Exception as e:
        print(e)


elif(d == "savethecatupdate"):
    try:
        pro_cat_id = f.getvalue("pro_cat_id")
        pro_cat_name = f.getvalue("pro_cat_name")
        pro_cat_desc = f.getvalue("pro_cat_desc")
        
        if(pro_cat_id != None and pro_cat_name != None and pro_cat_desc != None):
            saveCatUpdate_query = f"update product_category SET prodcat_name = '{pro_cat_name}', prodcat_desc = '{pro_cat_desc}' where prodcat_id = '{pro_cat_id}'"
            cur.execute(saveCatUpdate_query)
            conn.commit()
            print("successfully saved")
        else:
            print("no field should be empty")
    except Exception as e:
        print(e)

# inserting product details into database
elif (d=="insert_product"):
    print(d)
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

        if(prod_id != None and prod_name !=None and prod_cat_id != None and prod_stock !=None and prod_ori_price != None and prod_image1 !=None and prod_image2 != None and prod_image3 !=None and prod_desc != None):
            insert_prod_query = f"insert into product(product_id, product_name, category_id, stock_quant, original_price, discount_price, dimension, size, image_url1, image_url2, image_url3, product_desc) values('{prod_id}','{prod_name}','{prod_cat_id}','{prod_stock}','{prod_ori_price}','{prod_dis_price}','{prod_dimension}','{prod_size}','{prod_image1}','{prod_image2}','{prod_image3}','{prod_desc}')"
            print(insert_prod_query)
            cur.execute(insert_prod_query)
            conn.commit()
            print("product inserted")
        else:
            raise Exception("Error !!! One of the field is empty")

    except Exception as e:
        print(e)


# code for fetching product cat id into option from database   
elif (d=="fetchprodid"):
    try:
        cur.execute("select product_id, product_name from product")
        res = cur.fetchall()
        # lst = set()
        if res != []:
            for row in res:
                # print(row[0])
                print(f"<option value='{row[0]}'>{row[0]} -- {row[1]}</option>")
        else:
            print()
    except Exception as e:
        print("some error",e)



# fetching data on click of search button or searching data
elif(d=="fetch_prod_details_conditions"):
    # print(d)
    try:
        prod_id = f.getvalue("pro_id")
        prod_name = f.getvalue("prod_name")
        pro_cat_name = f.getvalue("pro_cat_name")
        pro_cat_id = f.getvalue("pro_cat_id")
        prod_stock = f.getvalue("prod_stock")
        prod_price_range = f.getvalue("prod_price_range")
        prod_size = f.getvalue("prod_size")
        

        # Construct conditions for the SQL query
        conditions = []
        if prod_id != None:
            conditions.append(f"product_id = '{prod_id}'")
        if prod_name is not None:
            conditions.append(f"product_name = '{prod_name}'")
        if pro_cat_id is not None:
            conditions.append(f"category_id = '{pro_cat_id}'")
        if prod_stock is not None:
            conditions.append(f"stock_quant >= '{prod_stock}'")
        if prod_price_range is not None:
            conditions.append(f"discount_price < '{prod_price_range}'")
        if prod_size != "---product size---":
            conditions.append(f"size = '{prod_size}'")

        # Construct the SQL query
        fetch_prod_query = "SELECT * FROM product"
        if conditions:
            fetch_prod_query += " WHERE " + " AND ".join(conditions)
       
        # print(fetch_prod_query)


        cur.execute(fetch_prod_query)
        srr = cur.fetchall()
        if srr != []:
            # print("<br>yes")
            print("<table class='tab'>")
            print("<tr>")
            print("<th>Product Id</th>")
            print("<th>Product Name</th>")
            print("<th>Category Id</th>")
            print("<th>Stock</th>")
            print("<th>MRP</th>")
            print("<th>Discount</th>")
            print("<th>Dimension</th>")
            print("<th>Size</th>")
            print("<th>images</th>")
            # print("<th>Size</th>")
            print("<th colspan='2' style='text-align:center;'>action</th>")
            print("</tr>")
            for row in srr:
                # print(row)
                print("<tr>")
                print(f'<td>{row[0]}</td>')
                print(f'<td>{row[1]}</td>')
                print(f'<td>{row[2]}</td>')
                print(f'<td>{row[3]}</td>')
                print(f'<td>{row[4]}</td>')
                print(f'<td>{row[5]}</td>')
                print(f'<td>{row[6]}</td>')
                print(f'<td>{row[7]}</td>')
                print(f'''<td><a class="view">View</a>
                      <div class="img_card">
            <div class="image_container">
                <div class="cut"><i class="fa-solid fa-xmark"></i></div>
                <img src="{row[8].decode()}" alt="product image1" class="items img1">
                <img src="{row[9].decode()}" alt="product image2" class="items img2">
                <img src="{row[10].decode()}" alt="product image3" class="items img3">
            </div>
            </div>
                      </td>''')
                # print(f'<td><div id="img_container"><img src="{row[8].decode()}"><img src="{row[9].decode()}"><img src="{row[10].decode()}"></div></td>')
                print(f"<td><div class='icon_div edit'><i class='fa-solid fa-pen-to-square fa-xl edit'  ></i></div></td>")
                print(f"<td><div class='icon_div del'><i class='fa-solid fa-trash-can fa-xl del'></i></div></td>")
                print("</tr>")
            print("</table>")
            print("<p style='display:none;'>product details fetched successfully</p>")
        else:
            # print("no")
            print("no data available")
    except Exception as e:
        print(e)

# deleting product category on click of delete button
elif(d == "deleteprod"):
    try:
        prod_id = f.getvalue("prod_id")
        # print(prod_id + " have gotten")
        delete_prod_query = f"delete from product where product_id = '{prod_id}'"
        # print(delete_prod_query)
        cur.execute(delete_prod_query)
        conn.commit()
        print("data deleted successfully")
    except Exception as e:
        print(e)


elif(d == "fetchForProdUpdate"):
    # print(d)
    try:
        prod_id = f.getvalue("prod_id_f")
        if(prod_id != None):
            fetch_query_prod_one = f"select * from product where product_id='{prod_id}'"
            cur.execute(fetch_query_prod_one)
            res = cur.fetchall()


            if res != []:
                for row in res:
                    print("<div style='display:none;'>data fetching successfully</div>")
                    # print(res)
                    # print(f'<div class="form_placeholder">')
                    print(f"<div class='updcard'>")
                    print("<div class='cut'><i class='fa-solid fa-xmark fa-xl'></i></div>")
                    print(f"<div>Update Product Details</div>")
                    print(f"<form>")
                    print(f"<table class='upd_tab'>")
                    print(f"<tr>")
                    print(f"    <td>")
                    print(f"        <label  for='prod_id'>Product Id*</label>")
                    print(f"        <input type='text' value='{row[0]}'  id='prod_id1' disabled>")
                    print(f"    </td>")
                    print(f"    <td>")
                    print(f"        <label  for='prod_name1'>Product Name*</label>")
                    print(f"        <input type='text' id='prod_name1' value='{row[1]}'>")
                    print(f"     </td>")
                    print(f"    <td>")
                    print(f"        <label  for='prod_cat_id'>Category Id</label>")
                    print(f"        <select id='prod_cat_id1'>")
                    print(f"            <option value='{row[2]}'>{row[2]}</option>")
                    print(f"        </select>")
                    print(f"    </td>")
                    print(f"</tr>")
                    print(f"<tr>")
                    print(f"    <td>")
                    print(f"        <label  for='prod_stock'>Stock Quantity*</label>")
                    print(f"        <input type='text' id='stock_size1' value='{row[3]}'>")
                    print(f"    </td>")
                    print(f"    <td>")
                    print(f"        <label  for='prod_ori_price'>Original Price*</label>")
                    print(f"        <input type='text' name='' id='prod_ori_price1' value='{row[4]}'>")
                    print(f"    </td>")
                    print(f"    <td>")
                    print(f"        <label  for='prod_dis_price'>Discounted Price</label>")
                    print(f"        <input type='text' name='' id='prod_dis_price1' value='{row[5]}'>")
                    print(f"    </td>")
                    print(f"</tr>")
                    print(f"<tr>")
                    print(f"    <td>")
                    print(f"        <label  for='prod_width'>produt width</label>")
                    print(f"        <input type='text' name='' class='dimen' id='upd_prod_width1' value='{row[6]}'>") 
                    print(f"    </td>")
                    print(f"    <td>")
                    print(f"        <label>Product Size</label>")
                    print(f"        <select name='' id='prod_size_upd1'>")
                    print(f"        <option value=''>---Select size---</option>")
                    print(f"        <option value='{row[7]}' selected >{row[7]}</option>")
                    print(f"        <option value='s'>S</option>")
                    print(f"        <option value='m'>M</option>")
                    print(f"        <option value='l'>L</option>")
                    print(f"        <option value='xl'>XL</option>")
                    print(f"        <option value='xxl'>XXL</option>")
                    print(f"        <option value='xxxl'>XXXL</option>")
                    print(f"        </select>")
                    print(f"    </td>")
                    print(f"    <td>")
                    print(f"        <label  for='prod_desc'>product description</label>")
                    print(f"        <input type='text' id='prod_desc1' value='{row[11]}'>")
                    print(f"    </td>")
                    print(f"</tr>")
                    print(f"<tr>")
                    print(f"    <td>")
                    print(f"        <img src='{row[8].decode()}' class='image' id='image1' > ")
                    print(f"        <input type='file' name='' id='prod_file1' value='{row[8].decode()}'   accept='image/*'>")
                    print(f"    </td>")
                    print(f"    <td>)")
                    print(f"        <img src='{row[9].decode()}' class='image' id='image2'>")
                    print(f"        <input type='file' name='' value='{row[9].decode()}' id='prod_file2' accept='image/*'>")
                    print(f"    </td>")
                    print(f"    <td>")
                    print(f"        <img src='{row[10].decode()}' class='image' id='image3'>")
                    print(f"        <input type='file' name='' id='prod_file3' value='{row[8].decode()}'  accept='image/*'>")
                    print(f"    </td>")
                    print(f"</tr>")
                    print(f"<tr>")
                    print(f"    <td class='btn_td' colspan='3'><button class='sub_btn save'>Save</button> <button type='reset' class='res_btn'>reset</button></td>")
                    print(f"</tr>")
                    print(f"</table>")
                    print(f"</form>")
                    # print(f"</div>")
                    print(f"</div>")
            else:
                print("no data available")
    except Exception as e:
        print(e)


elif(d == "savetheprodupdate"):
    try:
        prod_id1 = f.getvalue("prod_id1")
        prod_name1 = f.getvalue("prod_name1")
        prod_cat_id1 = f.getvalue("prod_cat_id1")
        prod_stock1 =f.getvalue("prod_stock1")
        prod_ori_price1 = f.getvalue("prod_ori_price1")
        prod_dis_price1 = f.getvalue("prod_dis_price1")
        upd_prod_width1 = f.getvalue("upd_prod_width1")
        prod_size_upd1 = f.getvalue("prod_size_upd1")
        prod_image1 = f.getvalue("prod_file11")
        prod_image2 = f.getvalue("prod_file21")
        prod_image3 = f.getvalue("prod_file31")
        prod_desc1 = f.getvalue("prod_desc1")

      
        
        
        if(prod_id1 != None and prod_name1 !=None and prod_cat_id1 != None  and prod_ori_price1 != None and  prod_desc1 != None and prod_image1 != None and prod_image2 != None and prod_image3 != None):
            saveProdUpdate_query = f"update product SET product_name = '{prod_name1}', category_id = '{prod_cat_id1}',stock_quant = '{prod_stock1}',original_price = '{prod_ori_price1}',discount_price = '{prod_dis_price1}',dimension = '{upd_prod_width1}',size = '{prod_size_upd1}', image_url1 = '{prod_image1}',image_url2 = '{prod_image2}',image_url3 = '{prod_image3}' ,product_desc='{prod_desc1}' where product_id = '{prod_id1}'"
            # print(saveProdUpdate_query)
            cur.execute(saveProdUpdate_query)
            conn.commit()
            print("successfully updated the product data")
        else:
            print("no field should be empty")
    except Exception as e:
        print(e)

elif(d == "insert_order"):
    try:
        order_id = f.getvalue("order_id")
        user_id = f.getvalue("user_id")
        order_date = f.getvalue("order_date")
        shipping_addr = f.getvalue("shipping_addr")

        if( order_id != None and user_id != None and order_date != None
        and shipping_addr != None):
            cur.execute(f'select * from order_info where order_id="{order_id}"')
            if cur.fetchall()==[]:
                order_insert_query = f"insert into order_info (order_id,user_id,order_date,shipping_addr) values('{order_id}','{user_id}','{order_date}','{shipping_addr}')"
                print(order_insert_query)
                cur.execute(order_insert_query)
                conn.commit()
                print("order inserted successfully")
            else:
                print("order already exists")
        else:
            print("one of the field is empty")
    except Exception as e:
        print(e)

# code for fetching product cat id into option from database   
elif (d=="fetchorderid"):
    try:
        cur.execute("select distinct order_id from order_info")
        res = cur.fetchall()
        # lst = set()
        if res != []:
            #  print('<option value="">-- Select Order Id --</option>')
            for row in res:
                print(f"<option value='{row[0]}'>{row[0]}</option>")
        else:
            print()
    except Exception as e:
        print("some error",e)

# fetching data on click of search button or searching data
elif(d=="fetch_order_details_conditions"):
    # print(d)
    try:
        order_id = f.getvalue("order_id")
        user_id = f.getvalue("user_id")
        order_date = f.getvalue("order_date")
        

        # Construct conditions for the SQL query
        conditions = []
        if order_id != None:
            conditions.append(f"order_id = '{order_id}'")
        if user_id is not None:
            conditions.append(f"user_id = '{user_id}'")
        if order_date is not None:
            conditions.append(f"order_date = '{order_date}'")
        
        # Construct the SQL query
        fetch_order_query = "SELECT * FROM order_info"
        if conditions:
            fetch_order_query += " WHERE " + " AND ".join(conditions)
       
        # print(fetch_order_query)


        cur.execute(fetch_order_query)
        srr = cur.fetchall()
        if srr != []:
            # print("<br>yes")
            print("<table class='tab'>")
            print("<tr>")
            print("<th>Order Id</th>")
            print("<th>User Id</th>")
            print("<th>Order Date</th>")
            print("<th>Stock</th>")
            # print("<th>Size</th>")
            print("<th colspan='2' style='text-align:center;'>action</th>")
            print("</tr>")
            for row in srr:
                # print(row)
                print("<tr>")
                print(f'<td>{row[0]}</td>')
                print(f'<td>{row[1]}</td>')
                print(f'<td>{row[2]}</td>')
                print(f'<td>{row[3]}</td>')
                # print(f'<td><div id="img_container"><img src="{row[8].decode()}"><img src="{row[9].decode()}"><img src="{row[10].decode()}"></div></td>')
                print(f"<td><div class='icon_div edit'><i class='fa-solid fa-pen-to-square fa-xl edit'  ></i></div></td>")
                print(f"<td><div class='icon_div del'><i class='fa-solid fa-trash-can fa-xl del'></i></div></td>")
                print("</tr>")
            print("</table>")
            print("<p style='display:none;'>product details fetched successfully</p>")
        else:
            # print("no")
            print("no data available")
    except Exception as e:
        print(e)

elif(d == "deleteorder"):
    try:
        order_id = f.getvalue("order_id")
        # print(prod_id + " have gotten")
        delete_order_query = f"delete from order_info where order_id = '{order_id}'"
        # print(delete_prod_query)
        cur.execute(delete_order_query)
        conn.commit()
        print("data deleted successfully")
    except Exception as e:
        print(e)

elif(d == "fetchForOrderUpdate"):
    # print(d)
    try:
        order_id = f.getvalue("order_id")
        if(order_id != None):
            fetch_query_order_one = f"select * from order_info where order_id='{order_id}'"
            cur.execute(fetch_query_order_one)
            res = cur.fetchall()

            if res != []:
                for row in res:
                    print("<div style='display:none;'>data fetching successfully</div>")
                    # print(res)
                    # print(f'<div class="form_placeholder">')
                    print(f"<div class='updcard'>")
                    print("<div class='cut'><i class='fa-solid fa-xmark fa-xl'></i></div>")
                    print(f"<div>Update Product Details</div>")
                    print(f"<form>")
                    print(f"<table class='upd_tab'>")
                    print(f"<tr>")
                    print(f"    <td>")
                    print(f"        <label  for='order_id1'>Order Id*</label>")
                    print(f"        <input type='text' value='{row[0]}'  id='order_id1' disabled>")
                    print(f"    </td>")
                    print(f"    <td>")
                    print(f"        <label  for='user_id1'>User Id*</label>")
                    print(f"        <input type='text' id='user_id1' value='{row[1]}'>")
                    print(f"     </td>")
                    print(f"</tr>")
                    print(f"<tr>")
                    print(f"     <td>")
                    print(f"        <label  for='order_date1'>Order Date*</label>")
                    print(f"        <input type='date' id='order_date1' value='{row[2]}'>")
                    print(f"    </td>")
                    print(f"     <td>")
                    # print(f"        <label class='lab ship_lab'  for='shipping_addr1'>Order Date*</label>")
                    print(f"        <textarea id='shipping_addr1' value='{row[3]}'>{row[3]}</textarea>")
                    print(f"    </td>")
                    print(f"</tr>")
                    print(f"<tr>")
                    print(f"    <td class='btn_td' colspan='3'><button class='sub_btn save'>Save</button> <button type='reset' class='res_btn'>reset</button></td>")
                    print(f"</tr>")
                    print(f"</table>")
                    print(f"</form>")
                    # print(f"</div>")
                    print(f"</div>")
            else:
                print("no data available")
    except Exception as e:
        print(e)


elif(d == "saveorderupdate"):
    try:
        order_id1 = f.getvalue("order_id1")
        user_id1 = f.getvalue("user_id1")
        order_date1 = f.getvalue("order_date1")
        shipping_addr1 =f.getvalue("shipping_addr1")

      
        
        
        if(order_id1 != None and user_id1 !=None and order_date1 != None  and shipping_addr1 != None):
            saveOrderUpdate_query = f"update order_info SET user_id = '{user_id1}', order_date = '{order_date1}',shipping_addr = '{shipping_addr1}' where order_id = '{order_id1}'"
            # print(saveProdUpdate_query)
            cur.execute(saveOrderUpdate_query)
            conn.commit()
            print("successfully updated the order data")
        else:
            print("no field should be empty")
        
        # cur.execute(f"select * from order_info where order_id='{order_id1}'")
    except Exception as e:
        print(e)


# order details page
elif (d=="fetchproductprice"):
    try:
        prod_id= f.getvalue("prod_id")
        cur.execute(f"select distinct discount_price from product where product_id='{prod_id}'")
        res = cur.fetchall()
        # lst = set()
        if res != []:
            #  print('<option value="">-- Select Order Id --</option>')
            for row in res:
                print(row[0])
        else:
            print()
    except Exception as e:
        print("some error",e)


elif (d=="fetchproductid"):
    try:
        prod_id= f.getvalue("prod_id")
        cur.execute(f"select product_id from product where product_id='{prod_id}'")
        res = cur.fetchall()
        # lst = set()
        if res != []:
            #  print('<option value="">-- Select Order Id --</option>')
            for row in res:
                print(row[0])
            print("productid exist")
        else:
            print("no product id available")
    except Exception as e:
        print("some error",e)

# insert order full details

elif(d == "insert_final_order"):
    try:
        order_id = f.getvalue("order_id")
        product_id = f.getvalue("prod_id")
        quantity = f.getvalue("quantity")
        amount = f.getvalue("amount")

        print(amount)

        if( order_id != None and product_id != None and quantity != None
        and amount != None):
            # cur.execute(f'select * from order_details where order_id="{order_id}"')
            # if cur.fetchall()==[]:
            order_insert_details_query = f"insert into order_details (order_id,product_id,quantity,amount) values('{order_id}','{product_id}','{quantity}','{amount}')"
            print(order_insert_details_query)
            cur.execute(order_insert_details_query)
            conn.commit()
            print("order details inserted successfully")
            # else:
            #     print("order already exists")
        else:
            print("one of the field is empty")
    except Exception as e:
        print(e)


# fetching data on click of search button or searching data
elif(d=="fetch_final_order_conditions"):
    # print(d)
    try:
        order_id = f.getvalue("order_id")
        user_id = f.getvalue("user_id")
        order_date = f.getvalue("order_date")
        

        # Construct conditions for the SQL query
        conditions = []
        if order_id != None:
            conditions.append(f"order_id = '{order_id}'")
        if user_id is not None:
            conditions.append(f"user_id = '{user_id}'")
        if order_date is not None:
            conditions.append(f"order_date = '{order_date}'")
        
        # Construct the SQL query
        fetch_final_order_query = '''SELECT distinct * FROM order_info
        join order_details on order_info.order_id = order_details.order_id
        '''
        if conditions:
            fetch_final_order_query += " WHERE " + " AND ".join(conditions)
       
        print(fetch_final_order_query)
        '''SELECT *
        FROM table1 t1
        JOIN table2 t2 ON t1.user_id = t2.user_id
        WHERE t1.user_id = 'your_user_id'
        OR t1.order_id = 'your_order_id'
        OR t1.order_date = 'your_order_date';'''


        cur.execute(fetch_final_order_query)
        srr = cur.fetchall()
        if srr != []:
            # print("<br>yes")
            print("<table class='tab'>")
            print("<tr>")
            print("<th>Order Id</th>")
            print("<th>User Id</th>")
            print("<th>Order Date</th>")
            print("<th>Shipping Address</th>")
            print("<th>Product Id</th>")
            print("<th>Quantity</th>")
            print("<th>Amount</th>")
            # print("<th>Size</th>")
            print("<th colspan='2' style='text-align:center;'>action</th>")
            print("</tr>")
            for row in srr:
                # print(row)
                print("<tr>")
                print(f'<td>{row[0]}</td>')
                print(f'<td>{row[1]}</td>')
                print(f'<td>{row[2]}</td>')
                print(f'<td>{row[3]}</td>')
                print(f'<td>{row[4]}</td>')
                print(f'<td>{row[6]}</td>')
                print(f'<td>{row[7]}</td>')
                # print(f'<td>{row[8]}</td>')
                # print(f'<td><div id="img_container"><img src="{row[8].decode()}"><img src="{row[9].decode()}"><img src="{row[10].decode()}"></div></td>')
                print(f"<td><div class='icon_div edit'><i class='fa-solid fa-pen-to-square fa-xl edit'  ></i></div></td>")
                print(f"<td><div class='icon_div del'><i class='fa-solid fa-trash-can fa-xl del'></i></div></td>")
                print("</tr>")
            print("</table>")
            print("<p style='display:none;'>product details fetched successfully</p>")
        else:
            # print("no")
            print("no data available")
    except Exception as e:
        print(e)

elif(d == "deleteorder"):
    try:
        order_id = f.getvalue("order_id")
        # print(prod_id + " have gotten")
        delete_order_query = f"delete from order_info where order_id = '{order_id}'"
        # print(delete_prod_query)
        cur.execute(delete_order_query)
        conn.commit()
        print("data deleted successfully")
    except Exception as e:
        print(e)

elif(d == "fetchForOrderUpdate"):
    # print(d)
    try:
        order_id = f.getvalue("order_id")
        if(order_id != None):
            fetch_query_order_one = f"select * from order_info where order_id='{order_id}'"
            cur.execute(fetch_query_order_one)
            res = cur.fetchall()

            if res != []:
                for row in res:
                    print("<div style='display:none;'>data fetching successfully</div>")
                    # print(res)
                    # print(f'<div class="form_placeholder">')
                    print(f"<div class='updcard'>")
                    print("<div class='cut'><i class='fa-solid fa-xmark fa-xl'></i></div>")
                    print(f"<div>Update Product Details</div>")
                    print(f"<form>")
                    print(f"<table class='upd_tab'>")
                    print(f"<tr>")
                    print(f"    <td>")
                    print(f"        <label  for='order_id1'>Order Id*</label>")
                    print(f"        <input type='text' value='{row[0]}'  id='order_id1' disabled>")
                    print(f"    </td>")
                    print(f"    <td>")
                    print(f"        <label  for='user_id1'>User Id*</label>")
                    print(f"        <input type='text' id='user_id1' value='{row[1]}'>")
                    print(f"     </td>")
                    print(f"</tr>")
                    print(f"<tr>")
                    print(f"     <td>")
                    print(f"        <label  for='order_date1'>Order Date*</label>")
                    print(f"        <input type='date' id='order_date1' value='{row[2]}'>")
                    print(f"    </td>")
                    print(f"     <td>")
                    # print(f"        <label class='lab ship_lab'  for='shipping_addr1'>Order Date*</label>")
                    print(f"        <textarea id='shipping_addr1' value='{row[3]}'>{row[3]}</textarea>")
                    print(f"    </td>")
                    print(f"</tr>")
                    print(f"<tr>")
                    print(f"    <td class='btn_td' colspan='3'><button class='sub_btn save'>Save</button> <button type='reset' class='res_btn'>reset</button></td>")
                    print(f"</tr>")
                    print(f"</table>")
                    print(f"</form>")
                    # print(f"</div>")
                    print(f"</div>")
            else:
                print("no data available")
    except Exception as e:
        print(e)


elif(d == "saveorderupdate"):
    try:
        order_id1 = f.getvalue("order_id1")
        user_id1 = f.getvalue("user_id1")
        order_date1 = f.getvalue("order_date1")
        shipping_addr1 =f.getvalue("shipping_addr1")

      
        
        
        if(order_id1 != None and user_id1 !=None and order_date1 != None  and shipping_addr1 != None):
            saveOrderUpdate_query = f"update order_info SET user_id = '{user_id1}', order_date = '{order_date1}',shipping_addr = '{shipping_addr1}' where order_id = '{order_id1}'"
            # print(saveProdUpdate_query)
            cur.execute(saveOrderUpdate_query)
            conn.commit()
            print("successfully updated the order data")
        else:
            print("no field should be empty")
        
        # cur.execute(f"select * from order_info where order_id='{order_id1}'")
    except Exception as e:
        print(e)











# else:
#     try:
#         cur.execute('select image_url1 from product order by product_id limit 1')
#         print(cur.fetchall()[0][0].decode())
#     except Exception as e:
#         print(str(e))