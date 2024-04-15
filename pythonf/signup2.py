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
    
    usertype = f.getvalue("usertype")
    userid = f.getvalue("userid")
    username = f.getvalue("username")
    useremail = f.getvalue("useremail")
    mobno = f.getvalue("mobno")
    upass = f.getvalue("upass")
    uagree = f.getvalue("uagree")
    flag = f.getvalue("uflag")

    print(flag)

    # if(userid == None):
    #     print("User id is none value")
    
    now = datetime.now()
    formatted_date = now.strftime('%Y-%m-%d') 
    registration_date = formatted_date

    last_formatted_date = now.strftime('%Y-%m-%d %H:%M:%S') 
    last_login  = last_formatted_date


    print(registration_date)
    print(uagree)
    # cur.execute(query,(userid2,ufname2,ulname2,useremail2,mobno2,upass2,urpass2,uagree2))
    # insertQuery = f"insert into user_info(userid, username, email, phone_number,password) values('{userid}','{username}','{useremail}','{mobno}','{upass}')"
    if(uagree == 'on'):
        if(usertype != None and userid != None and username != None and useremail != None and mobno != None and upass != None and registration_date != None and last_login != None):
            x.insert_data(userid,username,useremail,mobno,upass,registration_date,last_login,usertype)  
            print('inserted')
        else:
            raise Exception("Error !!! One of the field is empty")
    else:
        raise Exception("Error !!! please agree the term and conditions")
        
except Exception as e:
    print(e)

