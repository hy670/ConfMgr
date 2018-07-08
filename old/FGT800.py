# -*- coding:utf8 -*-
import os
import IPy
import regular
import devicebase


class address:
    def __init__(self, name=""):
        self.name = name
        self.addresscontent = []

    def addaddresscontent(self, content):
        self.addresscontent.append(content)

    def printaddress(self):
        print ('address name :'+self.name)
        for i in range(len(self.addresscontent)):
            print(' '+self.addresscontent[i])


class addressgroup:
    def __init__(self, name=""):
        self.name = name
        self.addressobject = []

    def addaddressobject(self, content):
        self.addressobject.append(content)

    def printaddressgroup(self):
        print ('addressgroup name :'+self.name)
        for i in range(len(self.addressobject)):
            print(' '+self.addressobject[i])


class service:
    def __init__(self, name=""):
        self.name = name
        self.servicecontent = []

    def addservicecontent(self, content):
        self.servicecontent.append(content)

    def printservice(self):
        print ('service name :'+self.name)
        for i in range(len(self.servicecontent)):
            print(' '+self.servicecontent[i])


class servicegroup:
    def __init__(self, name=""):
        self.name = name
        self.serviceobject = []

    def addserviceobject(self, content):
        self.serviceobject.append(content)

    def printservicegroup(self):
        print ('servicegroup name :'+self.name)
        for i in range(len(self.serviceobject)):
            print(self.serviceobject[i])


class policy:
    def __init__(self, name=""):
        self.name = name
        self.srceth = ''
        self.dsteth = ''
        self.srcaddr = []
        self.dstaddr = []
        self.service = []

    def printpolicy(self):
        print ('policy id :'+self.name)
        print (' policy srceth :'+self.srceth)
        print (' policy dsteth :'+self.dsteth)
        print (' policy srcaddr :')
        for i in range(len(self.srcaddr)):
            print(self.srcaddr[i])
        print (' policy dstaddr :')
        for i in range(len(self.dstaddr)):
            print(self.dstaddr[i])
        print (' policy service :')
        for i in range(len(self.service)):
            print(self.service[i])


class policydetail:
    def __init__(self, name=""):
        self.name = name
        self.srceth = ''
        self.dsteth = ''
        self.srcaddr = []
        self.dstaddr = []
        self.service = []

    def printpolicydetail(self):
        print ('policydetail id :'+self.name)
        print (' policydetail srceth :'+self.srceth)
        print (' policydetail dsteth :'+self.dsteth)
        print (' policydetail srcaddr :')
        for i in range(len(self.srcaddr)):
            print('  '+self.srcaddr[i])
        print (' policydetail dstaddr :')
        for i in range(len(self.dstaddr)):
            print('  '+self.dstaddr[i])
        print (' policydetail service :')
        for i in range(len(self.service)):
            print('  '+self.service[i])


class policymic:
    def __init__(self, name=""):
        self.name = name
        self.srceth = ''
        self.dsteth = ''
        self.srcaddr = ''
        self.dstaddr = ''
        self.service = ''

    def printpolicymic(self):
        print ('policydetail id :'+self.name+' srceth:'+self.srceth +
               ' dsteth :'+self.dsteth+'  srcaddr:'+self.srcaddr+' dstaddr:'+self.dstaddr+' service:'+self.service)


def locataddress(name):
    for i in addresslist:
        if name == i.name:
            return i
    return False


def locataddressgroup(name):
    for i in addressgrouplist:
        if name == i.name:
            return i
    return False


def locatservice(name):
    for i in servicelist:
        if name == i.name:
            return i
    return False


def locatservicegroup(name):
    for i in servicegrouplist:
        if name == i.name:
            return i
    return False

# 生成策略标准五元组


def creatpolicydetail(policylist):
    for i in policylist:
        policydetaillist.append(policydetail(i.name))
        policydetaillist[len(policydetaillist)-1].srceth = i.srceth
        policydetaillist[len(policydetaillist)-1].dsteth = i.dsteth
        for j in i.srcaddr:
            tempaddrgroup = locataddressgroup(j)
            if tempaddrgroup != False:
                for k in tempaddrgroup.addressobject:
                    tempaddr = locataddress(k)
                    if tempaddr != False:
                        for l in tempaddr.addresscontent:
                            policydetaillist[len(
                                policydetaillist)-1].srcaddr.append(l)
            elif locataddress(j) != False:
                tempaddr = locataddress(j)
                for l in tempaddr.addresscontent:
                    policydetaillist[len(
                        policydetaillist)-1].srcaddr.append(l)
            else:
                policydetaillist[len(
                                 policydetaillist)-1].srcaddr.append(j)
        for j in i.dstaddr:
            tempaddrgroup = locataddressgroup(j)
            if tempaddrgroup != False:
                for k in tempaddrgroup.addressobject:
                    tempaddr = locataddress(k)
                    if tempaddr != False:
                        for l in tempaddr.addresscontent:
                            policydetaillist[len(
                                policydetaillist)-1].dstaddr.append(l)
            elif locataddress(j) != False:
                tempaddr = locataddress(j)
                for l in tempaddr.addresscontent:
                    policydetaillist[len(
                        policydetaillist)-1].dstaddr.append(l)
            else:
                policydetaillist[len(
                                 policydetaillist)-1].dstaddr.append(j)
        for j in i.service:
            tempservicegroup = locatservicegroup(j)
            if tempservicegroup != False:
                for k in tempservicegroup.serviceobject:
                    tempservic = locatservice(k)
                    if tempservic != False:
                        for l in tempservic.servicecontent:
                            policydetaillist[len(
                                policydetaillist)-1].service.append(l)
            elif locatservice(j) != False:
                tempservic = locatservice(j)
                for l in tempservic.servicecontent:
                    policydetaillist[len(
                        policydetaillist)-1].service.append(l)
            else:
                policydetaillist[len(
                                 policydetaillist)-1].service.append(j)


