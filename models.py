from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,index=True)
    login=Column(String)
    password=Column(String)
    email=Column(String)
 
class Role(Base):
    __tablename__='roles'
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,index=True)

class Customer(Base):
    __tablename__='Customers'
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,index=True)
    phone_number=Column(String)
    status=Column(Integer)

class Contract(Base):
    __tablename__='Contracts'
    id=Column(Integer,primary_key=True,index=True)
    date=Column(String,index=True)
    osmp=Column(String)

class Service(Base):
    __tablename__='Services'
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,index=True)

class Address(Base):
    __tablename__='Addresses'
    id=Column(Integer,primary_key=True,index=True)
    house=Column(Integer,index=True)
    frac=Column(String)
    flat=Column(Integer)

class Commutator(Base):
    __tablename__='Commutators'
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,index=True)
    ip=Column(String)

class Port(Base):
    __tablename__='Ports'
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,index=True)
    number=Column(Integer)
    status_link=Column(String)

class Task(Base):
    __tablename__='Tasks'
    id=Column(Integer,primary_key=True,index=True)
    topic=Column(String,index=True)
    description=Column(String)
    date_creation=Column(String)
    date_from=Column(String)
    date_to=Column(String)