#! C:\Users\divya\AppData\Local\Programs\Python\Python312\python.exe
print ("Content-Type: text/html\r\n\r\n")
import cgi
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
    # print("hello ")
    print(f"User id :: {userid2}")
    print(f"User name :: {ufname2 + ' ' + ulname2}")
    print(f"User email :: {useremail2}")
    print(f"User mob :: {mobno2}")
    print(f"User pass :: {upass2}")
    print(f"User repeat pass :: {urpass2}")
    print(f"User agree :: {uagree2}")
except:
    print("something went wrong")

