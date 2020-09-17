#!/usr/bin/python3.8

with open ('nets.csv', 'r') as nets_file:
    for line in nets_file:
        tmp_line = line.replace('\n', '')
        print (tmp_line)
        ntwk_size = 2 ** (32 - (int(line[line.find('/')+1:line.find(';')])))
        print (ntwk_size)
        ntwk = line[:line.find('/')]
        print (ntwk)

        ntwk_addr = ntwk.split('.')
        for i in range(0, len(ntwk_addr)):
            ntwk_addr[i] = int(ntwk_addr[i]) 
        print (ntwk_addr, '\n')

        ip_addr = ntwk_addr
        if ntwk_addr[3] + (ntwk_size) <= 256:
            for i in range(0, ntwk_size - 1):
                ip_addr[3] = ip_addr[3] + 1
                print (ip_addr)
        else:
            for i in range(0, ntwk_size - 1):
                ip_addr = ip_addr[3] + 1
                print (ip_addr)




        print ('==============================================\n')