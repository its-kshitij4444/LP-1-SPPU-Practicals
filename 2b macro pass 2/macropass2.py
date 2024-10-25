import os

# Define paths to files
opfile = os.path.join('.', '2b macro pass 2', 'OUTPUT.txt')
icfile = os.path.join('.', '2a macro pass 1', 'IC.txt')
mdtfile = os.path.join('.', '2a macro pass 1', 'MDT.txt')
mntfile = os.path.join('.', '2a macro pass 1', 'MNT.txt')

# Read input files
with open(icfile, "r") as ic, open(mntfile, "r") as mnt, open(mdtfile, "r") as mdt:
    i = ic.readlines()
    n = mnt.readlines()
    m = mdt.readlines()

# Open output file
with open(opfile, "w") as f:
    # Iterate over each line in the intermediate code (IC)
    for line in i:
        flag = 0
        temp = str(line).strip().split()
        
        # Check if the current line matches any macro name in the MNT
        for mnt_line in n:
            t = str(mnt_line).strip().split()
            if t[0] == temp[0]:
                flag = 1
                mdpt = int(t[1])
                break
        
        if flag == 1:
            # Parse arguments from IC line
            ala = str(temp[1]).split(",") if len(temp) > 1 else []
            flag += 1
            
        if flag > 1:
            # Collect MDT lines corresponding to the macro definition
            lis = []
            for line_idx in range(mdpt, len(m)):
                st = str(m[line_idx]).strip()
                if st == "MEND":
                    break
                lis.append(st)
            
            # Parse the macro definition arguments from MDT
            ala2 = []
            for item_idx, item in enumerate(lis):
                tmp = str(item).split()
                if item_idx == 0:
                    ala2 = str(tmp[1]).split(",")
                
                if item_idx > 0:
                    # Write the macro instruction name
                    f.write(tmp[0] + " ")
                
                # Substitute parameters with actual arguments
                tmp_args = str(tmp[1]).split(",")
                buffer = ""
                
                for k in tmp_args:
                    for ii, arg in enumerate(ala2):
                        if k == f"#{ii}":
                            # Substitute arguments, handle default values
                            if len(ala) <= ii:
                                default_value = ala2[ii].split("=")[1] if "=" in ala2[ii] else ""
                                buffer += default_value + ","
                            else:
                                buffer += ala[ii] + ","
                
                if item_idx > 0:
                    f.write(buffer.rstrip(",") + "\n")
        elif flag == 0:
            # Write non-macro lines directly
            f.write(line)