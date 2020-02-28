import concurrent.futures as concurrent
import config
from SMTPServer import Server
from Site       import create_app
from Database   import db, models

app = create_app(config.site)
server = Server(config.smtp.host, config.smtp.port)
executor =  concurrent.ProcessPoolExecutor(max_workers=1)


if __name__ == '__main__':

	db.connect()
	models.create_table(db)
	executor.submit(server.run)
	app.run(port=config.site.port, debug=config.site.debug, use_reloader=config.site.debug)
