import email 
import imaplib 
import ctypes 
import getpass
mail = imaplib.IMAP4_SSL('imap.gmail.com',993) 
unm = 'your email' 
pwd= 'your password' 
mail.login(unm,pwd) 
mail.select('INBOX') 
def loop(): 
      mail.select('INBOX') 
      n=0
      (retcode,messages)=mail.search(None,'(ALL)')
      if retcode == 'OK' : 
          for num in messages[0].split():
                n=n+1 
                typ,data= mail.fetch(num,'(RFC822)') 
                raw_email = data[0][1] 
                raw_email_string = raw_email.decode('utf-8') 
                email_message = email.message_from_string(raw_email_string)   
                for respone_part in data: 
                      if isinstance (respone_part,tuple): 
                           original = (email.message_from_string(respone_part[1])) 
                           d1 = original['From'] 
                           print ('\n\n\nFrom : '+d1) 
                           data = original['Subject'] 
                           print ('Subject : '+data) 
                           typ, data = mail.store(num,'+FLAGS','\\Seen') 
                           for part in email_message.walk(): 
                                 if part.get_content_type() == "text/plain": 
                                        body = part.get_payload(decode=True) 
                                        print ("Body :"+body) 
                           f=open("Email content.txt","a") 
                           f.write(d1) 
                           f.write(str(data)) 
                           f.write(body) 
                           f.close() 
if __name__ == '__main__': 
     try:
            while True: 
               loop() 
     finally: 
          print("Thanks for using this service")
