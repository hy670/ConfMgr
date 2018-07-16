# -*- coding:utf8 -*-
import IPy
import re
from firewallbase import *
class USG:
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
        self.metapolicylist = []

    def locataddr(self, addrID):
        for i in self.addrlist:
            if addrID == i.addrID:
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
                        self.policydetaillist) - 1].service.append(j)

    def creatmetapolicylist(self):
        for i in self.policydetaillist:
            for j in i.srcaddr:
                for k in i.dstaddr:
                    for l in i.service:
                        self.metapolicylist.append(MetaPolicy(i.name))
                        self.metapolicylist[len(self.metapolicylist) - 1].srceth = i.srceth
                        self.metapolicylist[len(self.metapolicylist) - 1].dsteth = i.dsteth
                        self.metapolicylist[len(self.metapolicylist) - 1].srcaddr = j
                        self.metapolicylist[len(self.metapolicylist) - 1].dstaddr = k
                        self.metapolicylist[len(self.metapolicylist) - 1].service = l

    def printmetapolicylist(self):
        for i in self.metapolicylist:
            print("policy id:" + i.name + " srceth:" + i.srceth +
                  " dsteth:" + i.dsteth + " srcaddr:" + i.srcaddr + " dstaddr:" + i.dstaddr + " service:" + i.service)

    def parseconffile(self):
        f = open('./conffile/usg.conf', 'r')
        for line in f:
            tokss = re.split(''' (?=(?:[^'"]|'[^']*'|"[^"]*")*$)''',line.strip())
            if len(tokss)>2:
                if tokss[1] == 'service' and tokss[2]== "service":
                    tempser = Ser(tokss[8])
                    serdic ={}
                    for i in range(9,len(tokss)-2,2):
                        serdic[tokss[i]]=tokss[i+1].split('"')[1]
                    for i in range(1,8):
                        tempstr ='protocol'+str(i)
                        if serdic[tempstr] != "256":
                            if (serdic['dlport'+str(i)])==(serdic['dhport'+str(i)]):
                                portdic ={}
                                portdic['dstport']=serdic['dlport'+str(i)]
                                portdic['portocol'] = serdic['protocol' + str(i)]
                                tempser.servicecontent.append(portdic)
                            else:
                                for j in range(int(serdic['dlport'+str(i)]),int(serdic['dhport'+str(i)])+1):
                                    portdic = {}
                                    portdic['dstport'] = str(j)
                                    portdic['portocol'] = serdic['protocol'+str(i)]
                                    tempser.servicecontent.append(portdic)
                    self.serlist.append(tempser)
                elif tokss[1] == 'service' and tokss[2] == "defaultservice":
                    tempser = Ser(tokss[8])
                    serdic = {}
                    for i in range(9, len(tokss) - 2, 2):
                        serdic[tokss[i]] = tokss[i + 1].split('"')[1]
                    portdic = {}
                    portdic['dstport'] = serdic['port']
                    portdic['portocol'] = serdic['protocol']
                    tempser.servicecontent.append(portdic)
                    self.serlist.append(tempser)
                elif tokss[1] == 'service' and tokss[2] == "servicegrp":
                    tempsergrp =ServGrp(tokss[8])
                    sergrpdic= {}
                    for i in range(9,len(tokss)-2,2):
                        sergrpdic[tokss[i]]=tokss[i+1].split('"')[1]
                elif tokss[1] == 'address' and tokss[2] == "address":
                    tempaddr= Addr(tokss[4],tokss[8])
                    addrdic = {}
                    for i in range(9,len(tokss)-2,2):
                        addrdic[tokss[i]]=tokss[i+1].split('"')[1]
                    if addrdic['type'] =='1':
                        tempaddr.addrcontent.append(str(IPy.IP(addrdic['ip'], make_net=True)))
                    elif addrdic['type'] =='2':
                        addrlh = addrdic['ip'].split('-')
                        addrl = addrlh[0]
                        addrh = addrlh[1]
                        addrlsplit =addrl.split('.')
                        addrhsplit =addrh.split('.')
                        if addrlsplit[0]!=addrhsplit[0]:
                           pass
                        elif addrlsplit[1] != addrhsplit[1]:
                            pass
                        elif addrlsplit[2] != addrhsplit[2]:
                            pass
                        elif addrlsplit[3] != addrhsplit[3]:
                            for i in range(int(addrlsplit[3]),int(addrhsplit[3])+1):
                                ipstr= addrlsplit[0]+"."+addrlsplit[1]+"."+addrlsplit[2]+"."+str(i)
                                tempaddr.addrcontent.append(ipstr)
                    elif addrdic['type'] =='3':
                        for j in addrdic['ip'].split(';'):
                            tempaddr.addrcontent.append(str(IPy.IP(j, make_net=True)))
                    self.addrlist.append(tempaddr)
                elif tokss[1] == 'address' and tokss[2] == "addrgrp":
                    temaddrgrp = AddrGrp(tokss[4],tokss[8])
                    print(line)
                    addrgrpdic = {}
                    for i in range(9,len(tokss)-2,2):
                        addrgrpdic[tokss[i]]=tokss[i+1].split('"')[1]
                    addrID=addrgrpdic['o_id'].split(';')
                    for i in addrID:
                        temaddrgrp.addressobject.append(i)
                    self.addrgrplist.append(temaddrgrp)
                elif tokss[1] == 'rule' and tokss[2] == "policyinfo":
                    temppolicy = Policy(tokss[4],tokss[8])
                    policydic= {}
                    for i in range(9,len(tokss)-2,2):
                        policydic[tokss[i]]=tokss[i+1].split('"')[1]
                    if policydic['type']=='1':
                        print(tokss[4]+"   "+tokss[8])
                        print(policydic)

        f.close()
        for i in self.addrgrplist:
            i.printaddrgrp()
        #self.creatpolicydetail()
        #self.creatmetapolicylist()

    def redundantcheck(self):
        for i in range(len(self.metapolicylist)):
            for j in range(i + 1, len(self.metapolicylist)):
                if self.metapolicylist[i].name != self.metapolicylist[j].name:
                    if self.metapolicylist[i].srceth == self.metapolicylist[j].srceth and \
                            self.metapolicylist[i].dsteth == self.metapolicylist[j].dsteth:
                        if IPy.IP(self.metapolicylist[i].srcaddr).overlaps(self.metapolicylist[j].srcaddr) == 1 or \
                                IPy.IP(self.metapolicylist[j].srcaddr).overlaps(self.metapolicylist[i].srcaddr) == 1:
                            if IPy.IP(self.metapolicylist[i].dstaddr).overlaps(self.metapolicylist[j].dstaddr) == 1 or \
                                    IPy.IP(self.metapolicylist[j].srcaddr).overlaps(self.metapolicylist[i].srcaddr) == 1:
                                if self.metapolicylist[i].service == 'any' or self.metapolicylist[j].service == 'any':
                                    print("--------------------------------------------------------------")
                                    self.metapolicylist[i].printpolicymic()
                                    self.metapolicylist[j].printpolicymic()
                                elif self.metapolicylist[i].service == self.metapolicylist[j].service:
                                    print("--------------------------------------------------------------")
                                    self.metapolicylist[i].printpolicymic()
                                    self.metapolicylist[j].printpolicymic()