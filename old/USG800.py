# -*- coding:utf8 -*-
import os
import IPy
import regular

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
                            policydetaillist[len(policydetaillist)-1].service.append(l)
            elif locatservice(j) != False:
                tempservic = locatservice(j)
                for l in tempservic.servicecontent:
                    policydetaillist[len(policydetaillist)-1].service.append(l)
            else:
                policydetaillist[len(policydetaillist)-1].service.append(j)


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
addresslist.append(address('any'))
addresslist[0].addaddresscontent('0.0.0.0/0')
addressgrouplist = []
servicelist = []
servicegrouplist = []
policylist = []
policydetaillist = []
policymiclist = []

keyword = ''
f = open('219.txt', 'r')
for line in f:
    if not line[0].isspace():
        tokss = line.strip().split(' ')
        if(tokss[0] == 'address'):
            keyword = tokss[0]
            addresslist.append(address(tokss[1]))
        elif (tokss[0] == 'address-group'):
            keyword = tokss[0]
            addressgrouplist.append(addressgroup(tokss[1]))
        elif (tokss[0] == 'service'):
            keyword = tokss[0]
            servicelist.append(service(tokss[1]))
        elif (tokss[0] == 'service-group'):
            keyword = tokss[0]
            servicegrouplist.append(servicegroup(tokss[1]))
        elif (tokss[0] == 'policy'):
            keyword = tokss[0]
            policylist.append(policy(tokss[1]))
            policylist[len(policylist)-1].srceth = tokss[2]
            policylist[len(policylist)-1].dsteth = tokss[3]
            policylist[len(policylist)-1].srcaddr.append(tokss[4])
            policylist[len(policylist)-1].dstaddr.append(tokss[5])
            policylist[len(policylist)-1].service.append(tokss[6])

    else:
        if(keyword == "address"):
            tokss = line.strip().split(' ')
            if(tokss[0] == 'host-address' or tokss[0] == 'net-address'):
                addresslist[len(addresslist)-1].addaddresscontent(tokss[1])
        if(keyword == "address-group"):
            tokss = line.strip().split(' ')
            if(tokss[0] == 'address-object'):
                addressgrouplist[len(addressgrouplist) -
                                 1].addaddressobject(tokss[1])
        if(keyword == "service"):
            tokss = line.strip().split(' ')
            if(len(tokss) > 1):
                if(tokss[1] == 'dest'):
                    servicelist[len(servicelist)-1].addservicecontent(tokss[2])
        if(keyword == "service-group"):
            tokss = line.strip().split(' ')
            if(tokss[0] == 'service-object'):
                servicegrouplist[len(servicegrouplist) -
                                 1].addserviceobject(tokss[1])
f.close()
creatpolicydetail(policylist)
creatpolicmiclist(policydetaillist)

print("策略冗余检测开始---------")
for i in range(len(policymiclist)):
    for j in range(i+1, len(policymiclist)):
        if policymiclist[i].name != policymiclist[j].name:
            if policymiclist[i].srceth == policymiclist[j].srceth and policymiclist[i].dsteth == policymiclist[j].dsteth:
                if IPy.IP(policymiclist[i].srcaddr).overlaps(policymiclist[j].srcaddr) == 1:
                    if IPy.IP(policymiclist[i].dstaddr).overlaps(policymiclist[j].dstaddr) == 1:
                        if policymiclist[i].service == 'any'or policymiclist[j].service == 'any':
                            print("-----------------------------------------------------------------------")
                            policymiclist[i].printpolicymic()
                            policymiclist[j].printpolicymic()
                        elif policymiclist[i].service == policymiclist[j].service:
                            print("-----------------------------------------------------------------------")
                            policymiclist[i].printpolicymic()
                            policymiclist[j].printpolicymic()


print(len(policymiclist))
