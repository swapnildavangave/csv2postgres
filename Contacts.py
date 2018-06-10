from sqlalchemy 					import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm 				import relationship, backref
from sqlalchemy.ext.declarative 	import declarative_base
from sqlalchemy.orm 				import validates
from sqlalchemy 					import create_engine
from sqlalchemy.orm 				import sessionmaker
import os.path
import json

Base = declarative_base()

class Group(Base):
	__tablename__ 	= 'group'
	id 				= Column(Integer(), primary_key=True)
	_name 			= Column(String(), default="General")

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		self._name = name

class Contact(Base):
	__tablename__ 	= 'contact'
	id 				= Column(Integer(), primary_key=True)
	_name 			= Column(String())
	_number 		= Column(Integer(), unique=True)
	_email 			= Column(String())

	@validates('email')
	def validate_email(self, key, address):
		assert '@' in address
		return address

	@property
	def email(self):
		return self._email

	@email.setter
	def email(self, email):
		self._email = email
	
	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		self._name = name

	@property
	def number(self):
		return self._number

	@number.setter
	def number(self, number):
		self._number = number
	
class ContactGroup(Base):
	__tablename__ 	= 'contactgroup'
	id 				= Column(Integer(), primary_key=True)
	contact_id 		= Column(Integer(), ForeignKey('contact.id'))
	group_id 		= Column(Integer(), ForeignKey('group.id'))
	# Use cascade='delete,all' to propagate the deletion of a contactgroup onto its contacts
	contact 		= relationship(Contact,
						backref = backref('contacts',
						uselist = True,
						cascade = 'delete,all'))
	group 			= relationship(Group,
						backref = backref('groups',
						uselist = True,
						cascade = 'delete,all'))

if os.path.exists("config.json"):
	config 		= json.load(open("config.json"))
	user 		= config['user']
	password 	= config['password']
	host 		= config['host']
	port 		= config['port']
	db_name 	= config['db_name']
else:
	user 		= input("Enter database user: ")
	password 	= input("Enter database password: ")
	host 		= input("Enter database host address: ")
	port 		= input("Enter database port: ")
	db_name 	= input("Enter database named(default 'postgres'): ")

engine 	= create_engine('postgresql://{}:{}@{}:{}/{}'.format(user,password,host,port,db_name))
session = sessionmaker()
session.configure(bind = engine)
Base.metadata.create_all(engine)