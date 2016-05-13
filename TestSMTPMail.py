#! /usr/bin/env python3
# -*- encoding:utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(srcAddr):
        name, addr = parseaddr(srcAddr)
        return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = 'shutao.wang@yooli.com'
password = input('password:')
print('password = ', password)
to_addr = 'test_134@sina.com'
smtp_server = 'smtp.exmail.qq.com'
smtp_port = 25#465 #465 is ssl port

#html
htmlContent = '<html><body><h1>Hello</h1><p>send by <a href="http://www.python.org">Python</a>...</p></body></html>'
msg = MIMEText(htmlContent, 'html','utf-8')
#text
# msg = MIMEText('hello, send by python...', 'plain', 'utf-8')

#with attachment
msg = MIMEMultipart()
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

msg['From'] = _format_addr('Phthon dev <%s>' % from_addr)
msg['To'] = _format_addr('test email <%s>' % to_addr)
msg['Subject'] = Header('test send by python', 'utf-8').encode()

#send with attachment
with open('/home/todd/program/sublime/Icon/48x48/sublime_text.png', 'rb') as f:
        mime = MIMEBase('image', 'png', filename = 'sublime_text.png')
        mime.add_header('Content-Disposition', 'attachment', filename = 'sublime_text.png')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        mime.set_payload(f.read())
        encoders.encode_base64(mime)
        msg.attach(mime)

server = smtplib.SMTP(smtp_server, smtp_port)
# server = smtplib.SMTP_SSL(smtp_server, smtp_port)    #using ssl connection
# server.starttls()#set TLS transport
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
