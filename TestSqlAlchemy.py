#! /usr/bin/env python3
# -*- encoding:utf-8 -*-

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    """docstring for User"""
    __tablename__ = 'user'

    id=Column(String(20), primary_key=True)
    name = Column(String(20))

    #one to multi
    # books = relationship('Book')

class Book(Base):
    """docstring for Book"""
    __tablename__ = 'book'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))

    #
    # user_id = Column(String(20), ForeignKey('user.id'))

engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/blog')

DBSession = sessionmaker(bind=engine)

session = DBSession()
new_user = User(id='2', name = 'bob')
session.add(new_user)
session.commit()
session.close()

session = DBSession()
user = session.query(User).filter(User.id == '2').one()
print('type:', type(user))
print('name:', user.name)
session.close()
