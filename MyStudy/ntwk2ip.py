#!/usr/bin/python3.8

import ipaddress, os

with open ('./nets.csv', 'r') as nets_file:
    for line in nets_file:
        with open ('./ip-addresses.csv', 'a') as ip_addr_file:
            for ip_addr in ipaddress.IPv4Network(line.replace('\n', '')).hosts():
                ip_addr = str(ip_addr)
                #print (str(os.system('ping %s -n 1' % (ip_addr,))))
                result = str(ip_addr),';',str((os.system('ping %s -n 1' % (ip_addr,)))),';\n'
                ip_addr_file.writelines (result)
