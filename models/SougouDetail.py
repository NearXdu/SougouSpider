# -*- encoding:utf-8 -*-

from utils.MysqlUtil import *

class SougouDetail(DeclarationBase):
    __tablename__='t_sougou_detail'

    id=Column('id',Integer,primary_key=True)
    filename=Column('filename',VARCHAR(512))
    url = Column('url', VARCHAR(255))
    create_time = Column('create_time', DATETIME)
    update_time = Column('update_time', DATETIME)

    def __init__(self,filename,url,create_time,update_time):
        self.filename = filename
        self.url = url
        self.create_time = create_time
        self.update_time = update_time


