from sqlalchemy import Column,  Integer, String,DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import datetime

Base = declarative_base()

class Entry(Base):
    __tablename__ = 'entry'
    id = Column(Integer, primary_key = True)
    title =Column(String(256), nullable = False)
    content = Column(Text)
    date = Column(DateTime, default=datetime.datetime.now)

#pyanywhere
engine = create_engine('mysql+pymysql://root:hadoop@localhost',
pool_recycle=280, echo=True)

engine.execute("USE jira") # select new db


DBSession = sessionmaker(bind=engine)
db_session = DBSession()