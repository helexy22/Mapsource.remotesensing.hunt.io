#-*- coding:utf-8 -*-
'''
Send mail
message is content
Application : script operation monitoring
'''

import os
import sys
import smtplib
from email.mime.text import MIMEText
from email.header import Header

reload(sys)
sys.setdefaultencoding('utf-8')

def SendEmail(form,contentText):
    mail_host = 'smtp.163.com'
    mail_user = '************'  
    mail_pass = '************'  

	#���ͷ���Ϣ
    sender = '************' 
	
	#���ܷ���Ϣ
    receivers = ['************']

    message = MIMEText(form+contentText, 'plain', 'utf-8')
	
    message['Subject'] =form+contentText
    message['From'] = sender
    message['To'] = receivers[0]

    subject = 'Python SMTP �ʼ�����'
    message['Subject'] = Header(subject, 'utf-8')

    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print "�ʼ����ͳɹ�"