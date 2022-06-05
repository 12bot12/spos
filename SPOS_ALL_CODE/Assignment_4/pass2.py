f = open("pass1_output.txt","r")
out = open("pass2_output.txt","a+")
out.truncate(0)

mdtf = open("mdt.txt","r")
mntf = open("mnt.txt","r")

words = []
MDT = []
MNT = []
ALA = []
ALAC = 1

for line in mdtf:
    MDT.append(line.split())

for line in mntf:
    MNT.append(line.split())

def mdt_lines(MDTP):
    for x in MDT:
        if MDTP == int(x[0]):
            if "MEND" in x:
                break
            else:
                lines = "\t"
                for i in range(1, len(x)):
                    lines = lines + x[i] + " "
                    for j in ALA:
                        if str(j[0]) in lines:
                            lines = lines.replace(x[3], j[1])
                out.write(lines + "\n")
                MDTP += 1

for line in f:
    line = line.replace(",","")
    words = line.split()
    for i in MNT:
        if words[0] in i[1]:
            MDTC = int(i[2])
            for j in range(1, len(words)):
                ALA.append([ALAC, words[j]])
                ALAC += 1
            MDTC += 1
            mdt_lines(MDTC)
            line = ""
    out.write(line)

alatab = open("pass2_ala.txt","w")
for x in ALA:
    alatab.write(str(x[0]) + "\t" + str(x[1]) + "\n")

f.close()
out.close()
mdtf.close()
mntf.close()
alatab.close()