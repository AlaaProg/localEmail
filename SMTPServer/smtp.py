import smtpd, email
from email import policy
from email.parser import BytesParser, Parser
from datetime import datetime # datetime.now().strftime('%Y%m%d%H%M%S')
from Database.models    import User, Email



class SMTP(smtpd.SMTPServer):
    
	def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):

		message = Parser(policy=policy.default).parsestr(data)
		body = message.get_body(preferencelist=('html'))
		
		for rcptto in rcpttos:
			Email.create(subject=message.get('subject'), mailfrom=mailfrom, mailto=rcptto, data=body.get_content())

		return

