import config 
from peewee import SqliteDatabase, Model



db = SqliteDatabase(config.database.dbname)


class BaseModel(Model):
	class Meta:
		database = db



# def create_db:
# def 
# db.connect()

# db.create_tables([Person, Pet])
