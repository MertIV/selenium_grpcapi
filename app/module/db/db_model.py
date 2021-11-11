from datetime import datetime
from sqlalchemy import Column, Integer, String, MetaData, DateTime
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func
from sqlalchemy.sql.schema import ForeignKey

from app import db

Base = declarative_base()
meta = MetaData(db)

class Session(Base):
    __tablename__ ='session'
    id = Column(Integer, primary_key=True, index=True)
    pnumber_id = Column(Integer,ForeignKey('phone_number.id'),nullable=False)
    is_active = Column(String)

    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())

    chats = relationship("Chat",back_populates='session')
    clients = relationship("Client",back_populates='sessions')

    def __repr__(self):
        return "<Session(id='%s', pnumber_id='%s'')>" % (
                            self.id, self.pnumber_id)

class Client(Base):
    __tablename__ = 'client'
    id = Column(Integer, primary_key=True)
    client_pnumber = Column(String)

    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())

    sessions = relationship("Session",back_populates='clients')

    def __repr__(self):
        return "<Client(id='%s', phone_number='%s')>" % (
                            self.id, self.client_pnumber)

class Chat(Base):
    __tablename__ = 'chat'
    id = Column(Integer, primary_key=True)
    session_id = Column(Integer,ForeignKey('session.id'),nullable=False)
    client_id = Column(Integer,ForeignKey('client.id'),nullable=False)
    text = Column(String)
    route = Column(String)

    datetime = Column(DateTime(timezone=True), server_default=func.now())

    session = relationship("Session",back_populates='chats')

    def __repr__(self):
        return "<Chat(session_id='%s', text='%s')>" % (
                            self.session_id, self.text)

class Company(Base):
    __tablename__ = 'company'
    id = Column(Integer, primary_key=True)

    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())

    phone_numbers = relationship("Phonenumber",back_populates='company')

    def __repr__(self):
        return "<Company(id='%s',)>" % (
                            self.id)

class Phonenumber(Base):
    __tablename__ = 'phone_number'
    id = Column(Integer, primary_key=True)
    phone_number = Column(String)

    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())

    company = relationship("Company",back_populates='phone_numbers')

    def __repr__(self):
        return "<Phonenumber(company_id='%s', number='%s')>" % (
                            self.company_id, self.phone_number)

class Login(Base):
    __tablename__ = 'login'
    id = Column(Integer, primary_key=True)
    pnumber_id = Column(Integer,ForeignKey('phone_number.id'),nullable=False)
    is_logged = Column(String)
    qr = Column(String)

    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())


    def __repr__(self):
        return "<Login(pnumber_id='%s',is_logged='%s')>" % (
                            self.pnumber_id,self.is_logged)
