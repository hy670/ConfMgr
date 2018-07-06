# -*- coding:utf8 -*-
import devicebase
import IPy
import networkx
import matplotlib.pylab as plt

fgt800 = devicebase.FGT800('fgt800')
fgt800.parseconffile()

usg800 = devicebase.USG800('usg800')
usg800.parseconffile()

c4948 = devicebase.EthSW('c4948')
netaddrlist = []
lszaddr = devicebase.NetAddr('lszaddr', '192.168.3.0/24')
internet = devicebase.NetAddr('internetaddr', '0.0.0.0/0')
testaddr = devicebase.NetAddr('testaddr', '10.16.7.0/24')
webaddr = devicebase.NetAddr('webaddr', '10.16.8.0/24')
appaddr = devicebase.NetAddr('appaddr', '10.16.16.0/24')
mgraddr = devicebase.NetAddr('mgraddr', '172.168.1.0/24')
netaddrlist.append(lszaddr)
netaddrlist.append(testaddr)
netaddrlist.append(webaddr)
netaddrlist.append(appaddr)
netaddrlist.append(mgraddr)
netaddrlist.append(internet)
topology = networkx.Graph()
topology.add_node(usg800, labels=usg800.name)
topology.add_node(fgt800, labels=fgt800.name)
topology.add_node(c4948, labels=c4948.name)
topology.add_node(internet, labels=internet.name)
topology.add_node(lszaddr, labels=lszaddr.name)
topology.add_node(testaddr, labels=testaddr.name)
topology.add_node(webaddr, labels=webaddr.name)
topology.add_node(appaddr, labels=appaddr.name)
topology.add_node(mgraddr, labels=mgraddr.name)
topology.add_edge(internet, usg800)
topology.add_edge(usg800, c4948)
topology.add_edge(usg800, mgraddr)
topology.add_edge(c4948, testaddr)
topology.add_edge(c4948, webaddr)
topology.add_edge(c4948, fgt800)
topology.add_edge(fgt800, appaddr)
topology.add_edge(fgt800, lszaddr)

print(usg800.policymiclist[0].srcaddr)
print(usg800.policymiclist[0].dstaddr)

for i in netaddrlist:
    if IPy.IP(i.netaddr).overlaps(usg800.policymiclist[0].dstaddr) == 1:
        dstnet = i
        break
for i in netaddrlist:
    if IPy.IP(i.netaddr).overlaps(usg800.policymiclist[0].srcaddr) == 1:
        srcnet = i
        break
routelist = networkx.shortest_path(topology, source=srcnet, target=dstnet)

for i in routelist:
    if i.type == 'firewall':
        print i.name
