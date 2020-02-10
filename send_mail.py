import smtplib
import email.utils
from email.mime.text import MIMEText

# Create the message
msg = MIMEText('''
	<h1>This is the body of the message.</h1>
''')
msg['To'] = email.utils.formataddr(('Recipient', 'alaa_akiel@local.com'))
msg['From'] = email.utils.formataddr(('Author', 'alaa0akiel@example.com'))
msg['Subject'] = 'First Message'

server = smtplib.SMTP('127.0.0.1', 2025)
#server.set_debuglevel(True) # show communication with the server

try:
    server.sendmail('alaa0akiel@local.com', 'alaa_akiel@local.com', msg.as_string())
finally:
    server.quit()


# from 
# to 
# subject 
# body
# 