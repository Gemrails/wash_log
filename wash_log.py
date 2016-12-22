#!/usr/bin/python
#coding=utf-8

PATH_NGINX='/data/logs/nginx'
PATH_TEST='/tmp/log'
PATH_PHP='/data/logs/nginx'
cont_list = ['DE', 'GB', 'IE', 'IN', 'IT', 'MY', 'NG', 'NL', 'SG', 'US', 'ZA']
cont_list_c = ['德国', '英国', '爱尔兰', '印度', '意大利', '马来西亚', '尼日利亚', '荷兰', '新加坡', '美国', '南非']

import sys

a = sys.stdout
reload(sys)
sys.setdefaultencoding('utf-8')

import gzip
import json
import os
import urllib2
import country_short as cs
import time, datetime
from python_ipip.ipip import IP
from collections import Counter as cr
import re


class GetIpip():
    def __init__(self):
        self.lsip = IP
        self.lsip.load(os.path.abspath("python_ipip/17monipdb.dat"))

    def get_ip_name(self, ip):
        mm = self.lsip.find(ip).split('\t')[0]
        return str(mm)

def getdirlist():
    mm =os.listdir(PATH_TEST)
    print mm
    pass

def wlog(num, strs):
    filepath="/tmp/%s.log" % num
    fw = open(filepath, 'a+')
    fw.write(strs)
    fw.close()

def wlog_1(num, strs):
    filepath="/tmp/%s.log" % num
    fw = open(filepath, 'a+')
    fw.write(strs)
    fw.close()

def wlog_re(outname, strs):
    filepath = "/tmp/out_%s" % outname
    with open(filepath, 'a+') as fw:
        print filepath
        fw.write(str(strs)+'\n')
    return 0

def lookup(ip):

    #URL = 'http://freegeoip.net/json/' + ip
    URL = 'http://ip-api.com/json/' + ip
    urlobj = urllib2.urlopen(URL, timeout=5)
    data = urlobj.read()
    jdata = json.loads(data, encoding='utf-8')
    #{u'city': u'', u'region_code': u'', u'region_name': u'', u'ip': u'10.19.106.89', u'time_zone': u'', u'longitude': 0, u'metro_code': 0, u'latitude': 0, u'country_code': u'', u'country_name': u'', u'zip_code': u''}
    #{u'status': u'success', u'city': u'Beijing', u'zip': u'', u'countryCode': u'CN', u'country': u'China', u'region': u'11', u'isp': u'China Unicom Beijing', u'lon': 116.3883, u'timezone': u'Asia/Shanghai', u'as': u'AS4808 China Unicom Beijing Province Network', u'query': u'111.197.85.175', u'lat': 39.9289, u'org': u'China Unicom Beijing', u'regionName': u'Beijing'}
    if jdata['status'] == 'success':
        try:
            print "Count:%s, City:%s" %(cs.getcountry(jdata['countryCode']), str(jdata['city']))
            return "Count:%s, City:%s" %(cs.getcountry(jdata['countryCode']), str(jdata['city']))
        except UnicodeDecodeError:
            print  "error code..."


def lookup_country(ip):

    #URL = 'http://freegeoip.net/json/' + ip
    print ip
    mm = ip.split(".")
    if mm[0] == '10' and mm[1] == '8':
        return 'ERR'
    elif mm[0] == '10' and mm[1] == '19':
        return 'ERR'
    time.sleep(1)
    URL = 'http://ip-api.com/json/' + ip
    urlobj = urllib2.urlopen(URL, timeout=5)
    data = urlobj.read()
    jdata = json.loads(data, encoding='utf-8')
    #{u'city': u'', u'region_code': u'', u'region_name': u'', u'ip': u'10.19.106.89', u'time_zone': u'', u'longitude': 0, u'metro_code': 0, u'latitude': 0, u'country_code': u'', u'country_name': u'', u'zip_code': u''}
    #{u'status': u'success', u'city': u'Beijing', u'zip': u'', u'countryCode': u'CN', u'country': u'China', u'region': u'11', u'isp': u'China Unicom Beijing', u'lon': 116.3883, u'timezone': u'Asia/Shanghai', u'as': u'AS4808 China Unicom Beijing Province Network', u'query': u'111.197.85.175', u'lat': 39.9289, u'org': u'China Unicom Beijing', u'regionName': u'Beijing'}
    if jdata['status'] == 'success':
        try:
            print "Count_1:%s, City:%s" %(cs.getcountry(jdata['countryCode']), str(jdata['city']))
            #return str(cs.getcountry(jdata['countryCode']))
            return str(jdata['countryCode'])
        except UnicodeDecodeError:
            print  "error code..."
            return 9

