import mysql.connector as connector


class DBHelper():
    def __init__(self):
        self.con = connector.connect(
            host='localhost', port='3306', user='root', password='0809', database='faq_chatbot',
            auth_plugin='mysql_native_password')
        query = 'create table if not exists user(username varchar(50) primary key,name varchar(50),\
              mailid varchar(100) NOT NULL, \
                password varchar(100) NOT NULL,count int,UNIQUE(mailid));\
                    create table if not exists undefined(questions varchar(300) unique, count int);\
                        CREATE TABLE IF NOT EXISTS faq (questions VARCHAR(300) NOT NULL,answers VARCHAR(300) NOT NULL,count INT DEFAULT 0,FULLTEXT (questions));\
                            CREATE TABLE IF NOT EXISTS tickets (conversation TEXT NOT NULL,username VARCHAR(255),FOREIGN KEY (username) REFERENCES user(username));'
        cur = self.con.cursor()
        cur.execute(query,multi=True)
        self.con.commit()


    # inserting
    def insert_data(self, u_name,name,mailid, password):

        query = "insert into user(username,name,mailid,password,count)" \
                "values('{}','{}','{}','{}',0)".format(u_name,name,mailid, password)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()

    # Fetch values
    def fetch_password(self, username):
        query = f"select password from user where username = '{username}'"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
                return row[0]
    def mail_fetcher(self,mailid):
         query = f"select username from user where mailid = '{mailid}'"
         cur = self.con.cursor()
         cur.execute(query)
         for row in cur:
                return row[0]
    # delete
    def delete_account(self, username):
        query = "delete from user where username='{}'".format(username)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()

    # update
    def change_password(self,newpassword,mailid):
        query = f"update user set password='{newpassword}' where mailid = '{mailid}'"
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()

    def fetch_all_data(self):
         query = f"select * from user"
         cur = self.con.cursor()
         cur.execute(query)
         data = []
         for row in cur:
            data.append(row)
         return data
    
    def add_faq(self, question, answer):
        query = f"insert into faq(questions, answers, count)" \
                "values('{}','{}',0)".format(question, answer)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()

    def fetch_all_faqs(self):
         query = f"select * from faq"
         cur = self.con.cursor()
         cur.execute(query)
         data = []
         for row in cur:
            data.append(row)
         return data

    def fetch_all_new_faqs(self):
         query = f"select * from undefined"
         cur = self.con.cursor()
         cur.execute(query)
         data = []
         for row in cur:
            data.append(row)
         return data     
    
    def delete_faq(self, question):
        query = "delete from faq where questions='{}'".format(question)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()

    def fetch_questions(self):
         query = f"select questions from faq"
         cur = self.con.cursor()
         cur.execute(query)
         data = []
         for row in cur:
            data.append(row[0])
         return data

    def fetch_answer(self, question):
        x = f'SELECT answers, MATCH(questions) AGAINST("{question}" IN NATURAL LANGUAGE MODE) AS relevance \
            FROM faq \
                WHERE MATCH(questions) AGAINST("{question}" IN NATURAL LANGUAGE MODE) \
                    ORDER BY relevance DESC \
                        LIMIT 1;'
        cur = self.con.cursor()
        cur.execute(x)
        for row in cur:
                self.count_incriment("faq",row[0])
                return row[0]

    def fetch_count(self,op,feild):
         query = ""
         if op=="faq":
              query = f'select count from faq where answers = "{feild}"'
         else:
              query = f'select count from user where username = "{feild}"'
         cur = self.con.cursor()
         cur.execute(query)
         for row in cur:
                return row[0]
         
    def count_incriment(self, op, feild):
         c = self.fetch_count(op,feild)
         c+=1
         if op == "faq":
            query = f'update faq set count= "{c}" where answers = "{feild}"'
         elif op == "user":
              query = f"update user set count='{c}' where username = '{feild}'"
         cur = self.con.cursor()
         cur.execute(query)
         self.con.commit()

    def undefined_question(self, question):
         query = f'INSERT INTO undefined (questions, count) VALUES \
            ("{question}", 1) ON DUPLICATE KEY UPDATE count = count + 1'

         cur = self.con.cursor()
         cur.execute(query)
         self.con.commit()
    
    def delete_undefined_faq(self, question):
        query = "delete from undefined where questions='{}'".format(question)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()

    def add_ticket(self, username, conversation):
         query = f'INSERT INTO tickets values("{conversation}", "{username}")'
         cur = self.con.cursor()
         cur.execute(query)
         self.con.commit()

    def fetch_all_ticket(self):
         query = f'SELECT tickets.username, tickets.conversation, user.mailid FROM tickets JOIN user ON tickets.username = user.username;'
         cur = self.con.cursor()
         cur.execute(query)
         data = []
         for row in cur:
            data.append(row)
         return data 
    
    def delete_ticket(self,conversation):
         query = "delete from tickets where conversation ='{}'".format(conversation)
         cur = self.con.cursor()
         cur.execute(query)
         self.con.commit()

ob = DBHelper()