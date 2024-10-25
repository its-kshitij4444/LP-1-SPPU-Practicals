import os

# Define paths to files
opfile = os.path.join('.', '2b macro pass 2', 'OUTPUT.txt')
icfile = os.path.join('.', '2a macro pass 1', 'IC.txt')
mdtfile = os.path.join('.', '2a macro pass 1', 'MDT.txt')
mntfile = os.path.join('.', '2a macro pass 1', 'MNT.txt')

# Read input files
with open(icfile, "r") as ic, open(mntfile, "r") as mnt, open(mdtfile, "r") as mdt:
    ic_lines = ic.readlines()
    mnt_lines = mnt.readlines()
    mdt_lines = mdt.readlines()

# Open output file
with open(opfile, "w") as output:
    # Iterate over each line in the intermediate code (IC)
    for line in ic_lines:
        flag = 0
        temp = str(line).strip().split()
        
        # Check if the current line matches any macro name in the MNT
        for mnt_line in mnt_lines:
            t = str(mnt_line).strip().split()
            if t[0] == temp[0]:  # Macro call found
                flag = 1
                mdpt = int(t[1])  # Starting index for MDT expansion
                break
        
        if flag == 1:
            # Parse arguments from IC line
            ala = str(temp[1]).split(",") if len(temp) > 1 else []
            
            # Collect MDT lines corresponding to the macro definition
            macro_body = []
            for line_idx in range(mdpt, len(mdt_lines)):
                st = str(mdt_lines[line_idx]).strip()
                if st == "MEND":
                    break
                macro_body.append(st)
            
            # Parse the macro definition arguments from MDT's first line
            if macro_body:
                mdt_args = macro_body[0].split()[1].split(",")

            # Process and expand each line in the macro definition
            for item in macro_body:
                instr_parts = item.split()
                if instr_parts[0] != "MEND":
                    # Replace parameters in the instruction
                    instruction = instr_parts[0]
                    operands = instr_parts[1].split(",") if len(instr_parts) > 1 else []
                    expanded_operands = []
                    
                    for op in operands:
                        if op.startswith("#"):
                            idx = int(op[1:])  # Index of the parameter
                            if idx < len(ala):
                                # Substitute with actual argument or default value
                                expanded_operands.append(ala[idx])
                            elif "=" in mdt_args[idx]:  # Default value in MDT
                                expanded_operands.append(mdt_args[idx].split("=")[1])
                        else:
                            expanded_operands.append(op)
                    
                    # Write the expanded instruction line to the output file
                    output.write(f"{instruction} {','.join(expanded_operands)}\n")
        else:
            # Write non-macro lines directly to the output
            output.write(line)
