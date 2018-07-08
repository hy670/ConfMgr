# -*- coding:utf8 -*-

import IPy


class Addr:
    def __init__(self, name=""):
        self.name = name
        self.addresscontent = []

    def addaddresscontent(self, content):
        self.addresscontent.append(content)

    def printaddress(self):
        print('address name :' + self.name)
        for i in range(len(self.addresscontent)):
            print(' ' + self.addresscontent[i])


class AddrGrp:
    def __init__(self, name=""):
        self.name = name
        self.addressobject = []

    def addaddressobject(self, content):
        self.addressobject.append(content)

    def printaddressgroup(self):
        print('addressgroup name :' + self.name)
        for i in range(len(self.addressobject)):
            print(' ' + self.addressobject[i])


class Ser:
    def __init__(self, name=""):
        self.name = name
        self.servicecontent = []

    def addservicecontent(self, content):
        self.servicecontent.append(content)

    def printservice(self):
        print('service name :' + self.name)
        for i in range(len(self.servicecontent)):
            print(' ' + self.servicecontent[i])


class ServGrp:
    def __init__(self, name=""):
        self.name = name
        self.serviceobject = []

    def addserviceobject(self, content):
        self.serviceobject.append(content)

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


class PolicyMic:
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


class FGT800:
    def __init__(self, name=""):
        self.name = name
        self.type = 'firewall'
        self.portlink = ['external-c4948', 'internal-appaddr', 'port2-lszaddr']
        self.addrlist = []
        self.addrgrplist = []
        self.serlist = []
        self.sergrplist = []
        self.policylist = []
        self.policydetaillist = []
        self.policymiclist = []

    def locataddr(self, name):
        for i in self.addrlist:
            if name == i.name:
                return i
        return 0

    def locataddrgrp(self, name):
        for i in self.addrgrplist:
            if name == i.name:
                return i
        return 0

    def locatser(self, name):
        for i in self.serlist:
            if name == i.name:
                return i
        return 0

    def locatsergrp(self, name):
        for i in self.sergrplist:
            if name == i.name:
                return i
        return 0

    # 生成策略标准五元组

    def creatpolicydetail(self):
        for i in self.policylist:
            self.policydetaillist.append(PolicyDetail(i.name))
            self.policydetaillist[len(self.policydetaillist) - 1].srceth = i.srceth
            self.policydetaillist[len(self.policydetaillist) - 1].dsteth = i.dsteth
            for j in i.srcaddr:
                tempaddrgrp = self.locataddrgrp(j)
                if tempaddrgrp != 0:
                    for k in tempaddrgrp.addressobject:
                        tempaddr = self.locataddr(k)
                        if tempaddr != 0:
                            for l in tempaddr.addresscontent:
                                self.policydetaillist[len(
                                    self.policydetaillist) - 1].srcaddr.append(l)
                elif self.locataddr(j):
                    tempaddr = self.locataddr(j)
                    for l in tempaddr.addresscontent:
                        self.policydetaillist[len(
                            self.policydetaillist) - 1].srcaddr.append(l)
                else:
                    self.policydetaillist[len(
                        self.policydetaillist) - 1].srcaddr.append(j)
            for j in i.dstaddr:
                tempaddrgrp = self.locataddrgrp(j)
                if tempaddrgrp != 0:
                    for k in tempaddrgrp.addressobject:
                        tempaddr = self.locataddr(k)
                        if tempaddr != 0:
                            for l in tempaddr.addresscontent:
                                self.policydetaillist[len(
                                    self.policydetaillist) - 1].dstaddr.append(l)
                elif self.locataddr(j):
                    tempaddr = self.locataddr(j)
                    for l in tempaddr.addresscontent:
                        self.policydetaillist[len(
                            self.policydetaillist) - 1].dstaddr.append(l)
                else:
                    self.policydetaillist[len(
                        self.policydetaillist) - 1].dstaddr.append(j)
            for j in i.service:
                tempservicegroup = self.locatsergrp(j)
                if tempservicegroup != 0:
                    for k in tempservicegroup.serviceobject:
                        tempservic = self.locatser(k)
                        if tempservic != 0:
                            for l in tempservic.servicecontent:
                                self.policydetaillist[len(
                                    self.policydetaillist) - 1].service.append(l)
                elif self.locatser(j):
                    tempservic = self.locatser(j)
                    for l in tempservic.servicecontent:
                        self.policydetaillist[len(
                            self.policydetaillist) - 1].service.append(l)
                else:
                    self.policydetaillist[len(
                        self.policydetaillist) - 1].service.append(str.lower(j))

    def creatpolicymiclist(self):
        for i in self.policydetaillist:
            for j in i.srcaddr:
                for k in i.dstaddr:
                    for l in i.service:
                        self.policymiclist.append(PolicyMic(i.name))
                        self.policymiclist[len(self.policymiclist) - 1].srceth = i.srceth
                        self.policymiclist[len(self.policymiclist) - 1].dsteth = i.dsteth
                        self.policymiclist[len(self.policymiclist) - 1].srcaddr = j
                        self.policymiclist[len(self.policymiclist) - 1].dstaddr = k
                        self.policymiclist[len(self.policymiclist) - 1].service = l

    def printpolicymiclist(self):
        for i in self.policymiclist:
            print("policy id:" + i.name + " srceth:" + i.srceth +
                  " dsteth:" + i.dsteth + " srcaddr:" + i.srcaddr + " dstaddr:" + i.dstaddr + " service:" + i.service)

    def parseconffile(self):
        keyword = ''
        f = open('FGT800.conf', 'r')
        for line in f:
            # 设置对象关键字
            if 'config firewall address' in line.strip():
                keyword = 'address'
            elif 'config firewall addrgrp' in line.strip():
                keyword = 'addressgroup'
            elif 'config firewall service custom' in line.strip():
                keyword = 'service'
            elif 'config firewall service group' in line.strip():
                keyword = 'servicegroup'
            elif 'config firewall policy' in line.strip():
                keyword = 'policy'
            elif 'config' in line.strip():
                keyword = ''
            # 添加对象
            if keyword == "address" and 'edit' in line.strip():
                self.addrlist.append(
                    Addr(line.strip().split(' ', 1)[1].split('"', 2)[1]))
            elif keyword == "addressgroup" and 'edit' in line.strip():
                self.addrgrplist.append(
                    AddrGrp(line.strip().split(' ', 1)[1].split('"', 2)[1]))
            elif keyword == "service" and 'edit' in line.strip():
                self.serlist.append(
                    Ser(line.strip().split(' ', 1)[1].split('"', 2)[1]))
            elif keyword == "servicegroup" and 'edit' in line.strip():
                self.sergrplist.append(
                    ServGrp(line.strip().split(' ', 1)[1].split('"', 2)[1]))
            elif keyword == "policy" and 'edit' in line.strip():
                self.policylist.append(
                    Policy(line.strip().split(' ', 1)[1].split('"', 2)[0]))
            # 添加对象内容
            if keyword == "address" and 'set subnet' in line.strip():
                ipaddr = line.strip().split(
                    ' ', 3)[2] + '/' + line.strip().split(' ', 3)[3]
                self.addrlist[len(self.addrlist) -
                              1].addaddresscontent(IPy.IP(ipaddr, make_net=True).strNormal(1))
            elif keyword == "addressgroup" and 'set member' in line.strip():
                tokss = line.strip().split(' ', 2)[2].split('"')
                for i in tokss:
                    if i != '' and i != ' ':
                        self.addrgrplist[len(self.addrgrplist) - 1].addaddressobject(i)
            elif keyword == "service" and 'set tcp-portrange' in line.strip():
                tokss = line.strip().split(' ')
                for i in range(2, len(tokss)):
                    content = tokss[i].split(':')[0].split('-')
                    if content[0] == content[1]:
                        self.serlist[len(self.serlist) - 1].addservicecontent(content[0])
                    elif content[0] != '1' and content[1] != '65535':
                        for j in range(int(content[0]), int(content[1]) + 1):
                            self.serlist[len(self.serlist) - 1].addservicecontent(str(j))
            elif keyword == "servicegroup" and 'set member' in line.strip():
                tokss = line.strip().split(' ', 2)[2].split('"')
                for i in tokss:
                    if i != '' and i != ' ':
                        self.sergrplist[len(self.sergrplist) -
                                        1].addserviceobject(i)
            elif keyword == "policy":
                if 'set srcintf' in line.strip():
                    tokss = line.strip().split(' ', 2)[2].split('"')
                    for i in tokss:
                        if i != '' and i != ' ':
                            self.policylist[len(self.policylist) - 1].srceth = i
                elif 'set dstintf' in line.strip():
                    tokss = line.strip().split(' ', 2)[2].split('"')
                    for i in tokss:
                        if i != '' and i != ' ':
                            self.policylist[len(self.policylist) - 1].dsteth = i
                elif 'set srcaddr' in line.strip():
                    tokss = line.strip().split(' ', 2)[2].split('"')
                    for i in tokss:
                        if i != '' and i != ' ':
                            self.policylist[len(self.policylist) - 1].srcaddr.append(i)
                elif 'set dstaddr' in line.strip():
                    tokss = line.strip().split(' ', 2)[2].split('"')
                    for i in tokss:
                        if i != '' and i != ' ':
                            self.policylist[len(self.policylist) - 1].dstaddr.append(i)
                elif 'set service' in line.strip():
                    tokss = line.strip().split(' ', 2)[2].split('"')
                    for i in tokss:
                        if i != '' and i != ' ':
                            self.policylist[len(self.policylist) - 1].service.append(i)
        f.close()
        self.creatpolicydetail()
        self.creatpolicymiclist()

    def redundantcheck(self):
        for i in range(len(self.policymiclist)):
            for j in range(i + 1, len(self.policymiclist)):
                if self.policymiclist[i].name != self.policymiclist[j].name:
                    if self.policymiclist[i].srceth == self.policymiclist[j].srceth and \
                            self.policymiclist[i].dsteth == self.policymiclist[j].dsteth:
                        if IPy.IP(self.policymiclist[i].srcaddr).overlaps(self.policymiclist[j].srcaddr) == 1 or \
                                IPy.IP(self.policymiclist[j].srcaddr).overlaps(self.policymiclist[i].srcaddr) == 1:
                            if IPy.IP(self.policymiclist[i].dstaddr).overlaps(self.policymiclist[j].dstaddr) == 1 or \
                                    IPy.IP(self.policymiclist[j].srcaddr).overlaps(self.policymiclist[i].srcaddr) == 1:
                                if self.policymiclist[i].service == 'any' or self.policymiclist[j].service == 'any':
                                    print("--------------------------------------------------------------")
                                    self.policymiclist[i].printpolicymic()
                                    self.policymiclist[j].printpolicymic()
                                elif self.policymiclist[i].service == self.policymiclist[j].service:
                                    print("--------------------------------------------------------------")
                                    self.policymiclist[i].printpolicymic()
                                    self.policymiclist[j].printpolicymic()


