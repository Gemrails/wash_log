#!/usr/bin/python
#coding=utf-8

import ConfigParser
import os

class CacheNopath(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class _ConfigGet(ConfigParser.ConfigParser):

    def read(self, config_name):
        '''
        重写父类read方法.增加配置文件名
        '''
        self.path = os.path.split(os.path.realpath(__file__))[0] + "/" + config_name
        print self.path
        if os.path.exists(self.path):
            pass
        else:
            raise CacheNopath("no such config.")

        if isinstance(self.path, basestring):
            filenames = [self.path]
        read_ok = []
        for filename in filenames:
            try:
                fp = open(filename)
            except IOError:
                continue
            self._read(fp, filename)
            fp.close()
            read_ok.append(filename)
        return read_ok


if __name__ == '__main__':
    cf = _ConfigGet()
    cf.read('sql_config.ini')
    print cf.get('inter-mysql', 'DBHOST')
