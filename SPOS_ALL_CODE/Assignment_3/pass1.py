f = open("input.txt", "r")
out = open("pass1_output.txt", "a+")
out.truncate(0)

MDT = [] # Macro Definition Table
MNT = [] # Macro Name Table
ALA = [] # Argument List Array
words = []
MNTC = 1
MDTC = 1
ALAC = 1
MacroDefOn = False
macroname = 0

for line in f:
    if "MACRO" in line:
        MacroDefOn = True
        macroname = 1
    elif "MEND" in line:
        MDT.append([MDTC, line])
        MDTC += 1
        MacroDefOn = False
    elif MacroDefOn:
        if macroname == 1:
            MDT.append([MDTC, line])
            line = line.replace(",","")
            words = line.split()
            MNT.append([MNTC, words[0], MDTC])
            MNTC += 1
            for i in range(1,len(words)):
                words[i].replace(",","")
                ALA.append([ALAC,words[i]])
                ALAC += 1
            MDTC += 1
            macroname = 0
        else:
            for x in ALA:
                if x[1] in line:
                    line = line.replace(x[1],str(x[0]))
                    MDT.append([MDTC, line])
                    MDTC += 1
    else:
        out.write(line)

mdttab = open("mdt.txt","w")
mnttab = open("mnt.txt","w")
alatab = open("pass1_ala.txt","w")
for x in MDT:
    mdttab.write(str(x[0]) + "\t" + str(x[1]))
for x in MNT:
    mnttab.write(str(x[0]) + "\t" + str(x[1]) + "\t" + str(x[2]) + "\n")
for x in ALA:
    alatab.write(str(x[0]) + "\t" + str(x[1]) + "\n")

f.close()
out.close()
mdttab.close()
mnttab.close()
alatab.close()