def creatpolicmiclist(policydetaillist):
    for i in policydetaillist:
        for j in i.srcaddr:
            for k in i.dstaddr:
                for l in i.service:
                    policymiclist.append(policymic(i.name))
                    policymiclist[len(policymiclist)-1].srceth = i.srceth
                    policymiclist[len(policymiclist)-1].dsteth = i.dsteth
                    policymiclist[len(policymiclist)-1].srcaddr = j
                    policymiclist[len(policymiclist)-1].dstaddr = k
                    policymiclist[len(policymiclist)-1].service = l


def printpolicymiclist():
    for i in policymiclist:
        print ("policy id:"+i.name+" srceth:"+i.srceth +
               " dsteth:"+i.dsteth+" srcaddr:"+i.srcaddr+" dstaddr:"+i.dstaddr+" service:"+i.service)



addresslist = []
addressgrouplist = []
servicelist = []
servicegrouplist = []
policylist = []
policydetaillist = []
policymiclist = []

keyword = ''
f = open('FGT800.conf', 'r')
for line in f:
    # 设置对象关键字
    if('config firewall address' in line.strip()):
        keyword = 'address'
    elif('config firewall addrgrp' in line.strip()):
        keyword = 'addressgroup'
    elif('config firewall service custom' in line.strip()):
        keyword = 'service'
    elif('config firewall service group' in line.strip()):
        keyword = 'servicegroup'
    elif('config firewall policy' in line.strip()):
        keyword = 'policy'
    elif('config' in line.strip()):
        keyword = ''
    # 添加对象
    if(keyword == "address" and 'edit' in line.strip()):
        addresslist.append(
            address(line.strip().split(' ', 1)[1].split('"', 2)[1]))
    elif(keyword == "addressgroup" and 'edit' in line.strip()):
        addressgrouplist.append(
            addressgroup(line.strip().split(' ', 1)[1].split('"', 2)[1]))
    elif(keyword == "service" and 'edit' in line.strip()):
        servicelist.append(
            service(line.strip().split(' ', 1)[1].split('"', 2)[1]))
    elif(keyword == "servicegroup" and 'edit' in line.strip()):
        servicegrouplist.append(
            servicegroup(line.strip().split(' ', 1)[1].split('"', 2)[1]))
    elif(keyword == "policy" and 'edit' in line.strip()):
        policylist.append(
            policy(line.strip().split(' ', 1)[1].split('"', 2)[0]))
    # 添加对象内容
    if(keyword == "address" and 'set subnet' in line.strip()):
        ipaddr = line.strip().split(
            ' ', 3)[2]+'/'+line.strip().split(' ', 3)[3]
        addresslist[len(addresslist) -
                    1].addaddresscontent(IPy.IP(ipaddr, make_net=True).strNormal(1))
    elif(keyword == "addressgroup" and 'set member' in line.strip()):
        tokss = line.strip().split(' ', 2)[2].split('"')
        for i in tokss:
            if i != '' and i != ' ':
                addressgrouplist[len(addressgrouplist)-1].addaddressobject(i)
    elif(keyword == "service" and 'set tcp-portrange' in line.strip()):
        tokss = line.strip().split(' ')
        for i in range(2, len(tokss)):
            content = tokss[i].split(':')[0].split('-')
            if(content[0] == content[1]):
                servicelist[len(servicelist)-1].addservicecontent(content[0])
            elif(content[0] != '1' and content[1] != '65535'):
                for i in range(int(content[0]), int(content[1])+1):
                    servicelist[len(servicelist)-1].addservicecontent(str(i))
    elif(keyword == "servicegroup" and 'set member' in line.strip()):
        tokss = line.strip().split(' ', 2)[2].split('"')
        for i in tokss:
            if i != '' and i != ' ':
                servicegrouplist[len(servicegrouplist) -
                                 1].addserviceobject(i)
    elif(keyword == "policy"):
        if('set srcintf' in line.strip()):
            tokss = line.strip().split(' ', 2)[2].split('"')
            for i in tokss:
                if i != '' and i != ' ':
                    policylist[len(policylist) -
                               1].srceth = i
        elif('set dstintf' in line.strip()):
            tokss = line.strip().split(' ', 2)[2].split('"')
            for i in tokss:
                if i != '' and i != ' ':
                    policylist[len(policylist) -
                               1].dsteth = i
        elif('set srcaddr' in line.strip()):
            tokss = line.strip().split(' ', 2)[2].split('"')
            for i in tokss:
                if i != '' and i != ' ':
                    policylist[len(policylist) -
                               1].srcaddr.append(i)
        elif('set dstaddr' in line.strip()):
            tokss = line.strip().split(' ', 2)[2].split('"')
            for i in tokss:
                if i != '' and i != ' ':
                    policylist[len(policylist) -
                               1].dstaddr.append(i)
        elif('set service' in line.strip()):
            tokss = line.strip().split(' ', 2)[2].split('"')
            for i in tokss:
                if i != '' and i != ' ':
                    policylist[len(policylist) -
                               1].service.append(i)

f.close()
creatpolicydetail(policylist)
creatpolicmiclist(policydetaillist)

devicebase.redundantcheck(policymiclist)
regular.regularcheck(policymiclist)