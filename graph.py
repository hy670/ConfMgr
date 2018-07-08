# -*- coding:utf8 -*-
import devicebase
import IPy
import networkx
import matplotlib.pylab as plt


def isozmbiepolicy(checkfirewall):
    print('begin' + checkfirewall.name + 'policycheck')
    print(checkfirewall.name + '######---独立存在的策略---######')
    # 遍历需要检测防火墙的原子策略表
    for checkpoliy in checkfirewall.policymiclist:
        issrcport = 0
        isdstport = 0
        # 不对未初始化的安全域策略检查
        for port in checkfirewall.portlink:
            if checkpoliy.srceth in port:
                issrcport = 1
            if checkpoliy.dsteth in port:
                isdstport = 1
        if issrcport == 0 or isdstport == 0:
            continue
        # 根据策略的源地址和目的地址 匹配拓扑网络区域地址
        for i in netaddrlist:
            if 1 == IPy.IP(i.netaddr).overlaps(checkpoliy.dstaddr):
                dstnet = i
                break
        for i in netaddrlist:
            if 1 == IPy.IP(i.netaddr).overlaps(checkpoliy.srcaddr):
                srcnet = i
                break
        # 根据策略的源区域和目的区域 确认策略路径 生成路径设备列表
        routelist = networkx.shortest_path(topology, source=srcnet, target=dstnet)
        iscontent = 0
        # 遍历路径设备列表
        for i in range(len(routelist)):
            # 设备与策略主机一致跳过
            if routelist[i] == firewall:
                pass
            # 如设备类型为防火墙
            elif routelist[i].type == 'firewall':
                # 根据上下游设备 确定检测策略经过本机的安全域或端口
                srceth = ''
                dsteth = ''
                for port in routelist[i].portlink:
                    if routelist[i - 1].name in port:
                        srceth = port.split('-')[0]
                    if routelist[i + 1].name in port:
                        dsteth = port.split('-')[0]
                # 遍历主机原子策略表，与经过的安全域策略比较是否有相应的策略
                for j in routelist[i].policymiclist:
                    if j.srceth == srceth and j.dsteth == dsteth:
                        iscontent = 1
                        if IPy.IP(checkpoliy.srcaddr).overlaps(j.srcaddr) == 1 or IPy.IP(j.srcaddr).overlaps(
                                checkpoliy.srcaddr) == 1:
                            if IPy.IP(checkpoliy.dstaddr).overlaps(j.dstaddr) == 1 or IPy.IP(j.dstaddr).overlaps(
                                    checkpoliy.dstaddr) == 1:
                                if checkpoliy.service == 'any' or j.service == 'any':
                                    # print("--------------------------------------------------------------")
                                    # checkpoliy.printpolicymic()
                                    # j.printpolicymic()
                                    iscontent = 2
                                    break
                                elif checkpoliy.service == j.service:
                                    # print("--------------------------------------------------------------")
                                    # checkpoliy.printpolicymic()
                                    # j.printpolicymic()
                                    iscontent = 2
                                    break
                # 标识  表示 1= 相关安全域策略未匹配 2= 匹配（存在相对应的策略）
                if iscontent == 1:
                    checkpoliy.printpolicymic()


# 创建防火墙FGT800
fgt800 = devicebase.FGT800('fgt800')
# 解析FGT800配置文件、并生成策略表
fgt800.parseconffile()

# 创建防火墙USG800
usg800 = devicebase.USG800('usg800')
# 解析配置文件
usg800.parseconffile()

# 创建防火墙列表
firewalllist = []
firewalllist.append(usg800)
firewalllist.append(fgt800)
c4948 = devicebase.EthSW('c4948')

# 创建网络节点并添加至网络节点列表
netaddrlist = []
lszaddr = devicebase.NetAddr('lszaddr', '192.169.3.0/24')
chenzaddr = devicebase.NetAddr('chenzaddr', '192.168.22.0/24')
internet = devicebase.NetAddr('internetaddr', '0.0.0.0/0')
testaddr = devicebase.NetAddr('testaddr', '10.16.7.0/24')
webaddr = devicebase.NetAddr('webaddr', '10.16.8.0/24')
appaddr = devicebase.NetAddr('appaddr', '10.16.16.0/24')
mgraddr = devicebase.NetAddr('mgraddr', '172.168.1.0/24')
netaddrlist.append(lszaddr)
netaddrlist.append(chenzaddr)
netaddrlist.append(testaddr)
netaddrlist.append(webaddr)
netaddrlist.append(appaddr)
netaddrlist.append(mgraddr)
netaddrlist.append(internet)

# 创建网络拓扑
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
topology.add_edge(fgt800, chenzaddr)

for firewall in firewalllist:
    isozmbiepolicy(firewall)