def lookup_country_free(ip):
    #URL = 'http://freegeoip.net/json/' + ip
    print ip
    mm = ip.split(".")
    if mm[0] == '10' and mm[1] == '8':
        return 'ERR'
    elif mm[0] == '10' and mm[1] == '19':
        return 'ERR'
    time.sleep(0.1)
    URL = 'http://freegeoip.net/json/' + ip
    urlobj = urllib2.urlopen(URL, timeout=5)
    data = urlobj.read()
    jdata = json.loads(data, encoding='utf-8')
    #{u'city': u'', u'region_code': u'', u'region_name': u'', u'ip': u'10.19.106.89', u'time_zone': u'', u'longitude': 0, u'metro_code': 0, u'latitude': 0, u'country_code': u'', u'country_name': u'', u'zip_code': u''}
    #{u'status': u'success', u'city': u'Beijing', u'zip': u'', u'countryCode': u'CN', u'country': u'China', u'region': u'11', u'isp': u'China Unicom Beijing', u'lon': 116.3883, u'timezone': u'Asia/Shanghai', u'as': u'AS4808 China Unicom Beijing Province Network', u'query': u'111.197.85.175', u'lat': 39.9289, u'org': u'China Unicom Beijing', u'regionName': u'Beijing'}
    try:
        #print "Count_1:%s, cname:%s, City:%s" %(cs.getcountry(jdata['country_code']), str(jdata['country_name']), str(jdata['city']))
        #return str(cs.getcountry(jdata['countryCode']))
        print jdata['country_code']
        return str(jdata['country_code'])
    except UnicodeDecodeError:
        print  "error code..."
        return 9

def readlog(logpath, timel):

    with gzip.open(logpath, 'r') as fp:
        #lines = fp.readlines(10000)
        for line in fp:
            try:
                lineno = json.loads(line)
            except Exception, e:
                pass
            if lineno['request_time'] > int(timel):
                request_t = lineno['request_time']
                upstream_t = lineno['upstream_time']
                ips =  lineno['remote_addr']
                addr = lookup(lineno['remote_addr'])
            try:
                strips = "%s, %s, %s, %s\n" %(str(request_t), str(upstream_t), str(ips), str(addr))
                wlog(timel, strips)
            except Exception, e:
                pass
                # print line
    fp.close()
    



def getapi(logpath, uri):
    print uri
    base_uri = uri.split('/')
    apinum = []
    with gzip.open(logpath, 'r') as fp:
        for line in fp:
            try:
                linej = json.loads(line)
            except ValueError, e:
                pass
            if base_uri in linej['uri'].split('/'):
                addr = lookup_country_free(linej['remote_addr'])
                if addr in cont_list:
                    #print "find uri: %s, addr: %s" %(str(uri), addr)
                    apinum.append(addr)
    # return ['CN', 'CN', 'MM']
    apinum = [ cs.getcountry(x) for x in apinum ]
    return apinum

def read_local_log(logpath, gi):

    table_format1 = "line_info_%s"
    (filepath,filename)=os.path.split(logpath)
    mm = filename.split('.')
    if mm[0] == 'api':
        nn_time = ('_').join(mm[4].split('-')[:-1])
        table_name = table_format1 % nn_time
    else:
        table_name = table_format1 % '0000_00_00'
        print "Only api log can be analyst."
        pass

    with gzip.open(logpath, 'r') as fp:
        for line in fp:
            log_line(line, table_name, gi)



def log_line(line, table_name, gi):
    #依据母表生成当日子表
    try:
        lineno = json.loads(line)
    except Exception, e:
        pass
        print str(e)

    uri_re = lineno['uri']
    uuid = lineno['uuid']
    remote_ip = lineno['remote_addr']
    country = gi.get_ip_name(lineno['remote_addr'])
    visit_time = lineno['@timestamp']
    sql1 = "insert into %s (uri_re, uuid, country, remote_ip, visit_time) values ('%s', '%s', '%s', '%s', '%s');" %(table_name, uri_re, uuid, country, remote_ip, visit_time)
    return sql1

