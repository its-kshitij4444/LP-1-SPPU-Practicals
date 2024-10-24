import os
ipfile=os.path.join('.','2a macro pass 1','Input.txt')
cwd=os.getcwd()
icfile=os.path.join(cwd,'2a macro pass 1','IC.txt')
mdtfile=os.path.join(cwd,'2a macro pass 1','MDT.txt')
mntfile=os.path.join(cwd,'2a macro pass 1','MNT.txt')
with open(ipfile,"r")as f:
    file = f.readlines()

f = open(mdtfile,"w")
f.close()
f = open(mdtfile,"r")
f2 = f.readlines()
f.close()
mdpt = len(f2)+1

ala = []
mnt = open(mntfile, "w")
mdt = open(mdtfile, "w")
ic = open(icfile, "w")
flag = 0

for line in file:
    l = str(line[0:len(line)-1])
    if l == "MACRO":
        flag = 1
    elif l == "MEND":
        mdt.write(l+"\n")
        mdpt += 1
        flag = 0
    elif flag == 1:
        mdt.write(l+"\n")
        temp = str(l).split()
        mnt.write(temp[0]+" "+str(mdpt)+"\n")
        ala = str(temp[1]).split(",")
        mdpt += 1
        flag += 1
    elif flag > 1:
        temp = str(l).split()
        part2 = str(temp[1]).split(",")
        mdt.write(temp[0]+" ")
        for i in part2:
            for j in range(len(ala)):
                t = str(ala[j]).split("=")
                if t[0] == i:
                    mdt.write("#"+str(j)+",")
        mdt.write("\n")
        mdpt += 1
    else:
        ic.write(line)
ic.close()
mnt.close()
mdt.close()