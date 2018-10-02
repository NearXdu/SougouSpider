# -*- encoding:utf-8 -*-
import pymysql
#pymysql.install_as_MySQLdb()
from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.dialects.mysql import VARCHAR, DATETIME,DATE,FLOAT
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.pool import NullPool
from config import Settings
from sqlalchemy.orm import sessionmaker

DeclarationBase=declarative_base()

def build_session(db_name='sougoudb',pool=True,transaction=True):
    if pool:
        return sessionmaker(
            bind=create_engine(URL(**Settings.DATABASE[db_name]),
                               connect_args={'charset': 'utf8'}, pool_size=5,
                               pool_recycle=290), autocommit=not transaction)()


    return sessionmaker(bind=create_engine(URL(**Settings.DATABASE[db_name]),
                           connect_args={'charset': 'utf8'},
                           poolclass=NullPool),autocommit=not transaction)()



