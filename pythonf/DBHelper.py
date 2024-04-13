import mysql.connector as connector

class DBHelper:
    # using class constructor to initialize and create connection object here
    
    def __init__(self):
        self.conn = connector.connect(host='localhost',user='introdec',password='data73063',database='infotech')
        # query = 'create table if not exists user(userId int primary key, userName varchar(25), phone varchar(13))'
        # cur = self.conn.cursor()
        # cur.execute(query)
        # print('table created if not exist')
    
    # insert data
    def insert_data(self,userId, userName,userEmail, phone, upass,registration_date):
        query = f"insert into user_info(userid, username,email, phone_number, password,registration_date) values('{userId}','{userName}','{userEmail}','{phone}','{upass}','{registration_date}')"
        print(query)
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        print("user data inserted")
    
    # fetch one data using userid
    def fetch_by_id(self,userid):
        query = f"select * from user_info where userid = {userid}"
        cur = self.conn.cursor()
        cur.execute(query)
        
        for row in cur:
            print(row)
            print('User Id ::',row[0])
            print('User Name ::',row[1])
            print('User Phone ::',row[2])
            print('---------------')
    
    # fetch all data
    def fetch_all(self):
        query = 'select * from user_info'
        cur=self.conn.cursor()
        cur.execute(query)
        for row in cur:
            print(row)
            print('User Id ::',row[0])
            print('User Name ::',row[1])
            print('User Phone ::',row[2])
            print('---------------')
    
    # delete the data
    def delete_data(self,userid):
        query = f"delete from user_info where userid = '{userid}'"
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        print('deleted')

    # updata the data using userId
    def updata_data(self,userid, newName, newEmail,newPhone, newPass):
        query = f"update user_info set username='{newName}', email='{newEmail}' ,phone_number='{newPhone}', password='{newPass}' where userid = '{userid}'"
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        print("updated")