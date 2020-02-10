import asyncore
from SMTPServer.smtp import SMTP


class Server():

	def __init__(self, host='127.0.0.1', port=1025):
		self.host_port = (host, port)


	def run(self):	

		try:

			self.server = SMTP(self.host_port, None, decode_data=True, enable_SMTPUTF8=False)
			print(" * Runing Email Server %s:%s"%self.host_port)
			asyncore.loop(timeout=1, use_poll=True)

		except KeyboardInterrupt as e:
			self.server.close()
