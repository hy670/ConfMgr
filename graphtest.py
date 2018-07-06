# -*- coding:utf8 -*-
import networkx
import matplotlib.pylab as plt

class device:
    def __init__(self,name):
        self.name=name
        self.type= ''
        self.portlink = []
isg1000 =device('isg1000')
isg1000.type='firewall'
isg1000.portlink.append('0.0.0.0/0:internat')
isg1000.portlink.append('usg800:internal')

usg800 =device('usg800')
usg800.type='firewall'
usg800.portlink.append('isg1000:extranet')
usg800.portlink.append('c4948:internal')
usg800.portlink.append('172.168.1.0/24:internal')

fgt800 =device('fgt800')
fgt800.type='firewall'
fgt800.portlink.append('c4948:extranet')
fgt800.portlink.append('172.168.1.0/24:yunwei')

g = networkx.Graph()
g.add_node(usg800,type='firewall')
g.add_edge(usg800,'c4948')
g.add_edge(isg1000,usg800)
g.add_edge('c4948',fgt800)
g.add_edge('0.0.0.0/0',isg1000)
g.add_edge('c4948','10.16.7.0/24')
g.add_edge('c4948','10.16.8.0/24')
g.add_edge('10.16.16.0/24',fgt800)
g.add_edge('172.168.1.0/24',usg800)

routelist =networkx.shortest_path(g,source='0.0.0.0/0',target='10.16.16.0/24')
for i in range(len(routelist)-1):
    if isinstance(routelist[i],device):
        if routelist[i].type=='firewall':
            print(routelist[i].name)
            if isinstance(routelist[i-1],device):
                srcdevice = routelist[i-1].name
            else:
                srcdevice= routelist[i-1]
            if isinstance(routelist[i+1],device):
                dstdevice = routelist[i+1].name
            else:
                dstdevice= routelist[i+1]
            

networkx.draw(g,with_labels=True)
plt.savefig("ba.png",bbox_inches='tight')
plt.show()

