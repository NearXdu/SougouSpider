import hashlib
class Utils(object):
    @staticmethod
    def hash(data):
        return hashlib.md5(data).hexdigest()