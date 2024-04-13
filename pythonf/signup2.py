#! C:\Users\divya\AppData\Local\Programs\Python\Python312\python.exe
print ("Content-Type: text/html\r\n\r\n")
import cgi
import mysql.connector as connector
import DBHelper 
from datetime import datetime




 

# con = connector.connect(host="localhost",user="introdec",passwd="data73063", database="infotech")
x = DBHelper.DBHelper()
print(x)

# qry = 'insert into regdetails values(%s,%s,%s,%s,%s,%s,%s,%s)'
f = cgi.FieldStorage()

try:
    flag = False
    usertype = f.getvalue("usertype")
    userid = f.getvalue("userid")
    username = f.getvalue("username")
    useremail = f.getvalue("useremail")
    mobno = f.getvalue("mobno")
    upass = f.getvalue("upass")
    uagree = f.getvalue("uagree")

    now = datetime.now()
    formatted_date = now.strftime('%Y-%m-%d') 

    registration_date = formatted_date
    print(registration_date)
    print(uagree)
    # cur.execute(query,(userid2,ufname2,ulname2,useremail2,mobno2,upass2,urpass2,uagree2))
    # insertQuery = f"insert into user_info(userid, username, email, phone_number,password) values('{userid}','{username}','{useremail}','{mobno}','{upass}')"
    if(uagree == 'on'):
        x.insert_data(userid,username,useremail,mobno,upass,registration_date)  
        # x.delete_data(userid)
        # x.fetch_all()
        # x.updata_data(userid,username,useremail,mobno,upass)
        print('inserted')
    else:
        raise Exception("please agree the term and conditions")
except Exception as e:
    print("something went wrong " , e)

