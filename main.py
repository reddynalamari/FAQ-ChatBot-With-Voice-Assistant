import customtkinter as tk
from tkinter import messagebox as mb
import random
from mail import mail_sender as ms
from database import *
import speech_recognition as sr
from texttospeech import ts
recognizer = sr.Recognizer()

root = tk.CTk()
root.config(height=625,width=940)
root.resizable(False,False)
root.title("Batch 14")
font = "Roboto"
back_button = tk.CTkButton(master=root,text="Back",font=(font,15),command=lambda: p.main_frame())
back_button.place(x=600,y=463)
def exit_function():
    temp = mb.askyesno("MyApp","Do you want to exit?")
    if temp:
        root.destroy()


global temp_variable,t
class pingpong:
    def __init__(self) :
        self.temp_variable = 0
        self.temp_variable2 = 0
        self.exist = "user name exist"
        self.notexist = "OK"
        self.temparary = 0
        self.pass_changer_mail = ''
        self.temp_variable_z = 1

    def main_frame(self):
        back_button.configure(state=tk.DISABLED)
        self.frame1 = tk.CTkFrame(master=root,height=445,width=730)
        self.frame1.place(x=10,y=10)
        title_lable = tk.CTkLabel(master=self.frame1,text="Welcome to My App",font=("Segoe Script",50))
        title_lable.place(x=105,y=40)
        # entery 1
        self.entery1_function()
        # entery 2
        self.entery2_function()

        login_button = tk.CTkButton(master=self.frame1,text="login",fg_color="transparent",\
                                    font=(font,17),width=3,hover_color="#6675F0",command=self.login)
        login_button.place(x=325,y=285)

        admin_login_button = tk.CTkButton(master=self.frame1,text="Admin login",fg_color="transparent",\
                                    font=(font,17),width=3,hover_color="#6675F0",command=self.admin_login)
        admin_login_button.place(x=300,y=320)


        signup_label = tk.CTkLabel(master=self.frame1,text="New user?",font=("Roboto",20))
        signup_label.place(x=228,y=380)
        signup_button = tk.CTkButton(master=self.frame1,text="Click here to signup",fg_color="transparent",\
                                     font=("Roboto",17,"bold","underline")\
                                    ,text_color="green",hover_color="#313131", cursor="hand2",command=self.signup_frame)
        signup_button.place(x=325,y=380)

    def entery1_function(self):
        def on_id_enter(e):
            temp = self.entery1.get()
            if temp == 'ID':
                self.entery1.delete(0, 'end')
        def on_id_leave(e):
            temp = self.entery1.get()
            if temp == '':
                self.entery1.insert(0, 'ID')

        self.entery1 = tk.CTkEntry(master=self.frame1,font=(font,15))
        self.entery1.place(x=280,y=180)
        self.entery1.insert(0,"ID")
        self.entery1.bind('<FocusIn>', on_id_enter)
        self.entery1.bind('<FocusOut>', on_id_leave)

    def entery2_function(self):
        def on_id_enter(e):
            temp = self.entery2.get()
            if temp == 'password':
                self.entery2.delete(0, 'end')
        def on_id_leave(e):
            try:
                temp = self.entery2.get()
                if temp == '':
                    self.entery2.insert(0, 'password')
            except:
                pass
        self.entery2 = tk.CTkEntry(master=self.frame1,font=(font,15),show="*")
        self.entery2.place(x=280,y=215)
        self.entery2.insert(0,"password")
        self.entery2.bind('<FocusIn>', on_id_enter)
        self.entery2.bind('<FocusOut>', on_id_leave)
        
        self.pass_button = tk.CTkButton(master=self.frame1,hover_color="#6675F0",text="show",font=(font,15),width=5,\
                                        fg_color="transparent",command=lambda:self.show_hide(self.temp_variable))
        self.pass_button.place(x=423,y=215)

    def show_hide(self,temp_variable):
        if temp_variable == 0:
            self.pass_button.configure(text="hide")
            self.entery2.configure(show="")
            self.temp_variable = 1
        else:
            self.pass_button.configure(text="show")
            self.entery2.configure(show="*")
            self.temp_variable = 0


    def signup_frame(self):
        self.frame1.destroy()
        back_button.configure(state=tk.NORMAL)
        back_button.configure(command=self.main_frame)
        self.frame2 = tk.CTkFrame(master=root,height=445,width=730)
        self.frame2.place(x=10,y=10)
        title_lable = tk.CTkLabel(master=self.frame2,text="Sign Up to create account",font=("Segoe Script",40))
        title_lable.place(x=105,y=30)


        def on_name_enter(e):
            temp = self.suentryname.get()
            if temp == 'Name':
                self.suentryname.delete(0, 'end')
        def on_name_leave(e):
            temp = self.suentryname.get()
            if temp == '':
                self.suentryname.insert(0, 'Name')
        self.suentryname = tk.CTkEntry(master=self.frame2,font=(font,15))
        self.suentryname.place(x=280,y=105)
        self.suentryname.insert(0,"Name")
        self.suentryname.bind('<FocusIn>', on_name_enter)
        self.suentryname.bind('<FocusOut>', on_name_leave)


        def on_email_enter(e):
            temp = self.suentryemail.get()
            if temp == 'Email':
                self.suentryemail.delete(0, 'end')
                self.email_check.configure(text="Check mail id",text_color="red")
            elif "@gmail.com" not in temp:
                self.email_check.configure(text="Check mail id",text_color="red")
            elif ob.mail_fetcher(mailid=temp) == None:
                self.email_check.configure(text=self.notexist,text_color="green") 
            else:
                self.email_check.configure(text="mail id exist",text_color="red")
        def on_email_leave(e):
            temp = self.suentryemail.get()
            if temp == '':
                self.suentryemail.insert(0, 'Email')
                self.email_check.configure(text="Check mail id",text_color="red")
            elif "@gmail.com" not in temp:
                self.email_check.configure(text="Check mail id",text_color="red")
            elif ob.mail_fetcher(mailid=temp) == None:
                self.email_check.configure(text=self.notexist,text_color="green") 
            else:
                self.email_check.configure(text="mail id exist",text_color="red")
        self.suentryemail = tk.CTkEntry(master=self.frame2,font=(font,15))
        self.suentryemail.place(x=280,y=155)
        self.suentryemail.insert(0,"Email")
        self.suentryemail.bind('<FocusIn>', on_email_enter)
        self.suentryemail.bind('<FocusOut>', on_email_leave)

        self.email_check = tk.CTkLabel(master=self.frame2,text='',font=("Roboto",13,"bold"))
        self.email_check.place(x=425,y=155)


        def on_username_enter(e):
            temp = self.suentryusername.get()
            if temp == 'Username':
                self.suentryusername.delete(0, 'end')
                self.username_check.configure(text="Change username",text_color="red")
            elif ob.fetch_password(username=temp) == None:
                self.username_check.configure(text=self.notexist,text_color="green") 
            else:
                self.username_check.configure(text="username exist",text_color="red")
        def on_username_leave(e):
            temp = self.suentryusername.get()
            if temp == '':
                self.suentryusername.insert(0, 'Username')
                self.username_check.configure(text="Change username",text_color="red")
            elif ob.fetch_password(username=temp) == None:
                self.username_check.configure(text=self.notexist,text_color="green") 
            else:
                self.username_check.configure(text="username exist",text_color="red") 
        self.suentryusername = tk.CTkEntry(master=self.frame2,font=(font,15))
        self.suentryusername.place(x=280,y=205)
        self.suentryusername.insert(0,"Username")
        self.suentryusername.bind('<FocusIn>', on_username_enter)
        self.suentryusername.bind('<FocusOut>', on_username_leave)


        self.username_check = tk.CTkLabel(master=self.frame2,text='',font=("Roboto",13,"bold"))
        self.username_check.place(x=425,y=205)


        def on_pass1_enter(e):
            temp = self.suentrypass1.get()
            if temp == 'Password':
                self.suentrypass1.delete(0, 'end')
        def on_pass1_leave(e):
            temp = self.suentrypass1.get()
            if temp == '':
                self.suentrypass1.insert(0, 'Password')
        self.suentrypass1 = tk.CTkEntry(master=self.frame2,font=(font,15),show="*")
        self.suentrypass1.place(x=280,y=255)
        self.suentrypass1.insert(0,"Password")
        self.suentrypass1.bind('<FocusIn>', on_pass1_enter)
        self.suentrypass1.bind('<FocusOut>', on_pass1_leave)
        self.pass_button2 = tk.CTkButton(master=self.frame2,hover_color="#6675F0",text="show",font=(font,15),width=5,\
                                        fg_color="transparent",command=lambda:self.show_hidesu(self.temp_variable2))
        self.pass_button2.place(x=423,y=255)


        signup_button = tk.CTkButton(master=self.frame2,text="Sign up",fg_color="transparent",\
                                     font=("Roboto",17,"bold"),width=5\
                                    ,hover_color="#6675F0", cursor="hand2",command=self.signup)
        signup_button.place(x=300,y=325)

    def show_hidesu(self,temp_variable2):
        if temp_variable2 == 0:
            self.pass_button2.configure(text="hide")
            self.suentrypass1.configure(show="")
            self.temp_variable2 = 1
        else:
            self.pass_button2.configure(text="show")
            self.suentrypass1.configure(show="*")
            self.temp_variable2 = 0


    def signup(self):
        self.suusername = self.suentryusername.get()
        self.suname = self.suentryname.get()
        self.sumail = self.suentryemail.get()
        self.supassword = self.suentrypass1.get()
        if ob.fetch_password(username=self.suusername) == None:
            if ob.mail_fetcher(mailid=self.sumail) == None:
                self.otp_page()
            else:
                mb.showerror("MyApp","Mailid alredy Exist")
        else:
            mb.showerror("MyApp","Username alredy Exist")

    def otp_page(self):
        
        self.randomnumber = random.randint(100000,999999)
        pass
        #print(self.randomnumber)
        try:
            ms(name=self.suname,email_receiver=self.sumail,otp=self.randomnumber,operation="new")
        except Exception as e:
            if "is not a valid" in str(e):
                mb.showerror("MyApp","No Mail id found")
                self.suentryemail.delete(0,"end")
            else:
                mb.showerror("MyApp","No internet, can't send OTP")
                self.main_frame()
                self.frame2.destroy()
        else:
            self.frame2.destroy()
            back_button.configure(state=tk.NORMAL)
            back_button.configure(command=self.signup_frame)
            self.frame3 = tk.CTkFrame(master=root,height=445,width=730)
            self.frame3.place(x=10,y=10)
            title_lable = tk.CTkLabel(master=self.frame3,text="Enter Your Otp",font=("Segoe Script",40))
            title_lable.place(x=180,y=100)
            def on_otp_enter(e):
                temp = self.otpentery.get()
                if temp == 'OTP':
                    self.otpentery.delete(0, 'end')
            def on_otp_leave(e):
                temp = self.otpentery.get()
                if temp == '':
                    self.otpentery.insert(0, 'OTP')
            self.otpentery = tk.CTkEntry(master=self.frame3,font=(font,15))
            self.otpentery.place(x=225,y=220)
            self.otpentery.insert(0,"OTP")
            self.otpentery.bind('<FocusIn>', on_otp_enter)
            self.otpentery.bind('<FocusOut>', on_otp_leave)
            self.submitbutton = tk.CTkButton(master=self.frame3,text="Submit",fg_color="transparent",\
                                        font=("Roboto",17,"bold"),width=5\
                                        ,hover_color="#6675F0", cursor="hand2",command=self.data_entery)
            self.submitbutton.place(x=400,y=220)
        
        
    def data_entery(self):
        try:
            if int(self.otpentery.get()) == self.randomnumber:
                ob.insert_data(u_name=self.suusername,name=self.suname,mailid=self.sumail,password=self.supassword)
                mb.showinfo("MyApp","Account created successfully!")
                self.frame3.destroy()
                self.main_frame()
            else:
                raise ValueError
        except:
            mb.showerror("MyApp","Wrong OTP")

    def admin_login(self):
        u_id = self.entery1.get()
        password = self.entery2.get()
        if (u_id == "ID" and password == "password"):
            self.admin_main_page()
        else:
            mb.showerror("MyApp","Login Unsuccess")

    def admin_main_page(self):
        self.frame1.destroy()
        back_button.configure(state=tk.NORMAL)
        back_button.configure(command=self.main_frame)
        self.admin_frame1 = tk.CTkFrame(master=root,height=445,width=730)
        self.admin_frame1.place(x=10,y=10)
        title_lable = tk.CTkLabel(master=self.admin_frame1,text="Admin",font=("Segoe Script",40))
        title_lable.place(x=305,y=30)
        self.show_user_button = tk.CTkButton(master=self.admin_frame1,text="Users List",font=(font,20),command=self.users_list)
        self.show_user_button.place(x=300,y=153)
        self.add_faq_button = tk.CTkButton(master=self.admin_frame1,text="Add FAQ",font=(font,20),command= self.add_faq)
        self.add_faq_button.place(x=300,y=203)
        self.show_faq_button = tk.CTkButton(master=self.admin_frame1,text="FAQ List",font=(font,20),command=self.faq_list)
        self.show_faq_button.place(x=300,y=253)
        self.new_faq_button = tk.CTkButton(master=self.admin_frame1,text="New FAQ List",font=(font,20),command=self.new_faq_list)
        self.new_faq_button.place(x=300,y=303)
        self.tickets_button = tk.CTkButton(master=self.admin_frame1,text="Tickets",font=(font,20),command=self.tickets_list)
        self.tickets_button.place(x=500,y=303)
        self.admin_logout_button = tk.CTkButton(master=self.admin_frame1,text="LogOut",fg_color="red",font=(font,20),command=lambda: p.main_frame())
        self.admin_logout_button.place(x=300,y=353)

    def users_list(self):
        self.admin_frame1.destroy()
        back_button.configure(command=self.admin_main_page)
        self.admin_frame2 = tk.CTkFrame(master=root,height=445,width=730)
        self.admin_frame2.place(x=10,y=10)
        title_lable = tk.CTkLabel(master=self.admin_frame2,text="Users",font=("Segoe Script",40))
        title_lable.place(x=305,y=30)
        from tkinter import ttk
        table = ttk.Treeview(self.admin_frame2, columns= ("username","name","mail","password","count"), show="headings")
        table.heading("username", text="Username")
        table.heading("name", text="Name")
        table.heading("mail", text="Mail ID")
        table.heading("password", text="Password")
        table.heading("count", text="Count          ")
        table.place(x=0,y=200)
        data = ob.fetch_all_data()
        for i in range(len(data)):
            table.insert(parent="", index=0, values=data[i])
        def item_select(_):
            for i in table.selection():
                pass
                #print(table.item(i)["values"])
        def delete_item(_):
            for i in table.selection():
                try:
                    u = table.item(i)["values"]
                    ob.delete_account(u[0])
                    ms(name=u[1],email_receiver=u[2],operation="delete")
                    table.delete(i)
                except:
                    mb.showerror("MyApp","This user had an active ticket, you cant remove their account without resolving the issue")
        table.bind('<<TreeviewSelect>>', item_select)
        table.bind("<Delete>",delete_item)

    def tickets_list(self):
        self.admin_frame1.destroy()
        back_button.configure(command=self.admin_main_page)
        self.admin_frame6 = tk.CTkFrame(master=root,height=445,width=730)
        self.admin_frame6.place(x=10,y=10)
        title_lable = tk.CTkLabel(master=self.admin_frame6,text="Users",font=("Segoe Script",40))
        title_lable.place(x=305,y=30)
        from tkinter import ttk
        table = ttk.Treeview(self.admin_frame6, columns= ("username"), show="headings")
        table.heading("username", text="Usernames")
        table.place(x=20,y=240)
        data = ob.fetch_all_ticket()
        self.conversation_area = tk.CTkTextbox(master=self.admin_frame6,width=510)
        self.conversation_area.place(x=210, y=180)
        self.conversation_area.configure(state="disable")
        self.conversationForDeleting = None
        global mail
        mail = tk.CTkEntry(master=self.admin_frame6,font=(font,15), width=350)
        mail.place(x=280,y=130)
        mail.configure(state="disable")
        def solved():
            global mail
            if mb.askyesno("MyApp","Are you sure you want to close this ticket?"):
                ob.delete_ticket(conversation=self.conversationForDeleting)
                table.delete(table.selection()[0])
                mail.delete(0,"end")
                self.conversation_area.delete("1.0", "end")
                mb.showinfo("MyApp","Ticket Closed")
        tk.CTkButton(master=self.admin_frame6,text="Close Ticket",font=(font,17),width=3,command=solved).place(x=301,y=400)
        for i in range(len(data)):
            table.insert(parent="", index=0, values=data[i])
        def item_select(_):
            if len(table.selection()) == 1:
                x = table.item(table.selection()[0])["values"]
                pass
                #print(x)
                self.conversationForDeleting = x[1]
                self.conversation_area.configure(state="normal")
                mail.configure(state="normal")
                mail.delete(0,"end")
                self.conversation_area.delete("1.0", "end")
                self.conversation_area.insert("1.0", x[1][1:])
                self.conversation_area.configure(state="disable")
                mail.insert(0,x[2])
                mail.configure(state="disable")
            elif len(table.selection()) == 0:
                pass
            else:
                mb.showwarning("MyApp","Please select only one item")
        table.bind('<<TreeviewSelect>>', item_select)
    
    def faq_list(self):
        self.admin_frame1.destroy()
        back_button.configure(command=self.admin_main_page)
        self.admin_frame3 = tk.CTkFrame(master=root,height=445,width=730)
        self.admin_frame3.place(x=10,y=10)
        title_lable = tk.CTkLabel(master=self.admin_frame3,text="Users",font=("Segoe Script",40))
        title_lable.place(x=305,y=30)
        from tkinter import ttk
        table = ttk.Treeview(self.admin_frame3, columns= ("questions","answers","count"), show="headings")
        table.heading("questions", text="Questions")
        table.heading("answers", text="Answers")
        table.heading("count", text="Count")
        table.place(x=155,y=200)
        data = ob.fetch_all_faqs()
        for i in range(len(data)):
            table.insert(parent="", index=0, values=data[i])
        def item_select(_):
            for i in table.selection():
                pass
                #print(table.item(i)["values"])
        def delete_item(_):
            for i in table.selection():
                u = table.item(i)["values"]
                ob.delete_faq(u[0])
                table.delete(i)
        table.bind('<<TreeviewSelect>>', item_select)
        table.bind("<Delete>",delete_item)

    def new_faq_list(self):
        self.admin_frame1.destroy()
        back_button.configure(command=self.admin_main_page)
        self.admin_frame5 = tk.CTkFrame(master=root,height=445,width=730)
        self.admin_frame5.place(x=10,y=10)
        title_lable = tk.CTkLabel(master=self.admin_frame5,text="Users",font=("Segoe Script",40))
        title_lable.place(x=305,y=30)
        q = tk.CTkEntry(master=self.admin_frame5,font=(font,15), width=450)
        q.place(x=150,y=310)
        def on_id_enter(e):
            temp = self.answer_entery_new_faq.get()
            if temp == 'Answer':
                self.answer_entery_new_faq.delete(0, 'end')
        def on_id_leave(e):
            temp = self.answer_entery_new_faq.get()
            if temp == '':
                self.answer_entery_new_faq.insert(0, 'Answer')

        self.answer_entery_new_faq = tk.CTkEntry(master=self.admin_frame5,font=(font,15), width=450)
        self.answer_entery_new_faq.place(x=150,y=350)
        self.answer_entery_new_faq.insert(0,"Answer")
        self.answer_entery_new_faq.bind('<FocusIn>', on_id_enter)
        self.answer_entery_new_faq.bind('<FocusOut>', on_id_leave)
        def submit_new_faq():
            ans = self.answer_entery_new_faq.get()
            if ans == "":
                mb.showwarning("MyApp","Please enter answer")
                return
            if ans == "Answer":
                temp = mb.askyesno("MyApp","are you sure your answer is 'Answer'?")
                if temp:
                    return
            qes = q.get()
            ob.add_faq(qes,ans)
            mb.showinfo("MyApp","FAQ Added!")
            try:
                ob.delete_undefined_faq(qes)
            except:
                pass
            table.delete(table.selection()[0])   
            q.delete(0,"end")
            self.answer_entery_new_faq.delete(0,"end")
            self.answer_entery_new_faq.insert(0,"Answer")
        submit_button = tk.CTkButton(master=self.admin_frame5,text="Submit",\
                                    font=(font,17),width=3,command=submit_new_faq)
        submit_button.place(x=325,y=400)
        from tkinter import ttk
        table = ttk.Treeview(self.admin_frame5, columns= ("questions","count"), show="headings")
        table.heading("questions", text="Questions")
        table.heading("count", text="Count")
        table.place(x=255,y=150)
        data = ob.fetch_all_new_faqs()
        for i in range(len(data)):
            table.insert(parent="", index=0, values=data[i])
        def item_select(_):
            if len(table.selection()) == 1:
                x = table.item(table.selection()[0])["values"]
                pass
                #print(x)
                q.delete(0,"end")
                q.insert(0,x[0])
            elif len(table.selection()) == 0:
                pass
            else:
                mb.showwarning("MyApp","Please select only one item")
        def delete_item(_):
            for i in table.selection():
                u = table.item(i)["values"]
                ob.delete_undefined_faq(u[0])
                table.delete(i)
        table.bind('<<TreeviewSelect>>', item_select)
        table.bind("<Delete>",delete_item)

    def add_faq(self):
        self.admin_frame1.destroy()
        back_button.configure(command=self.admin_main_page)
        self.admin_frame4 = tk.CTkFrame(master=root,height=445,width=730)
        self.admin_frame4.place(x=10,y=10)
        title_lable = tk.CTkLabel(master=self.admin_frame4,text="ADD FAQ",font=("Segoe Script",40))
        title_lable.place(x=275,y=30)

        def on_id_enter1(e):
            temp = self.question_entery.get()
            if temp == 'Question':
                self.question_entery.delete(0, 'end')
        def on_id_leave1(e):
            temp = self.question_entery.get()
            if temp == '':
                self.question_entery.insert(0, 'Question')

        self.question_entery = tk.CTkEntry(master=self.admin_frame4,font=(font,15), width=450)
        self.question_entery.place(x=150,y=180)
        self.question_entery.insert(0,"Question")
        self.question_entery.bind('<FocusIn>', on_id_enter1)
        self.question_entery.bind('<FocusOut>', on_id_leave1)


        def on_id_enter(e):
            temp = self.answer_entery.get()
            if temp == 'Answer':
                self.answer_entery.delete(0, 'end')
        def on_id_leave(e):
            temp = self.answer_entery.get()
            if temp == '':
                self.answer_entery.insert(0, 'Answer')

        self.answer_entery = tk.CTkEntry(master=self.admin_frame4,font=(font,15), width=450)
        self.answer_entery.place(x=150,y=230)
        self.answer_entery.insert(0,"Answer")
        self.answer_entery.bind('<FocusIn>', on_id_enter)
        self.answer_entery.bind('<FocusOut>', on_id_leave)
        submit_button = tk.CTkButton(master=self.admin_frame4,text="Submit",\
                                    font=(font,17),width=3,command=self.submit_question)
        submit_button.place(x=325,y=285)

    def submit_question(self):
        q = self.question_entery.get()
        a = self.answer_entery.get()
        ob.add_faq(q,a)
        mb.showinfo("MyApp","FAQ Added!")

    def login(self):
        self.u_id = self.entery1.get()
        password = self.entery2.get()
        if ob.fetch_password(username=self.u_id) == None:
            mb.showerror("MyApp","No User found")
            self.entery1.delete(0,"end")
        elif ob.fetch_password(username=self.u_id) != password:
            mb.showerror("MyApp","Wrong password")
            self.entery2.delete(0,"end")
            forgot_button = tk.CTkButton(master=self.frame1,text="forgot password",fg_color="transparent",\
                                     font=("Roboto",15,"bold")\
                                    ,text_color="#F94822",hover_color="#313131", cursor="hand2",command=lambda:self.forgot_pass(1))
            forgot_button.place(x=280,y=250)
        else: 
            self.user_login()

    def user_login(self):
        try:
            self.frame1.destroy()
        except:
            self.frame6.destroy()
        back_button.configure(state=tk.NORMAL)
        back_button.configure(command=self.main_frame)
        self.frame5 = tk.CTkFrame(master=root,height=445,width=730)
        self.frame5.place(x=10,y=10)
        title_lable = tk.CTkLabel(master=self.frame5,text="Chat Bot",font=("Segoe Script",40))
        title_lable.place(x=255,y=30)
        self.interact_bot = tk.CTkButton(master=self.frame5,text="Interact",font=(font,20),command=self.chat_bot)
        self.interact_bot.place(x=285,y=173)
        self.user_logout = tk.CTkButton(master=self.frame5,text="LogOut",fg_color="red",font=(font,20),command=lambda: p.main_frame())
        self.user_logout.place(x=285,y=253)

    def st(self):
        global text
        self.flag = True
        if self.question.get() != "":
            self.question.delete(0,'end')
        with sr.Microphone() as source:
            pass
            #print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            try:
                text = recognizer.recognize_google(audio) # API
                return text
            except sr.UnknownValueError:
                self.flag = False
                mb.showerror("hello","Could not understand the audio, please speak clearly")
            except sr.RequestError:
                self.flag = False
                mb.showerror("hello","Could not request results, please connect to fast internet connection or type the question")
                self.question.delete(0,"end")
                self.submit_button.configure(command=lambda: self.texting_button())


    def texting_button(self):
        global text
        text = self.question.get()
        self.real_question = text
        self.answer = ob.fetch_answer(text)
        if self.answer == None:
            self.answer = "Unknown question, please contact to customer service"
            ob.undefined_question(text)
        ob.count_incriment(op="user",feild=self.u_id)
        pass
        #print(self.answer)
        self.flag = True
        if self.flag:
            ts(self.answer)
            self.text_area.configure(state="normal")
            self.text_area.insert(tk.END, f"\nUser :       {self.real_question}")
            self.text_area.insert(tk.END, f"\nChatBot : {self.answer}")
            self.text_area.configure(state="disabled")
        self.submit_button.configure(command=self.listen)


    def chat_bot(self):
        self.frame5.destroy()
        back_button.configure(command=self.user_login)
        self.frame6 = tk.CTkFrame(master=root,height=445,width=730)
        self.frame6.place(x=10,y=10)
        title_lable = tk.CTkLabel(master=self.frame6,text="Chat Bot",font=("Segoe Script",40))
        title_lable.place(x=255,y=30)
        global text
        self.submit_button = tk.CTkButton(master=self.frame6,text="Start",\
                                    font=(font,17),width=3,command=self.listen)
        self.submit_button.place(x=335,y=150)
        self.question = tk.CTkEntry(master=self.frame6,font=(font,15), width=450)
        self.question.place(x=150,y=100)
        self.text_area = tk.CTkTextbox(master=self.frame6,width=710)
        self.text_area.place(x=10, y=190)
        self.report_button = tk.CTkButton(master=self.frame6,text="Report",fg_color="red",font=(font,17),width=3,command=self.ticket)
        self.report_button.place(x=325,y=400)
        self.text_area.configure(state="disabled")

    def ticket(self):
        all_text = self.text_area.get("1.0", "end")
        ob.add_ticket(self.u_id, all_text)
        mb.showinfo("MyApp","Your ticket has been raised, someone will contact you soon, buee buee")
        try:
            ms(name=self.u_id, otp=all_text, operation="ticket for admin")
        except:
            mb.showerror("MyApp","No internet connection, we can't send mail to you")
        self.frame6.destroy()
        self.main_frame()

    def listen(self):
        global text
        text = self.st()
        self.real_question = text
        try:
            self.question.insert(0, text)
        except:
            pass
        self.answer = ob.fetch_answer(text)
        if self.answer == None:
            self.answer = "Unknown question, please contact to customer service"
            ob.undefined_question(text)
        ob.count_incriment(op="user",feild=self.u_id)
        pass
        #print(self.answer)
        if self.flag:
            ts(self.answer)
            self.text_area.configure(state="normal")
            self.text_area.insert(tk.END, f"\nUser :       {self.real_question}")
            self.text_area.insert(tk.END, f"\nChatBot : {self.answer}")
            self.text_area.configure(state="disabled")


    def forgot_pass(self,a):
        self.a = a
        self.frame1.destroy()
        back_button.configure(state=tk.NORMAL)
        back_button.configure(command=self.main_frame)
        self.frame4 = tk.CTkFrame(master=root,height=445,width=730)
        self.frame4.place(x=10,y=10)
        title_lable = tk.CTkLabel(master=self.frame4,text="Change password",font=("Segoe Script",40))
        title_lable.place(x=175,y=30)
        def on_email_enter(e):
            temp = self.forgetemail.get()
            if temp == 'Email':
                self.forgetemail.delete(0, 'end')
        def on_email_leave(e):
            temp = self.forgetemail.get()
            if temp == '':
                self.forgetemail.insert(0, 'Email')
        self.forgetemail = tk.CTkEntry(master=self.frame4,font=(font,15))
        self.forgetemail.place(x=280,y=155)
        self.forgetemail.insert(0,"Email")
        self.forgetemail.bind('<FocusIn>', on_email_enter)
        self.forgetemail.bind('<FocusOut>', on_email_leave)
        self.otp_button = tk.CTkButton(master=self.frame4,text="Get otp",fg_color="transparent",\
                                        font=("Roboto",17,"bold"),width=5\
                                        ,hover_color="#6675F0", cursor="hand2",command=self.password_canger)
        self.otp_button.place(x=305,y=220)


    
    def password_canger(self):
        self.pass_changer_mail = self.forgetemail.get()
        try:
            self.forgot_pass1.destroy()
            self.forgot_pass2.destroy()
            self.show_hide_forgotpass.destroy()
            self.changebutton.destroy()
        except:
            pass

        if ob.mail_fetcher(mailid=self.pass_changer_mail) == None:
            mb.showerror("MyApp","Mail not found")
        else:
            if self.a:
                self.randomnumber2 = random.randint(100000,999999)
                pass
                #print(self.randomnumber2)
                try:
                    ms(email_receiver=self.pass_changer_mail,otp=self.randomnumber2,operation="edit")
                except Exception as e:
                    if "is not a valid" in str(e):
                        mb.showerror("MyApp","No Mail id found")
                        self.forgetemail.delete(0,"end")
                    else:
                        mb.showerror("MyApp","No internet, can't send OTP")
                else:
                    back_button.configure(command=lambda:self.forgot_pass(0))
                    self.forgetemail.configure(state="readonly")
                    self.otp_button.destroy()
                    def on_otp_enter(e):
                        temp = self.forgot_otp_entery.get()
                        if temp == 'OTP':
                            self.forgot_otp_entery.delete(0, 'end')
                    def on_otp_leave(e):
                        temp = self.forgot_otp_entery.get()
                        if temp == '':
                            self.forgot_otp_entery.insert(0, 'OTP')
                    self.forgot_otp_entery = tk.CTkEntry(master=self.frame4,font=(font,15))
                    self.forgot_otp_entery.place(x=280,y=205)
                    self.forgot_otp_entery.insert(0,"OTP")
                    self.forgot_otp_entery.bind('<FocusIn>', on_otp_enter)
                    self.forgot_otp_entery.bind('<FocusOut>', on_otp_leave)
                    self.submitbutton = tk.CTkButton(master=self.frame4,text="Submit",fg_color="transparent",\
                                                    font=("Roboto",17,"bold"),width=5\
                                                    ,hover_color="#6675F0", cursor="hand2",command=self.data_entery_forgot)
                    self.submitbutton.place(x=310,y=255)

    
    def data_entery_forgot(self):
        temp = self.forgot_otp_entery.get()
        if temp != str(self.randomnumber2):
            mb.showerror("MyApp","Wrong OTP")
        else:
            back_button.configure(command=self.password_canger)
            self.forgot_otp_entery.configure(state="readonly")
            self.submitbutton.destroy()



            def on_newpass_enter(e):
                    temp = self.forgot_pass1.get()
                    if temp == 'New password':
                        self.forgot_pass1.delete(0, 'end')
            def on_newpass_leave(e):
                    temp = self.forgot_pass1.get()
                    if temp == '':
                        self.forgot_pass1.insert(0, 'New password')

            self.forgot_pass1 = tk.CTkEntry(master=self.frame4,font=(font,15))
            self.forgot_pass1.place(x=180,y=255)
            self.forgot_pass1.insert(0,"New password")
            self.forgot_pass1.bind('<FocusIn>', on_newpass_enter)
            self.forgot_pass1.bind('<FocusOut>', on_newpass_leave)


            def on_newpass2_enter(e):
                    temp = self.forgot_pass2.get()
                    if temp == 'Re-enter password':
                        self.forgot_pass2.delete(0, 'end')
            def on_newpass2_leave(e):
                    temp = self.forgot_pass2.get()
                    if temp == '':
                        self.forgot_pass2.insert(0, 'Re-enter password')
            self.forgot_pass2 = tk.CTkEntry(master=self.frame4,font=(font,15))
            self.forgot_pass2.place(x=380,y=255)
            self.forgot_pass2.insert(0,"Re-enter password")
            self.forgot_pass2.bind('<FocusIn>', on_newpass2_enter)
            self.forgot_pass2.bind('<FocusOut>', on_newpass2_leave)
            self.show_hide_forgotpass = tk.CTkButton(master=self.frame4,hover_color="#6675F0",text="hide",font=(font,15),width=5,\
                                        fg_color="transparent",command=lambda:self.show_hide_forgotpassfun(self.temp_variable_z))
            self.show_hide_forgotpass.place(x=530,y=255)
            self.changebutton = tk.CTkButton(master=self.frame4,text="Change",fg_color="transparent",\
                                                font=("Roboto",17,"bold"),width=5\
                                                ,hover_color="#6675F0", cursor="hand2",\
                                                command=lambda:self.password_canger_final())
            self.changebutton.place(x=310,y=305)



    def show_hide_forgotpassfun(self,temp_variable):
                if temp_variable == 0:
                    self.show_hide_forgotpass.configure(text="hide")
                    self.forgot_pass1.configure(show="")
                    self.forgot_pass2.configure(show="")
                    self.temp_variable_z = 1
                else:
                    self.show_hide_forgotpass.configure(text="show")
                    self.forgot_pass1.configure(show="*")
                    self.forgot_pass2.configure(show="*")
                    self.temp_variable_z = 0

    def password_canger_final(self):
        new_password = self.forgot_pass1.get()
        re_enter_pass = self.forgot_pass2.get()
        if new_password == re_enter_pass:
            ob.change_password(newpassword=new_password,mailid=self.pass_changer_mail)
            mb.showinfo("MyApp","Password changed!!")
            self.frame4.destroy()
            self.main_frame()
        else:
            mb.showerror("MyApp","Password is not matched")


p = pingpong()
exit_button = tk.CTkButton(master=root,text="Exit",fg_color="red",font=(font,15),command=lambda: exit_function())
exit_button.place(x=295,y=463)
home_button = tk.CTkButton(master=root,text="Home",font=(font,15),command=lambda: p.main_frame())
home_button.place(x=10,y=463)
p.main_frame()
root.mainloop()
