# -*- encoding=utf8 -*-

class DataHolder(object):
    def __init__(self,value=None):self.value=value
    def set(self,value):self.value=value;return value
    def get(self):return self.value
