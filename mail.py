import smtplib
import ssl
from email.message import EmailMessage

def mail_sender(name="user",email_receiver="",otp="",operation=""):
    email_sender = 'myapplogin75@gmail.com'
    email_password = 'ztiptcinocbtzjzn'
    subject = 'OTP'
    if operation == 'new':
        body = f"""
        Hello {name}, {otp} is your one time password to create your account \
            please don't share this otp with anyone.
        
        
        For any queries contact:-986575****
        """
    elif operation == "edit":
        body = f"""
        Hello {name}, {otp} is your one time password to change your account password \
            please don't share this otp with anyone.
        
        
        For any queries contact:-986575****
        """
    elif operation == "delete":
        body = f"""
        Hello {name}, Your Account is Deleted Successfully!
        
        
        For any queries contact:-986575****
        """
    
    elif operation == "ticket for admin":
        body = f"""
        Hello admin bro, there is a problem with user :{name}, check out this conversation:{otp}
        
        
        """
        email_receiver = "shashidharreddynalamariedu@gmail.com" # admin mail id
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())