def _test_read_local_log(line, gi):

    lineno = json.loads(line)

    format1 = '%s^_^%s^_^%s^_^%s^_^%s'

    uri_re = lineno['uri']
    uuid = lineno['uuid']
    remote_ip = lineno['remote_addr']
    country = gi.get_ip_name(lineno['remote_addr'])
    visit_time = lineno['@timestamp']
    #agent = lineno['agent']
    #mm = format1.format(uri_re, uuid, remote_ip, country, visit_time, agent)
    mm = '%s^_^%s^_^%s^_^%s^_^%s' %(uri_re, uuid, remote_ip, country, visit_time)
    print mm


def getapi_local(logpath, uri, gi):
    print uri
    base_uri = ('').join(uri.split('/'))
    apinum = []
    with gzip.open(logpath, 'r') as fp:
        for line in fp:
            try:
                linej = json.loads(line)
                urr = linej['uri'].split('/')
                if len(urr) == len(base_uri and urr):
                    addr = gi.get_ip_name(linej['remote_addr'])
                    print addr
                    if addr in cont_list_c:
                        apinum.append(addr)

            except ValueError, e:
                # line format ERR
                pass
    return apinum

def ip_check(ip, gi):
    addr = gi.get_ip_name(ip)
    if addr in cont_list_c:
        return addr
    else:
        return 0

def getapi_from_re(logpath, uri, gi):
    apinum = []
    with gzip.open(logpath, 'r') as fp:
        for line in fp:
            try:
                linej = json.loads(line)
                urr = linej['uri']
                if len(re.findall(uri, urr)):
                    addr = gi.get_ip_name(linej['remote_addr'])
                    if addr in cont_list_c:
                        apinum.append(addr)
            except ValueError, e:
                #line format ERR
                pass
    return apinum

def getapi_from_re2(logpath, gi, uuid_list=None):
    from count_uri import count2_uri
    out_api = []
    with gzip.open(logpath, 'r') as fp:
        for line in fp:
            linej = json.loads(line)
            uuid = linej['uuid']
            if uuid in uuid_list:
                urr = linej['uri']
                for uri in count2_uri:
                    if len(re.findall(uri, urr)):
                        addr = gi.get_ip_name(linej['remote_addr'])
                        real_key = uuid + ':' + addr + str(uri)
                        out_api.append(real_key)
                        break
                    else:
                        continue
            else:
                continue
    print out_api
    return out_api


def main(logpath, isjson=0):
    from count_uri import count_upi
    jlist = []
    for i in count_upi:
        uritt = getapi(logpath, i)
        mm = ('_').join(i.split('/'))
        outpath = "result_%s" % mm
        dr = cr(uritt)
        if not isjson:
            #mm = json.dumps(dr, encoding="UTF-8", ensure_ascii=False, indent=4)
            mm = json.dumps(dr, encoding="UTF-8", ensure_ascii=False)
            rc = wlog_re(outpath, str(mm))
        jlist.append(i)
        jlist.append(uritt) 
    nn = json.dumps(jlist, encoding="UTF-8", ensure_ascii=False, indent=4)
    print nn
    return nn

def main_local(logpath, isjson=0):
    gi = GetIpip()
    from count_uri import count_upi
    jlist = []
    for uri in count_upi:
        uritt = getapi_from_re(logpath, uri, gi)
        dr = cr(uritt)
        jlist.append(uri)
        # common name
        jlist.append(dr.most_common())
    nn = json.dumps(jlist, encoding="UTF-8", ensure_ascii=False, indent=4)
    if not isjson:
        mm = os.path.basename(logpath) + "_out.json"
        outpath = "result_%s" % mm
        nn = json.dumps(jlist, encoding="UTF-8", ensure_ascii=False, indent=4)
        rc = wlog_re(outpath, str(nn))
        return rc
    print nn
    return nn

def main_line_in(logpath):
    gi = GetIpip()
    read_local_log(logpath, gi)


class TimeFormatCook(object):

    __format_inter = "%Y-%m-%d %H:%M:%S"
    __today = datetime.date.today()

    def __init__(self, time_string="1970-1-1 00:00:00"):
        '''
        2016-11-19 00:00:00
        '''
        self.format_inter = "%Y-%m-%d %H:%M:%S"
        self.today = datetime.date.today()

    def __today_format(self, timesetting=1):
        if timesetting == 1:
            print time.strftime(self.format_inter)

    @staticmethod
    def today_zero():
        '''
        string...
        '''
        return datetime.datetime.strftime(TimeFormatCook.__today, TimeFormatCook.__format_inter)

    @staticmethod
    def time_change(day=0):
        '''
        string -> datetime
        + - 相应天数获得对应时间.
        '''
        today_zero = datetime.datetime.strptime(TimeFormatCook.today_zero(), TimeFormatCook.__format_inter)
        if isinstance(day,(int)):
            day = int(day)
        day_change = today_zero + datetime.timedelta(days= day)
        return day_change


