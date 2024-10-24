import os
cwd=os.getcwd()
opfile = os.path.join('.', '2b macro pass 2', 'OUTPUT.txt')
icfile = os.path.join('.', '2a macro pass 1', 'IC.txt')
mdtfile = os.path.join('.', '2a macro pass 1', 'MDT.txt')
mntfile = os.path.join('.', '2a macro pass 1', 'MNT.txt')

ic = open(icfile,"r")
mnt = open(mntfile,"r")
mdt = open(mntfile,"r")
i = ic.readlines()
n = mnt.readlines()
m = mdt.readlines()
ic.close()
mnt.close()
mdt.close()

f = open(opfile,"w")
for line in i:
    flag = 0
    temp = str(line).split()
    print(temp)
    for i2 in n:
        t = str(i2).split()
        if t[0] == temp[0]:
            flag = 1
            mdpt = int(str(t[1]))
            break
    if flag == 1:
        ala = str(temp[1]).split(",")
        flag += 1
    if flag > 1:
        lis = []
        for i2 in range(mdpt-1,len(m)):
            st = str(m[i2])[0:len(m[i2])-1]
            if st == "MEND":
                break
            else:
                lis.append(st)
        ala2 = []
        for item in range(len(lis)):
            tmp = str(lis[item]).split()
            if item == 0:
                ala2 = str(tmp[1]).split(",")
            if item > 0:
                f.write(tmp[0]+" ")
            tmp = str(tmp[1]).split(",")
            buffer = ""
            for k in tmp:
                for ii in range(len(ala2)):
                    if k == "#"+str(ii):
                        if len(ala) < len(ala2):
                            for l in range(len(ala2)):
                                aflag=0
                                for ll in range(len(ala2[l])):
                                    if ala2[l][ll] == '=':
                                        aflag = 1
                                if aflag == 1 and ll > l:
                                    ala2[l] = str(ala2[l]).split("=")[1]
                                else:
                                    ala2[l] = ala[l]
                                ala = ala2
                        h = ala[ii].split("=")

                        if len(h) == 2:
                            buffer += (str(h[1])+",")
                        else:
                            buffer += (str(h[0])+",")
            if item > 0:
                f.write(buffer[0:len(buffer)-1]+"\n")
    elif flag == 0:
        f.write(line)