import psycopg2 as pg2
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class ContactGroup(Base):
	__tablename__ = 'contactgroup'
	id 		= Column(Integer, primary_key=True)
	name 	= Column(String)
	
	@property
    def name(self):
        return self.name

    @email.setter
    def name(self, email):
        self.email = name

class Contact(Base):
	__tablename__ = 'contact'
	id = Column(Integer, primary_key=True)
	name = Column(String, unique=True)
	email = Column(String, unique=True)
	contactgroup_id = Column(Integer, ForeignKey('contactgroup.id'))
	# Use cascade='delete,all' to propagate the deletion of a contactgroup onto its contacts
	contactgroup = relationship(
		contactgroup,
		backref=backref('contacts',
						uselist=True,
						cascade='delete,all'))

	@validates('email')
    def validate_email(self, key, address):
        assert '@' in address
        return address

	@property
    def email(self):
        return self.email

    @email.setter
    def email(self, email):
        self.email = email
	
	@property
    def name(self):
        return self.name

    @email.setter
    def name(self, email):
        self.name = name
	
	

from sqlalchemy import create_engine
engine = create_engine('postgresql://admin:admin@localhost:5432/mydb')
from sqlalchemy.orm import sessionmaker
session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)
