# -*- coding:utf8 -*-
import devicebase
import networkx
import matplotlib.pylab as plt

fgt800 = devicebase.FGT800('fgt800')
# fgt800.parseconffile()

usg800 = devicebase.USG800('usg800')
# usg800.parseconffile()

c4948 = devicebase.EthSW('c4948')

lszaddr = devicebase.NetAddr('lszaddr', '192.168.3.0/24')
internet = devicebase.NetAddr('internetaddr', '0.0.0.0/0')
testaddr = devicebase.NetAddr('testaddr', '10.16.7.0/24')
webaddr = devicebase.NetAddr('webaddr', '10.16.8.0/24')
appaddr = devicebase.NetAddr('appaddr', '10.16.16.0/24')
mgraddr = devicebase.NetAddr('mgraddr', '172.168.1.0/24')

topology = networkx.Graph()
topology.add_node(usg800, labels=usg800.name)
topology.add_node(fgt800,labels=fgt800.name)
topology.add_node(c4948, labels=c4948.name)
topology.add_node(internet,labels =internet.name)
topology.add_node(lszaddr, labels = lszaddr.name)
topology.add_node(testaddr, labels =testaddr.name)
topology.add_node(webaddr, labels = webaddr.name)
topology.add_node(appaddr,labels =appaddr.name)
topology.add_node(mgraddr,labels =mgraddr.name)
topology.add_edge(internet, usg800)
topology.add_edge(usg800, c4948)
topology.add_edge(usg800, mgraddr)
topology.add_edge(c4948, testaddr)
topology.add_edge(c4948, webaddr)
topology.add_edge(c4948, fgt800)
topology.add_edge(fgt800, appaddr)
topology.add_edge(fgt800, lszaddr)

routelist =networkx.shortest_path(topology,source=lszaddr,target=internet)
for i in routelist:
    print i.name


