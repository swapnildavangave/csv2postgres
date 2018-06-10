from Contacts 		import Group, Contact, ContactGroup
from sqlalchemy 	import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import json
import os.path
import csv


def store(row, session):
	s 			= session()    
	contacts 	= [contact.id for contact in s.query(Contact).all() if row[1] == contact.name]
	groups 		= [group.id for group in s.query(Group).all() if row[0] == group.name]
	contact_id 	= None
	group_id 	= None
	if contacts:
		contact_id 	= contacts[0]
	if groups:
		group_id 	= groups[0]
	
	if contact_id is not None:
		record = [cg.id for cg in s.query(ContactGroup).all() if (cg.contact_id == contact_id and cg.group_id == group_id)]
		if record:
			print("Record Already Exist")
		else:
			cg = ContactGroup(contact_id = contact_id, group_id = group_id)
			s.add(cg)
			s.commit()
	else:
		c = Contact(name = row[1], number = row[2], email = row[3])
		s.add(c)
		s.commit()
		cid = max([contact.id for contact in s.query(Contact).all()])
		cg 	= ContactGroup(contact_id = cid, group_id = group_id)
		s 	= session()
		s.add(cg)
		s.commit()

if __name__=='__main__':

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
	engine 			= create_engine('postgresql://{}:{}@{}:{}/{}'.format(user,password,host,port,db_name))
	session 		= sessionmaker()
	session.configure(bind = engine)
	with open('test.csv', newline = '') as csvfile:
		spamreader = csv.reader(csvfile, delimiter = ',', quotechar = '"')
		for row in spamreader:
			store(row, session)