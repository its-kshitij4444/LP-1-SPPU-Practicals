# Import necessary module
import os
import re
from collections import defaultdict

pattern = r'[(),]'
cwd = os.getcwd()
# Construct the relative path to the text file in "pass 1 assembler"
ic_file = os.path.join('.', '1a pass 1', 'inter_code.txt')
sym_file = os.path.join('.', '1a pass 1', 'SymTab.txt')
pool_file = os.path.join('.', '1a pass 1', 'PoolTab.txt')
lit_file = os.path.join('.', '1a pass 1', 'literals.txt')

lit_tab = [['' for _ in range(2)] for _ in range(10)]
sym_tab = defaultdict(str)

with open(lit_file, 'r') as file:
    z = 0
    for line in file:
        if line.strip():  # Ensure the line is not empty
            parts = line.strip().split('\t')
            if len(parts) >= 2:
                lit_tab[z][0] = parts[0]
                lit_tab[z][1] = parts[1]
                z += 1

with open(sym_file, 'r') as file:
    for line in file:
        if line.strip():  # Ensure the line is not empty
            parts = line.strip().split('\t')
            if len(parts) >= 2:
                sym_tab[parts[0]] = parts[1]

pool_tab = []
with open(pool_file, 'r') as file:
    for line in file:
        if line.strip():  # Ensure the line is not empty
            pool_tab.append(int(line.strip()))

pool_tab_ptr = 1
temp1 = pool_tab[0]
temp2 = pool_tab[1]

mc_file = os.path.join(cwd, '1b pass 2', 'machine_code.txt')

ic_file_path = open(ic_file, 'r')
current_line = ic_file_path.readline()
ic_file_path.close()

part = re.split(pattern, current_line)
loc_ctr = int(part[-2])

with open(ic_file, 'r') as ic, open(lit_file, 'r') as lit, open(mc_file, 'w') as mc:
    next(ic)
    for sCurrentLine in ic:
        result = re.split(pattern, sCurrentLine)
        mc.write(f"{loc_ctr}\t")
        parts = [item.strip() for item in result if item.strip()][1:]
        # print(parts)
        s0 = parts[0]
        s1 = parts[1]

        if s0 == "IS":
            mc.write(f"{s1}\t")
            if len(parts) == 6:
                mc.write(f"{parts[3]}\t")
                if parts[-2] == "L":
                    position = int(parts[-1])
                    mc.write(f"{lit_tab[position - 1][1]}")
                if parts[-2] == "S":
                    add1 = int(parts[-1])
                    for i, (key, value) in enumerate(sym_tab.items(), start=1):
                        if i == add1:
                            mc.write(f"{value}")
                            break
            else:
                mc.write("0\t000")

        if s0 == "AD":

            if s1 == "05":
                # Reset lit pointer (Python does not have reset, so re-open the file)
                lit.seek(0)
                j = 1
                while j < temp1:
                    lit.readline()
                    j += 1

                while temp1 < temp2:
                    line = lit.readline().strip()
                    # print(line)
                    if line:
                        mc.write(f"00\t0\t00{line.split('\'')[1]}")
                    if temp1 < (temp2 - 1):
                        loc_ctr += 1
                        mc.write("\n")
                        mc.write(f"{loc_ctr}\t")
                    temp1 += 1

                temp1 = temp2
                pool_tab_ptr += 1
                if pool_tab_ptr < len(pool_tab):
                    temp2 = pool_tab[pool_tab_ptr]

            if s1 == "02":
                j = 1
                for s in lit:
                    s = s.strip()
                    # print(s.split('\''))
                    if j >= temp1:
                        mc.write(f"00\t0\t00{s.split('\'')[1]}")
                    j += 1

        if s0 == "DL" and s1 == "01":
            res = re.split(pattern, sCurrentLine)
            mc.write(f"00\t0\t00{res[-2]}")

        if s0 == "DL" and s1 == "02":
            mc.write(f"00\t0\t{loc_ctr}")

        loc_ctr += 1
        mc.write("\n")

with open(mc_file, 'r') as mc:
    for line in mc:
        print(line)
