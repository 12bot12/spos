mnemonics={
    'STOP':('00','IS',0),
    'ADD':('01','IS',2),
    'SUB':('02','IS',2),
    'MUL':('03','IS',2),
    'MOVER':('04','IS',2),
    'MOVEM':('05','IS',2),
    'COMP':('06','IS',2),
    'BC':('07','IS',2),
    'DIV':('08','IS',2),
    'READ':('09','IS',1),
    'PRINT':('10','IS',1),
    'LTORG':('05','AD',0),
    'ORIGIN':('03','AD',1),
    'START':('01','AD',1),
    'EQU':('04','AD',2),
    'DS':('01','DL',1),
    'DC':('02','DL',1),
    'END':('AD',0)
    }
REG={'AREG':1,'BREG':2,'CREG':3,'DREG':4} 

# open files
inputFile = open("input.txt",'r')
Mc_code = open("Inter_codes.txt","a+")

# variable declaration
LC = 0   #location Counter
words =[]
symtab ={}
littab ={}
litCount = 1
c=1


# function declarations 
def OTHERS(mnemonic,k):
    global words
    global mnemonics 
    global symtab
    global LC,symindex,litCount
    z=mnemonics[mnemonic]
    Mc_code.write("\t("+z[1]+","+z[0]+")\t")
    i=0
    y=z[-1]
    #print("y="+str(y))
    for i in range(1,y+1):
        words[k+i]=words[k+i].replace(",","")
        if(words[k+i] in REG.keys()):
            Mc_code.write("("+str(REG[words[k+i]])+")")
        elif("=" in words[k+i]):
            #print(words[k+i])
            littab[words[k+i]] = [litCount,words[k+i],"**"]
            #print(len(x))
            Mc_code.write("(L,"+str(litCount)+")")
            litCount+=1
        else:
            #print(words,symtab)
            if(words[k+i] not in symtab.keys()):
                symtab[words[k+i]]=(symindex,words[k+i],"**")
                Mc_code.write("(S,"+str(symindex)+")")
                symindex+=1
            else:
                w=symtab[words[k+i]]
                Mc_code.write("(S,"+str(w[-1])+")")
    #print(symtab)
    Mc_code.write("\n")
    LC+=1





def detect_mnemonic(k):
    global words,LC,c

    if words[k]=="START":
        LC=int(words[1])
        Mc_code.write("\t(AD,01)\t(C,"+str(LC)+')\n')
    elif words[k]=="DC":
        Mc_code.write("\t(DL,02)\t(C,"+words[k+1]+")\n")
        LC+=1
    elif words[k] == "DS":
        Mc_code.write("\t(DL,01)\t(C,"+words[k+1]+")\n")
        LC=LC+int(words[k+1])
    elif words[k]=="ORIGIN":
        Mc_code.write("\t(AD,03)\t(C,"+str(words[k+1])+")\n")
        LC =int(words[k+1])
    elif words[k] == "END":
         Mc_code.write("\t(AD,02) (c,"+str(c)+")\n")   
         c+=1
         for x in littab.values():
             if "**" in x[2]:
                 x[2]=LC
                 LC+=1

    else:
        OTHERS(words[k],k)  


# actual execution
symindex=0
for line in inputFile:
    # print(line)
    words = line.split()
    # print(words)
    if(LC > 0):
        Mc_code.write(str(LC))
        
    k=0
    # if first word is mnemonic
    if words[0] in mnemonics.keys():
        
        # print(val)
        k=0
        detect_mnemonic(k)
    # else it is a symbol
    else:
        # it is not present in symbol table then add it
        if words[0] not in symtab.keys():
            symtab[words[k]] = (symindex,words[k],LC)
            symindex+=1
            # symbol()  # to print symbol table

        # present in symbol table
        else:

             x=symtab[words[k]]
             if x[2]=="**":
                symtab[words[k]]=(x[0],x[1],LC)
            
        k=1
        detect_mnemonic(k)

l = open("littab.txt",'w')
s = open("symtab.txt",'w')

for x in symtab.values():
    s.write(str(x[0])+"\t  "+str(x[1])+"\t  "+str(x[2])+"\n")
