import json
from datetime import *

from passlib.apps import custom_app_context as pwd_context
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# from itsdangerous import(TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
Base = declarative_base()
if __name__ == '__main__':
    DBSession = sessionmaker()



class Questions(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    gender = Column(String)
    age = Column(String)
    goal = Column(String)
    activity = Column(String)
    env = Column(String)
    intensity = Column(String)
    preference = Column(String)

# LOCAL
engine = create_engine('sqlite:///database.db')

Base.metadata.create_all(engine)