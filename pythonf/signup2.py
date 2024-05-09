#! C:\Users\divya\AppData\Local\Programs\Python\Python312\python.exe
print ("Content-Type: text/html\r\n\r\n")
import cgi
import mysql.connector as connector
from DBHelper import *
from datetime import datetime
import json
import os




 

# con = connector.connect(host="localhost",user="introdec",passwd="data73063", database="infotech")
# creating object of DBHelper which contain connection data
x = DBHelper()
# print(x)

f = cgi.FieldStorage()

# getting the value from signup.js to what to do
d = f.getvalue("what")

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
                cur= x.conn.cursor()
                cur.execute(insert_query)
                x.conn.commit()
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
        cur = x.conn.cursor()
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
            cur=x.conn.cursor()
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
                    print("<th colspan='2'>action</th>")
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
        cur=x.conn.cursor()
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
                data = {
                    "userid": row[0],
                    "username": row[1],
                    "email": row[2],
                    "phone_number":row[4],
                }

                items.append(data)

            # Write the JSON string to a file
            file_name = 'C:\\xampp\\htdocs\\Crazyhomes\\datas\\data.js'
            with open(file_name, 'w') as js_file:
                js_file.write('const userData = ')
                json.dump(items, js_file, indent=4)
                js_file.write(';\n')

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
        cur=x.conn.cursor()
        cur.execute(delete_query)
        x.conn.commit()
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
            cur=x.conn.cursor()
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
            cur=x.conn.cursor()
            cur.execute(saveTheUpdate_query)
            x.conn.commit()
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
            cur = x.conn.cursor()
            cur.execute(insert_pro_cat_query)
            x.conn.commit()
            print("product category inserted")
        else:
            raise Exception("Error !!! One of the field is empty")

    except Exception as e:
        print(e)
# code for fetching product cat id into option from database   
elif (d=="fetchcatid"):
    try:
        cur = x.conn.cursor()
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
       
        print(fetch_cat_query)

        # print(fetch_cat_query)
        cur=x.conn.cursor()
        cur.execute(fetch_cat_query)
        srr = cur.fetchall()
        if srr != []:
            # print("<br>yes")
            print("<table class='tab'>")
            print("<tr>")
            print("<th>Product Category Id</th>")
            print("<th>Product Category Name</th>")
            print("<th>Product Category Desc</th>")
            print("<th colspan='2' style='text-align:center;'>action</th>")
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
        cur=x.conn.cursor()
        cur.execute(delete_cat_query)
        x.conn.commit()
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
            cur=x.conn.cursor()
            cur.execute(fetch_query_cat_one)
            res = cur.fetchall()
            if res != []:
                print("<div style='display:none;'>data fetching successfully</div>")
                # print(res)
                print("<span><i class='fa-solid fa-xmark fa-2xl'></i></span>")
                print("<form class='catupform'>")
                for row in res:
                    print(f"<label for='pcid'>Product Category Id </label><input id='pcid' type='text' value='{row[0]}' disabled><br>")
                    print(f"<label for='pcname'>Product Category Name </label><input id='pcname' type='text' value='{row[1]}'><br>")
                    print(f"<label for='pcdesc'>Product Category Desc </label><input id='pcdesc' type='text' value='{row[2]}'><br>")
                    print(f"<input id='save' type='button' value='save'><br>")  
              
                print("</form>")
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
            cur=x.conn.cursor()
            cur.execute(saveCatUpdate_query)
            x.conn.commit()
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
            cur = x.conn.cursor()
            cur.execute(insert_prod_query)
            x.conn.commit()
            print("product inserted")
        else:
            raise Exception("Error !!! One of the field is empty")

    except Exception as e:
        print(e)


# code for fetching product cat id into option from database   
elif (d=="fetchprodid"):
    try:
        cur = x.conn.cursor()
        cur.execute("select distinct product_id from product")
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
elif(d=="fetch_prod_details_conditions"):
    print(d)
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


        cur=x.conn.cursor()
        cur.execute(fetch_prod_query)
        srr = cur.fetchall()
        if srr != []:
            # print("<br>yes")
            print("<table class='tab'>")
            print("<tr>")
            print("<th>Product Id</th>")
            print("<th>Product Name</th>")
            print("<th>Category Id</th>")
            print("<th>Stock Quantity</th>")
            print("<th>Original Price</th>")
            print("<th>Discount Price</th>")
            print("<th>Dimension</th>")
            print("<th>Size</th>")
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
elif(d == "deleteprod"):
    try:
        prod_id = f.getvalue("prod_id")
        # print(prod_id + " have gotten")
        delete_prod_query = f"delete from product where product_id = '{prod_id}'"
        # print(delete_prod_query)
        cur=x.conn.cursor()
        cur.execute(delete_prod_query)
        x.conn.commit()
        print("data deleted successfully")
    except Exception as e:
        print(e)


