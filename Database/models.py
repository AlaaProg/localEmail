from datetime import datetime
from peewee   import CharField, DateTimeField, TextField, ManyToManyField, ForeignKeyField
from Database import BaseModel 



class Email(BaseModel):
	subject    = CharField()
	mailfrom   = CharField()
	mailto     = CharField()
	data       = TextField()
	created_at = DateTimeField(default=datetime.now)


class User(BaseModel):
	username  = CharField(unique=True)
	fullname  = CharField()
	password  = CharField()
	created_at = DateTimeField(default=datetime.now)


class Relationship(BaseModel):
	from_user = ForeignKeyField(User, backref='relationships')
	to_user = ForeignKeyField(User, backref='related_to')
	
	class Meta:
		indexes = (
			(('from_user', 'to_user'), True),
		)

class Message(BaseModel):
	user = ForeignKeyField(User, backref='messages')
	content    = TextField()
	created_at = DateTimeField(default=datetime.now)


def create_table(db):
	db.create_tables([
		User, Relationship, Message, Email
	])
