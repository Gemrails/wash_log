#!/usr/bin/python
#coding=utf-8

import wash_log
import sys

if __name__ == '__main__':
    logpath = sys.argv[1]
    isjson = sys.argv[2]
    wash_log.main_local(logpath, int(isjson))
 
