import hashlib
class Utils(object):
    @staticmethod
    def hash(data):
        data=data.encode('utf-8')
        return hashlib.md5(data).hexdigest()