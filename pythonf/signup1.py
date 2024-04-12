#! C:\Users\divya\AppData\Local\Programs\Python\Python312\python.exe
print ("Content-Type: text/html\r\n\r\n")
import cgi
# import DBHelper 
import json
import sys
import mysql.connector as connector

mydb = connector.connect(
    host="localhost",
    user="root",
    passwd="data73063",
    database = "divya"
)

f = cgi.FieldStorage()

sys.stdout.write("Content-Type: application/json")
sys.stdout.write("\n")
sys.stdout.write("\n")
mycursor = mydb.cursor()

sqlQuery = "select * from persons"

result={}
result['success'] = True
result['message'] = "The command completed successfully"
result['keys'] = ",".join(f.keys())

mycursor.execute(sqlQuery)
myresult = mycursor.fetchall()

result['data'] = myresult

sys.stdout.write(json.dumps(result,indent=1))
sys.stdout.write("\n")

sys.stdout.close()



# try:
#     userid2 = f.getvalue("userid1")
#     ufname2 = f.getvalue("ufname1")
#     ulname2 = f.getvalue("ulname1")
#     useremail2 = f.getvalue("useremail1")
#     mobno2 = f.getvalue("mobno1")
#     upass2 = f.getvalue("upass1")
#     urpass2 = f.getvalue("urpass1")
#     uagree2 = f.getvalue("uagree1")
#     # print("hello ")
#     print(f"User id :: {userid2}")
#     print(f"User name :: {ufname2 + ' ' + ulname2}")
#     print(f"User email :: {useremail2}")
#     print(f"User mob :: {mobno2}")
#     print(f"User pass :: {upass2}")
#     print(f"User repeat pass :: {urpass2}")
#     print(f"User agree :: {uagree2}")
# except Exception as e:
#     print("something went wrong " + e)



