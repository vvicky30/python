import smtplib
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart 
from email.mime.base import MIMEBase 
from email import encoders 

#user info sender to receiver 
email_user = 'enter sender email' 
email_password = 'enter sender password' 
email_send = 'enter receiver email' 
subject = 'Email test' 

#message format 
msg = MIMEMultipart() 
msg['From'] = email_user 
msg['To'] = email_send 
msg['Subject'] = subject 
body = 'Here this is vedant bhatt... winter is coming' 
msg.attach(MIMEText(body,'plain')) 

#attachment of file 
filename='dock.txt' 
attachment =open(filename,'rb') 
part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read()) 
encoders.encode_base64(part) 
part.add_header('Content-Disposition',"attachment; filename= "+filename) 
msg.attach(part) 
#converting msg as string type 
text=msg.as_string() 

#protocols to send over smtp 
server = smtplib.SMTP('smtp.gmail.com',587) 
server.starttls()
server.login(email_user,email_password) 
server.sendmail(email_user,email_send,text) 
server.quit()
