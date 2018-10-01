# -*- encoding:utf-8 -*-

from utils.MysqlUtil import *

class SougouList(DeclarationBase):
    __tablename__='t_sougou_list'

    id=Column('id',Integer,primary_key=True)
    url = Column('url', VARCHAR(255))
    filename = Column('filename', VARCHAR(512))
    create_time = Column('create_time', DATETIME)
    update_time = Column('update_time', DATETIME)
    hash=Column('hash',VARCHAR(64))

    def __init__(self,url,filename,create_time,update_time,hash):
        self.url=url
        self.filename=filename
        self.create_time = create_time
        self.update_time = update_time
        self.hash=hash


