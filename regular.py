import os
import IPy
import devicebase

def regularcheck(policymiclist):
    denyregularlist= []
    f =open('denyregular.txt','r')
    for line  in f:
        tokss=line.strip().split(' ')
        denyregularlist.append(devicebase.policymic(tokss[0]))
        denyregularlist[len(denyregularlist)-1].srcaddr=tokss[1]
        denyregularlist[len(denyregularlist)-1].dstaddr=tokss[2]
        denyregularlist[len(denyregularlist)-1].service=tokss[3]
    f.close()
    print('##########beging regularchecke########')

    for i in denyregularlist:
        for j in policymiclist:
            if IPy.IP(i.srcaddr).overlaps(j.srcaddr) == 1:
                    if IPy.IP(i.dstaddr).overlaps(j.dstaddr) == 1:
                        if i.service == 'any'or j.service == 'any':
                            print("-----------------------------------------------------------------------")
                            i.printpolicymic()
                            j.printpolicymic()
                        elif i.service == j.service:
                            print("-----------------------------------------------------------------------")
                            i.printpolicymic()
                            j.printpolicymic()





