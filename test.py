import smtplib
from email.mime.text import MIMEText



smtpserver = "smtp.163.com"
port = 0
sender = "chukun3@163.com"
psw = 'chu123456789'
receiver = "249836495@qq.com"

subject = "这是个主题163"
body = '<p>这是个163邮件呢</p>'
msg = MIMEText(body, 'html', 'utf-8')
msg['from'] = sender
msg['to'] = receiver
msg['subject'] = subject


smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(sender, psw)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()