import email
from gspread.models import Worksheet
import xlrd
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from xlrd import sheet
from sheet2api import Sheet2APIClient

#This is for google spreadsheet
gc = gspread.service_account(filename='[json file that you downloaded from google api console].json')
sh = gc.open_by_key("[uri's key of google spreadsheet]")
Worksheet = sh.sheet1

#Test google spreadsheet
# print(Worksheet.col_count)
# d = Worksheet.get('B1:B2')
# print(Worksheet.get(f'B1:B{Worksheet.row_count}'))
# print(Worksheet.col_values(2))

name = Worksheet.col_values(2)
mail_list = Worksheet.col_values(3)

#This is for Microsft excell >> xlsx file
# path =  "uni.xlsx"
# openFile = xlrd.open_workbook(path)
# sheet = openFile.sheet_by_name('Sheet1')
# mail_list = []
# name = []
# for k in range(sheet.nrows):
#     family_name = sheet.cell_value(k,1)
#     email = sheet.cell_value(k,2)
#     mail_list.append(email) 
#     name.append(family_name)

my_email = ''  
my_password = '' 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(my_email, my_password)

for mail_to in mail_list:
    send_to_email = mail_to
    find_des = mail_list.index(send_to_email) 
    family_nameName = name[find_des] 
    email_text = f""""
Hello Dr.{family_nameName},
I hope you are fine.
I am interested in continuing my education toward a direct Ph.D. and doing research in the field of security combining with AI.

As I reviewed your honorable research works regarding cybersecurity, I found them perfectly close to my research interests. Therefore, I would like to ask you kindly to consider me as a candidate for the direct Ph.D. position working under your supervision for 2022. It would be very kind of you to look at my CV and let me know if there is an opportunity for me to join your research group.

I am a bachelor’s degree graduated of electrical engineering from Iran University of Science and Technology (top 3 university in Iran). I have won the first prize in an international competition, named Huawei ICT Skill, in 2017. I have trained in Huawei HQ and Huawei University in Shenzhen, China. Besides, I was accepted at Padua University (top 200 university in QS ranking) for fall 2020 in MS Cybersecurity, but unfortunately my visa was rejected. Within 3 months participating in classes online, I read my lessons completely such as Machine learning, Information security, Cryptography, and Cognition and computation. Moreover, I have one year of versatile professional work experience in R&D cybersecurity development engineer. In specific, research on event correlation (Elasticsearch) and threat intelligence (User Behavior Analysis), and etc.
Full details of my skills are available in the enclosed CV.
Looking forward to hearing from you.

Best Regards, 
"""
    subject = 'PhD application'
    message = email_text
    msg = MIMEMultipart()
    msg['To'] = send_to_email 
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
    
    filename = "CV - Arastoo Zibaeirad.pdf"  
    with open(filename, "rb") as attachment:
        payload = MIMEBase("application", "octet-stream")
        payload.set_payload(attachment.read())
    encoders.encode_base64(payload)
    payload.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    
    msg.attach(payload)
    text = msg.as_string()
    print(f'Sending email to {family_nameName}... ') 
    server.sendmail(my_email, send_to_email, text)
    time.sleep(120)

server.quit()
print('Process is finished!')
time.sleep(10)