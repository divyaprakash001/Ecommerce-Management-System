#! C:\Users\divya\AppData\Local\Programs\Python\Python312\python.exe
print ("Content-Type: text/html\r\n\r\n")
import cgi
import mysql.connector as connector

con = connector.connect(host="localhost",user="introdec",passwd="data73063", database="infotech")
cur = con.cursor()

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
    
    print(uagree)
    # cur.execute(query,(userid2,ufname2,ulname2,useremail2,mobno2,upass2,urpass2,uagree2))
    insertQuery = f"insert into user_info(userid, username, email, phone_number,password) values('{userid}','{username}','{useremail}','{mobno}','{upass}')"
    if(uagree == 'on'):
        cur.execute(insertQuery)
        con.commit()  
        print('inserted')
    else:
        raise Exception("please agree the term and conditions")
except Exception as e:
    print("something went wrong " , e)

