# -*- coding:utf8 -*-

import IPy


class Addr:
    def __init__(self, addrid="", name=""):
        self.addrid =addrid
        self.name = name
        self.addrcontent = []

    def printaddr(self):
        print('address name :' + self.name)
        print('address ID :' + self.addrid)
        for i in range(len(self.addrcontent)):
            print(' ' + self.addrcontent[i])


class AddrGrp:
    def __init__(self, name=""):
        self.name = name
        self.addressobject = []


    def printaddressgroup(self):
        print('addressgroup name :' + self.name)
        for i in range(len(self.addressobject)):
            print(' ' + self.addressobject[i])


class Ser:
    def __init__(self, name=""):
        self.name = name
        self.servicecontent = []


    def printservice(self):
        print('service name :' + self.name)
        for i in range(len(self.servicecontent)):
            print(' ' + self.servicecontent[i])


class ServGrp:
    def __init__(self, name=""):
        self.name = name
        self.serviceobject = []


    def printservicegroup(self):
        print('servicegroup name :' + self.name)
        for i in range(len(self.serviceobject)):
            print(self.serviceobject[i])


class Policy:
    def __init__(self, name=""):
        self.name = name
        self.srceth = ''
        self.dsteth = ''
        self.srcaddr = []
        self.dstaddr = []
        self.service = []

    def printpolicy(self):
        print('policy id :' + self.name)
        print(' policy srceth :' + self.srceth)
        print(' policy dsteth :' + self.dsteth)
        print(' policy srcaddr :')
        for i in range(len(self.srcaddr)):
            print(self.srcaddr[i])
        print(' policy dstaddr :')
        for i in range(len(self.dstaddr)):
            print(self.dstaddr[i])
        print(' policy service :')
        for i in range(len(self.service)):
            print(self.service[i])


class PolicyDetail:
    def __init__(self, name=""):
        self.name = name
        self.srceth = ''
        self.dsteth = ''
        self.srcaddr = []
        self.dstaddr = []
        self.service = []

    def printpolicydetail(self):
        print('policydetail id :' + self.name)
        print(' policydetail srceth :' + self.srceth)
        print(' policydetail dsteth :' + self.dsteth)
        print(' policydetail srcaddr :')
        for i in range(len(self.srcaddr)):
            print('  ' + self.srcaddr[i])
        print(' policydetail dstaddr :')
        for i in range(len(self.dstaddr)):
            print('  ' + self.dstaddr[i])
        print(' policydetail service :')
        for i in range(len(self.service)):
            print('  ' + self.service[i])


class MetaPolicy:
    def __init__(self, name=""):
        self.name = name
        self.srceth = ''
        self.dsteth = ''
        self.srcaddr = ''
        self.dstaddr = ''
        self.service = ''

    def printpolicymic(self):
        print('policydetail id :' + self.name + ' srceth:' + self.srceth +
              ' dsteth :' + self.dsteth + '  srcaddr:' + self.srcaddr +
              ' dstaddr:' + self.dstaddr + ' service:' + self.service)