def get_valid_uuid(logpath, days=-1):
    from mysql_pool import sql_pool
    sp = sql_pool.MysqlPool()
    sql1 = "select uuid, created_ip, last_ip from uuids where created_at > '%s'" % TimeFormatCook.time_change(days)
    out = sp.getAll(sql1)
    '''
    out = ({'last_ip': '183.232.175.4', 'uuid': '908e804ebf4f3e2', 'created_ip': '183.232.175.4'},  \
           {'last_ip': '23.106.150.102', 'uuid': '2727557', 'created_ip': '23.106.150.102'},  \
           {'last_ip': '124.207.6.82', 'uuid': '354834060490145', 'created_ip': '124.207.6.82'},  \
           {'last_ip': '23.106.150.102', 'uuid': '2727565', 'created_ip': '23.106.150.102'},  \
           {'last_ip': '123.123.51.81', 'uuid': '8861c4c529a170a8f09d44fe1830c635e7f5b483', 'created_ip': '123.123.51.81'},  \
           {'last_ip': '23.91.100.107', 'uuid': '2727558', 'created_ip': '23.91.100.107'},  \
           {'last_ip': '124.207.6.82', 'uuid': 'c0531bd1b807a2ea0e5588980f38b922de6d5791', 'created_ip': '124.207.6.82'},  \
           {'last_ip': '23.91.100.107', 'uuid': '2727603', 'created_ip': '23.91.100.107'},  \
           {'last_ip': '124.207.6.82', 'uuid': '860582031986330', 'created_ip': '23.91.100.107'},  \
           {'last_ip': '183.232.175.3', 'uuid': '98f7bc077671eb0', 'created_ip': '183.232.175.3'},  \
           {'last_ip': '124.207.6.82', 'uuid': '29569e74f4b96209dedd32a589ca68e6d99acbb2', 'created_ip': '124.207.6.82'},  \
           {'last_ip': '218.205.184.14', 'uuid': 'bacdb540ca012a9c5ef2c5aed26e332e76d47789', 'created_ip': '124.207.6.82'},  \
           {'last_ip': '124.207.6.82', 'uuid': '2727539', 'created_ip': '124.207.6.82'},  \
           {'last_ip': '124.207.6.82', 'uuid': '2727612', 'created_ip': '124.207.6.82'},  \
           {'last_ip': '124.207.6.82', 'uuid': '2727567', 'created_ip': '124.207.6.82'})
    '''
    listout = list(out)
    gi = GetIpip()

    for mm in range(0, len(listout)):
        addr_real = ip_check(listout[mm].get('last_ip'), gi) or ip_check(out[mm].get('created_ip'), gi)
        if addr_real:
            #listout[mm]['uuid'] = listout[mm].get('uuid') + ':' + addr_real
            pass
        else:
            listout[mm] = {}

    list_uuids = [listout[i].get('uuid') for i in xrange(len(listout)) if listout[i].get('uuid') ]

    nn = json.dumps(getapi_from_re2(logpath, gi, list_uuids), encoding="UTF-8", ensure_ascii=False, indent=4)
    return nn


if __name__ == '__main__':
    #print TimeFormatCook.today_zero()
    #print type(TimeFormatCook.time_change())
    gi = GetIpip()
    line = '{"@timestamp":"2016-12-19T16:32:21+08:00","server_addr":"10.8.97.205","remote_addr":"124.207.6.82","scheme":"http","host":"beta-api.allfootballapp.com","method":"GET","uri":"/upgrade?platform=android&is_sem=0","url":"/index.php","protocol":"HTTP/1.1","status":200,"size":248,"request_time":0.089,"upstream_time":"0.078","upstream_host":"127.0.0.1:9000","referer":"-","agent":"Mozilla/5.0 (Linux; Android 6.0; PLK-AL10 Build/HONORPLK-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/49.0.2623.105 Mobile Safari/537.36 News/7 Android/7 AppFootball/7 SDK/23","xff":"124.207.6.82","uuid": "860582031986330","authorization":"","lang":"zh-cn"}'
    print log_line(line, 'line_info_2016_12_21', gi)



