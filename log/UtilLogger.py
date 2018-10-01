import os
import time
import logging

from utils.NoUse import NoUse


class UtilLogger(object):
    def __init__(self, name, logFile=None, level=logging.DEBUG):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s - %(message)s",
                                      '%Y-%m-%d %H:%M:%S')
        if logFile is None:
            handler = logging.StreamHandler()
        else:
            logDir = os.path.dirname(logFile)
            if logDir != "" and not os.path.exists(logDir):
                os.mkdir(logDir)
                NoUse.__no_use__()
            now = time.localtime()
            suffix = '.%d%02d%02d' % (now.tm_year, now.tm_mon, now.tm_mday)+'.log'
            handler = logging.FileHandler(logFile + suffix)
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log(self, message,level='debug'):
        levelMethod = {
            'debug': lambda: self.logger.debug(message),
            'info': lambda: self.logger.info(message),
            'warning': lambda: self.logger.warn(message),
            'error': lambda: self.logger.error(message),
        }[level.lower()]()



def tt():
    log = UtilLogger('testname')
    log.log('hahah')
    log.log('jjj','Info')
    log.log('asdfasdfasdf')


if __name__ == '__main__':
    tt()