class USG800:
    def __init__(self, name=""):
        self.name = name
        self.type = 'firewall'
        self.portlink = ['eth0-internetaddr', 'eth1-mgraddr', 'eth2-c4948']
        self.addrlist = []
        self.addrgrplist = []
        self.serlist = []
        self.sergrplist = []
        self.policylist = []
        self.policydetaillist = []
        self.policymiclist = []

    def locataddr(self, name):
        for i in self.addrlist:
            if name == i.name:
                return i
        return False

    def locataddrgrp(self, name):
        for i in self.addrgrplist:
            if name == i.name:
                return i
        return False

    def locatser(self, name):
        for i in self.serlist:
            if name == i.name:
                return i
        return False

    def locatsergrp(self, name):
        for i in self.sergrplist:
            if name == i.name:
                return i
        return False

    # 生成策略标准五元组

    def creatpolicydetail(self):
        for i in self.policylist:
            self.policydetaillist.append(PolicyDetail(i.name))
            self.policydetaillist[len(self.policydetaillist) - 1].srceth = i.srceth
            self.policydetaillist[len(self.policydetaillist) - 1].dsteth = i.dsteth
            for j in i.srcaddr:
                tempaddrgrp = self.locataddrgrp(j)
                if tempaddrgrp != 0:
                    for k in tempaddrgrp.addressobject:
                        tempaddr = self.locataddr(k)
                        if tempaddr != 0:
                            for l in tempaddr.addresscontent:
                                self.policydetaillist[len(
                                    self.policydetaillist) - 1].srcaddr.append(l)
                elif self.locataddr(j):
                    tempaddr = self.locataddr(j)
                    for l in tempaddr.addresscontent:
                        self.policydetaillist[len(
                            self.policydetaillist) - 1].srcaddr.append(l)
                else:
                    self.policydetaillist[len(
                        self.policydetaillist) - 1].srcaddr.append(j)
            for j in i.dstaddr:
                tempaddrgrp = self.locataddrgrp(j)
                if tempaddrgrp != 0:
                    for k in tempaddrgrp.addressobject:
                        tempaddr = self.locataddr(k)
                        if tempaddr != 0:
                            for l in tempaddr.addresscontent:
                                self.policydetaillist[len(
                                    self.policydetaillist) - 1].dstaddr.append(l)
                elif self.locataddr(j):
                    tempaddr = self.locataddr(j)
                    for l in tempaddr.addresscontent:
                        self.policydetaillist[len(
                            self.policydetaillist) - 1].dstaddr.append(l)
                else:
                    self.policydetaillist[len(
                        self.policydetaillist) - 1].dstaddr.append(j)
            for j in i.service:
                tempservicegroup = self.locatsergrp(j)
                if tempservicegroup != 0:
                    for k in tempservicegroup.serviceobject:
                        tempservic = self.locatser(k)
                        if tempservic != 0:
                            for l in tempservic.servicecontent:
                                self.policydetaillist[len(
                                    self.policydetaillist) - 1].service.append(l)
                elif self.locatser(j):
                    tempservic = self.locatser(j)
                    for l in tempservic.servicecontent:
                        self.policydetaillist[len(
                            self.policydetaillist) - 1].service.append(l)
                else:
                    self.policydetaillist[len(
                        self.policydetaillist) - 1].service.append(j)

    def creatpolicymiclist(self):
        for i in self.policydetaillist:
            for j in i.srcaddr:
                for k in i.dstaddr:
                    for l in i.service:
                        self.policymiclist.append(PolicyMic(i.name))
                        self.policymiclist[len(self.policymiclist) - 1].srceth = i.srceth
                        self.policymiclist[len(self.policymiclist) - 1].dsteth = i.dsteth
                        self.policymiclist[len(self.policymiclist) - 1].srcaddr = j
                        self.policymiclist[len(self.policymiclist) - 1].dstaddr = k
                        self.policymiclist[len(self.policymiclist) - 1].service = l

    def printpolicymiclist(self):
        for i in self.policymiclist:
            print("policy id:" + i.name + " srceth:" + i.srceth +
                  " dsteth:" + i.dsteth + " srcaddr:" + i.srcaddr + " dstaddr:" + i.dstaddr + " service:" + i.service)

    def parseconffile(self):
        keyword = ''
        f = open('219.txt', 'r')
        for line in f:
            if not line[0].isspace():
                tokss = line.strip().split(' ')
                if tokss[0] == 'address':
                    keyword = tokss[0]
                    self.addrlist.append(Addr(tokss[1]))
                elif tokss[0] == 'address-group':
                    keyword = tokss[0]
                    self.addrgrplist.append(AddrGrp(tokss[1]))
                elif tokss[0] == 'service':
                    keyword = tokss[0]
                    self.serlist.append(Ser(tokss[1]))
                elif tokss[0] == 'service-group':
                    keyword = tokss[0]
                    self.sergrplist.append(ServGrp(tokss[1]))
                elif tokss[0] == 'policy':
                    keyword = tokss[0]
                    self.policylist.append(Policy(tokss[1]))
                    self.policylist[len(self.policylist) - 1].srceth = tokss[2]
                    self.policylist[len(self.policylist) - 1].dsteth = tokss[3]
                    if tokss[4] != 'any':
                        self.policylist[len(self.policylist) - 1].srcaddr.append(tokss[4])
                    else:
                        self.policylist[len(self.policylist) - 1].srcaddr.append('0.0.0.0/0')
                    if tokss[5] != 'any':
                        self.policylist[len(self.policylist) - 1].dstaddr.append(tokss[5])
                    else:
                        self.policylist[len(self.policylist) - 1].dstaddr.append('0.0.0.0/0')
                    self.policylist[len(self.policylist) - 1].service.append(tokss[6])

            else:
                if keyword == "address":
                    tokss = line.strip().split(' ')
                    if tokss[0] == 'host-address' or tokss[0] == 'net-address':
                        self.addrlist[len(self.addrlist) - 1].addaddresscontent(tokss[1])
                if keyword == "address-group":
                    tokss = line.strip().split(' ')
                    if tokss[0] == 'address-object':
                        self.addrgrplist[len(self.addrgrplist) - 1].addaddressobject(tokss[1])
                if keyword == "service":
                    tokss = line.strip().split(' ')
                    if len(tokss) > 1:
                        if tokss[1] == 'dest':
                            self.serlist[len(self.serlist) - 1].addservicecontent(tokss[2])
                if keyword == "service-group":
                    tokss = line.strip().split(' ')
                    if tokss[0] == 'service-object':
                        self.sergrplist[len(self.sergrplist) - 1].addserviceobject(tokss[1])
        f.close()
        self.creatpolicydetail()
        self.creatpolicymiclist()

    def redundantcheck(self):
        for i in range(len(self.policymiclist)):
            for j in range(i + 1, len(self.policymiclist)):
                if self.policymiclist[i].name != self.policymiclist[j].name:
                    if self.policymiclist[i].srceth == self.policymiclist[j].srceth and \
                            self.policymiclist[i].dsteth == self.policymiclist[j].dsteth:
                        if IPy.IP(self.policymiclist[i].srcaddr).overlaps(self.policymiclist[j].srcaddr) == 1 or \
                                IPy.IP(self.policymiclist[j].srcaddr).overlaps(self.policymiclist[i].srcaddr) == 1:
                            if IPy.IP(self.policymiclist[i].dstaddr).overlaps(self.policymiclist[j].dstaddr) == 1 or \
                                    IPy.IP(self.policymiclist[j].srcaddr).overlaps(self.policymiclist[i].srcaddr) == 1:
                                if self.policymiclist[i].service == 'any' or self.policymiclist[j].service == 'any':
                                    print("--------------------------------------------------------------")
                                    self.policymiclist[i].printpolicymic()
                                    self.policymiclist[j].printpolicymic()
                                elif self.policymiclist[i].service == self.policymiclist[j].service:
                                    print("--------------------------------------------------------------")
                                    self.policymiclist[i].printpolicymic()
                                    self.policymiclist[j].printpolicymic()


class NetAddr:
    def __init__(self, name, netaddr):
        self.name = name
        self.type = 'netaddr'
        self.netaddr = netaddr


class EthSW:
    def __init__(self, name):
        self.name = name
        self.type = 'SW'
