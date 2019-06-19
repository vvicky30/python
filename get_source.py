#!/usr/bin/python3
                                                                                                                                      
import requests   #behave like a browser
   # now connecting to website
webdata=requests.get("https://www.google.com")
print(webdata) #to get response code of http or https i.e. 200,404,505,302 etc
#now for looking html data
htmldata=webdata.text #to get front end data or source-code
f=open('google_data.txt','w')#for save into the file
f.write(htmldata)                                                                                                                     
f.close()                                                                                                                             
             
