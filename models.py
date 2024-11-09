from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship,Mapped,mapped_column
from database import Base
from typing import List

class User(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,index=True)
    login=Column(String)
    password=Column(String)
    email=Column(String)
    role = relationship("Role",uselist=False, back_populates="user")
 
class Role(Base):
    __tablename__='roles'
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,index=True)
    user_id=Column(Integer,ForeignKey('users.id'))
    user=relationship('User',back_populates="role")

class Customer(Base):
    __tablename__='customers'
    id: Mapped[int] = mapped_column(primary_key=True)
    name=Column(String,index=True)
    phone_number=Column(String)
    status=Column(Integer)
    contract: Mapped[List["Contract"]] = relationship()

class Contract(Base):
    __tablename__='contracts'
    id: Mapped[int] = mapped_column(primary_key=True)
    date=Column(String,index=True)
    osmp=Column(String)
    customer_id: Mapped[int] = mapped_column(ForeignKey('customers.id'))
    service: Mapped[List["Service"]] = relationship()
    task = relationship("Task",uselist=False, back_populates="contract")

class Service(Base):
    __tablename__='services'
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,index=True)
    contract_id: Mapped[int] = mapped_column(ForeignKey('contracts.id'))

class Address(Base):
    __tablename__='addresses'
    id=Column(Integer,primary_key=True,index=True)
    house=Column(Integer,index=True)
    frac=Column(String)
    flat=Column(Integer)
    commutator = relationship("Commutator",uselist=False, back_populates="address")

class Commutator(Base):
    __tablename__='commutators'
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,index=True)
    ip=Column(String)
    address_id=Column(Integer,ForeignKey('addresses.id'))
    address=relationship('Address',back_populates="commutator")
    port: Mapped[List["Port"]] = relationship()

class Port(Base):
    __tablename__='ports'
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,index=True)
    number=Column(Integer)
    status_link=Column(String)
    commutator_id: Mapped[int] = mapped_column(ForeignKey('commutators.id'))

class Task(Base):
    __tablename__='tasks'
    id=Column(Integer,primary_key=True,index=True)
    topic=Column(String,index=True)
    description=Column(String)
    date_creation=Column(String)
    date_from=Column(String)
    date_to=Column(String)
    contract_id=Column(Integer,ForeignKey('contracts.id'))
    contract=relationship('Contract',back_populates="task")