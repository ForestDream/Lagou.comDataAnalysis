#!/usr/bin/env python
# coding:utf-8

import urllib
import urllib2
import json

class Position:
    '''A positino in L with lowSalary, highSalary and campany'''
    def __init__(self, positionName, salary, companyName):
        self.positionName = positionName
        self.salary = salary
        self.companyName = companyName

def sendPostRequest(postData = {'first':True, 'pn':1, 'kd':'python'}):
    postData = urllib.urlencode(postData)
    url = 'http://www.lagou.com/jobs/positionAjax.json?px=default&gx=%E5%85%A8%E8%81%8C&city=%E5%8C%97%E4%BA%AC'
    rcv = urllib2.urlopen(url, postData)
    rcv = rcv.read()
    #print rcv
    return rcv

def parsePage(i, keyWord, p):
    if i == 0:
        postData = {'first':True, 'pn':1, 'kd':keyWord}
    else:
        postData = {'first':False, 'pn':i+1, 'kd':keyWord} 
    print 'page', i+1, postData
    data = json.loads(sendPostRequest(postData))
    #print data
    if(data['content']['pageSize'] == 15):
        pageSize = 15
    else:
        pageSize = data['content']['pageSize'] - 1
    if(i < data['content']['totalPageCount']):
        if(i == data['content']['totalPageCount'] - 1):
            print data['content']['pageSize']
        for j in range(0, pageSize):
            p.append(Position(data['content']['result'][j]['positionName'], data['content']['result'][j]['salary'], data['content']['result'][j]['companyName']))
            print "%-24s\t%-8s\t%-8s" % (p[-1].positionName, p[-1].salary, p[-1].companyName)
        print

def parsePages(total, keyWord):
    p = []
    for i in range(0, total):
        parsePage(i, keyWord, p)
    return p

if __name__ == '__main__':
    keyWord = raw_input('Please Input the job u wanna search:')
    print
    p = parsePages(30, keyWord)
    for j in range(0, len(p)):
        #print "%-24s\t%-8s\t%-8s" % (p[j].positionName, p[j].salary, p[j].companyName)
        pass
    print
