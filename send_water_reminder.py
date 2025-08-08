# -*- coding: utf-8 -*-
from email.message import EmailMessage
import smtplib
import os
from dotenv import load_dotenv

load_dotenv() # 加载 .env 文件中的环境变量

SENDER_EMAIL = os.getenv('SENDER_EMAIL')
AUTH_CODE = os.getenv('AUTH_CODE')
RECEIVER_EMAIL = os.getenv('RECEIVER_EMAIL')
SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = int(os.getenv('SMTP_PORT'))

msg = EmailMessage()
msg['From'] =  SENDER_EMAIL
msg['To'] = RECEIVER_EMAIL
msg['Subject'] = "嘉然提醒谢斌喝水了"
html_content = """
<html>
<body>
    <p>亲爱的谢斌小朋友，</p>
    <p><b>提醒你喝水时间到了！</b></p>
    <p>保持水分充足对身体很重要哦！</p>
    <p>祝你一天愉快！</p>
</body>
</html>
"""
msg.set_content(html_content,subtype='html')

smtp_server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
smtp_server.login(SENDER_EMAIL, AUTH_CODE)
smtp_server.send_message(msg)
smtp_server.quit()
