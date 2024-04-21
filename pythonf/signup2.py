#! C:\Users\divya\AppData\Local\Programs\Python\Python312\python.exe
print ("Content-Type: text/html\r\n\r\n")
import cgi
import mysql.connector as connector
from DBHelper import *
from datetime import datetime




 

# con = connector.connect(host="localhost",user="introdec",passwd="data73063", database="infotech")
# creating object of DBHelper which contain connection data
x = DBHelper()
# print(x)

f = cgi.FieldStorage()

# getting the value from signup.js to what to do
d = f.getvalue("what")

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
        for row in res:
            # print(row[0])
            print(f"<option value='{row[0]}'>{row[0]}</option>")
        # print(lst)
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
            if cur != None:
                for row in cur:
                    # print(row)
                    print("<tr>")
                    print(f'<td>{row[0]}</td>')
                    print(f'<td>{row[1]}</td>')
                    print(f'<td>{row[2]}</td>')
                    print(f'<td>{row[4]}</td>')
                    print("</tr>")
            else:
                print("no data available")
        else:
            raise Exception("please enter remaining field")
    except Exception as e:
        print(e)

     
