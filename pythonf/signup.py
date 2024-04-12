#! C:\Users\divya\AppData\Local\Programs\Python\Python312\python.exe
print ("Content-Type: text/html\r\n\r\n")
import cgi
import mysql.connector as connector

con = connector.connect(host="localhost",user="introdec",passwd="data73063", database="infotech")
cur = con.cursor()

qry = 'insert into regdetails values(%s,%s,%s,%s,%s,%s,%s,%s)'
f = cgi.FieldStorage()

try:
    userid2 = f.getvalue("userid1")
    ufname2 = f.getvalue("ufname1")
    ulname2 = f.getvalue("ulname1")
    useremail2 = f.getvalue("useremail1")
    mobno2 = f.getvalue("mobno1")
    upass2 = f.getvalue("upass1")
    urpass2 = f.getvalue("urpass1")
    uagree2 = f.getvalue("uagree1")
    
    query = f"insert into user(userId, userName, phone) values({userid2},'{ufname2}','{ulname2}')"
    cur.execute(qry,(userid2,ufname2,ulname2,useremail2,mobno2,upass2,urpass2,uagree2))
    con.commit()
    print('successfully record inserted')
except Exception as e:
    print("something went wrong " + e)