for x in littab.values():
    l.write(str(x[0])+"\t  "+str(x[1])+"\t  "+str(x[2])+"\n")

l.close()
s.close()
print(symtab)
print(littab)
inputFile.close()
Mc_code.close()
def ORIGIN(addr):
    global LC
    ifp.write("\t(AD,03)\t(C,"+str(addr)+")\n")
    LC =int(addr)

#handles DS mnemonic
def DS(size):
    global LC
    ifp.write("\t(DL,01)\t(C,"+size+")\n")
    LC=LC+int(size)

#handles DC mnemonic
def DC(value):
    global LC
    ifp.write("\t(DL,02)\t(C,"+value+")\n")
    LC+=1
 #identifies type of operands i.e. registers, literals, symbols and add approprite data in intermediate code file, literal table and symbol table as well as pool table.   
def OTHERS(mnemonic,k):
    global words
    global mnemonics 
    global symtab
    global LC,symindex
    z=mnemonics[mnemonic]
    ifp.write("\t("+z[1]+","+z[0]+")\t")
    i=0
    y=z[-1]
    #print("y="+str(y))
    for i in range(1,y+1):
        words[k+i]=words[k+i].replace(",","")
        if(words[k+i] in REG.keys()):
            ifp.write("(RG,"+str(REG[words[k+i]])+")")
        elif("=" in words[k+i]):
            #print(words[k+i])
            lit.seek(0,2)
            lit.write(words[k+i]+"\t**\n")
            lit.seek(0,0)
            x=lit.readlines()
            #print(len(x))
            ifp.write("(L,"+str(len(x))+")")
        else:
            #print(words,symtab)
            if(words[k+i] not in symtab.keys()):
                symtab[words[k+i]]=("**",symindex)
                ifp.write("(S,"+str(symindex)+")")
                symindex+=1
            else:
                w=symtab[words[k+i]]
                ifp.write("(S,"+str(w[-1])+")")
    #print(symtab)
    ifp.write("\n")
    LC+=1
 
 #idenifies mnemonic and redirect to resepective function    
def detect_mn(k):
    global words,LC
    if(words[k]=="START"):
        LC=int(words[1])
        ifp.write("\t(AD,01)\t(C,"+str(LC)+')\n')
    elif(words[k]=='END'):
        END()
    elif(words[k]=="LTORG"):
       LTORG()
    elif(words[k]=="ORIGIN"):
       ORIGIN(words[k+1])
    elif(words[k]=="DS"):
        DS(words[k+1])
    elif(words[k]=="DC"):
        DC(words[k+1])
    #elif(words[k]=="EQU"):
        #EQU(words)
    else:
        OTHERS(words[k],k)
    littab()
    pooltab2()
    symbol()

#actual code execution starts from here
symindex=0
for line in file:
    #print(line)
    words=line.split()
    #print(words)
    if(LC>0):
        ifp.write(str(LC))
    print("LC=",LC)
    print(line)
    print(words)
    k=0
        
    if words[0] in mnemonics.keys():
        print("Mnemonic:",words[0])
        val=mnemonics[words[0]]
        k=0
        detect_mn(k)
    else:
        print("Label:",words[0],"Mnemonic:",words[1])
        if words[k] not in symtab.keys():
            symtab[words[k]]=(LC,symindex)
            #ifp.write("\t(S,"+str(symindex)+")\t")
            symindex+=1
            symbol()
        else:
            #print(words)
            x=symtab[words[k]]
            if x[0]=="**":
                print("yes")
                symtab[words[k]]=(LC,x[1])
            #ifp.write("\t(S,"+str(symindex)+")\t")
            symbol()
        k=1
        detect_mn(k)
#print(symtab)
#print(pooltab)
ifp.close()
lit.close()
tmp.close()
sym=open("SymTab.txt","a+")
sym.truncate(0)
for x in symtab:
    sym.write(x+"\t"+str(symtab[x][0])+"\n")
sym.close()
pool=open("PoolTab.txt","a+")
pool.truncate(0)
for x in pooltab:
    pool.write(str(x)+"\n")
pool.close()
if os.path.exists("tmp.txt")==True:
    os.remove("tmp.txt")