elif(d == "fetchForProdUpdate"):
    # print(d)
    try:
        prod_id = f.getvalue("prod_id")
        # print(userid + " have gotten")
        if(prod_id != None):
            fetch_query_prod_one = f"select * from product where product_id='{prod_id}'"
            # print(fetch_query_prod_one)
            cur=x.conn.cursor()
            cur.execute(fetch_query_prod_one)
            res = cur.fetchall()

            # redirectURL = "http://localhost/Crazyhomes/pages-product_update.html"
            # print('<html>')
            # print('  <head>')
            # print('    <meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />') 
            # print('  </head>')
            # print('</html>')

            if res != []:
                print("<div style='display:none;'>data fetching successfully</div>")
                # print(res)
                print("<span><i class='fa-solid fa-xmark fa-2xl'></i></span>")
                # print("<form class='catupform'>")
                for row in res:
                    print(f'''<section class='section'>"
                    <div class='updcard'>
                    <span>Update Product Details</span>
                    <form>
                    <table class='upd_tab'>
                    <tr>
                    <td>
                    <label  for='prod_id'>Product Id*</label>
                    <input type='text' value='{row[0]}'  id='prod_id' disable>
                    </td>
                    <td>
                    <label  for='prod_name'>Product Name*</label>
                    <input type='text' id='prod_name' value='{row[1]}'>
                    </td>
                    <td>
                    <label  for='prod_id'>Category Id</label>
                    <select id='prod_cat_id'>
                    <option value='{row[2]}'>{row[2]}</option>
                    </select>
                    </td>

                    </tr>
                    <tr>
                    <td>
                    <label  for='prod_stock'>Stock Quantity*</label>
                    <input type='text' name='' id='prod_stock' value='{row[3]}'>
                    </td>
                    <td>
                    <label  for='prod_ori_price'>Original Price*</label>
                    <input type='text' name='' id='prod_ori_price' value='{row[4]}'>
                    </td>
                    <td>
                    <label  for='prod_dis_price'>Discounted Price</label>
                    <input type='text' name='' id='prod_dis_price' value='{row[5]}'>
                    </td>

                    </tr>

                    <tr>
                    <td>
                    <label  for='prod_width'>produt width</label>
                    <input type='text' name='' class='dimen' id='upd_prod_width' value='{row[6]}'> 
                    </td>
                    <td>
                    <label>Product Size</label>
                    <select name='' id='prod_size'>
                    <option value='{row[7]}'>{row[7]}</option>
                    <option value='s'>S</option>
                    <option value='m'>M</option>
                    <option value='l'>L</option>
                    <option value='xl'>XL</option>
                    <option value='xxl'>XXL</option>
                    <option value='xxxl'>XXXL</option>
                    </select>
                    </td>
                    <td>
                        <label  for='prod_id'>image 1</label>
                        <input type='file' name='' id='prod_file1' value='{row[8]}' accept='image/*'>
                    </td>

                    </tr>
                    <tr>
                    <td>
                        <label  for='prod_id'>image 2</label>
                        <input type='file' name='' id='prod_file2' accept='image/*'>
                    </td>
                    <td>
                        <label  for='prod_id'>image 3</label>
                        <input type='file' name='' id='prod_file3' accept='image/*'>
                    </td>
                    <td>
                        <label  for='prod_desc'>product description</label>
                        <input type='text' id='prod_desc' value='{row[11]}'>
                    </td>
                    </tr>
                    <tr>
                    <td class='btn_td' colspan='3'><button class='sub_btn' id='save'>Save</button> <button
                        class='res_btn'>reset</button></td>
                    </tr>
                    </table>
                    </form>


                    </div>
                    </section>''')
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
            cur=x.conn.cursor()
            cur.execute(saveCatUpdate_query)
            x.conn.commit()
            print("successfully saved")
        else:
            print("no field should be empty")
    except Exception as e:
        print(e)
