#! C:\Users\divya\AppData\Local\Programs\Python\Python312\python.exe
print ("Content-Type: text/html\r\n\r\n")
import cgi
import mysql.connector as connector
from DBHelper import *
from datetime import datetime
import json




 

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
            print("<th class='action_th' colspan='2'>action</th>")
            print("<tr>")
            for row in srr:
                # print(row)
                print("<tr>")
                print(f'<td>{row[0]}</td>')
                print(f'<td>{row[1]}</td>')
                print(f'<td>{row[2]}</td>')
                print(f'<td>{row[4]}</td>')
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


