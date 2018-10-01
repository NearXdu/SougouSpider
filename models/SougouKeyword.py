# -*- encoding:utf-8 -*-

from utils.MysqlUtil import *

class SougouKeyword(DeclarationBase):
    __tablename__='t_sougou_keyword'

    id=Column('id',Integer,primary_key=True)
    keyword=Column('keyword',VARCHAR(255))
    create_time = Column('create_time', DATETIME)
    update_time = Column('update_time', DATETIME)

    def __init__(self,keyword,create_time,update_time):
        self.keyword=keyword
        self.create_time = create_time
        self.update_time = update_time


