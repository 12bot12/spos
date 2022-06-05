f3=open('MNT.txt','w')
f3.write('{}{}{}{}{}{}'.format('MNTC','\t','MacroName','\t','MDTC','\n'))
f2=open('raw_MDT.txt','w')
f2.write('MDTC'+'\t'+'MacroInstruction\n')
f6=open('MDT.txt','w')
f6.write('MDTC'+'\t'+'MacroInstruction\n')
f4=open('ALA.txt','w')
f4.write('ALA_Index'+'\t'+'Argument\n')
f2.close()
f3.close()
f4.close()
f6.close()
with open('macro.txt') as f1:
    MDT_pt=0
    MNT_pt=0
    ALA_pt=0
    Argument_l=[]
    while True:
        line=f1.readline()
        if(line==''):
            break
        if('MACRO' in line):
            is_macro=1
            continue
        if(is_macro==1):
            is_macro=0
            with open('MNT.txt','a') as f3:
                words=line.strip('\n').split(' ')
                f3.write('{}{}{}{}{}{}'.format(MNT_pt,'\t',words[0],'\t\t',MDT_pt,'\n'))
                MNT_pt+=1
                for i in range(1,len(words)):
                        Argument_l.append(words[i][1])
                with open('raw_MDT.txt','a') as f2:
                    while 'MEND' not in line:
                        f2.write('{}{}{}'.format(MDT_pt,'\t',line))
                        MDT_pt+=1
                        line=f1.readline()
                    f2.write(str(MDT_pt)+'\t'+'MEND\n')
                    MDT_pt+=1
            continue
        words=line.strip('\n').split(' ')
        f3=open('MNT.txt')
        data=f3.read()
        f3.close()
        if(words[0] in data):
            f5=open('output.txt','a')
            f5.write(line)
            f5.close()
            with open('ALA.txt','a') as f4:
                for i in range(1,len(words)):
                    f4.write('{}{}{}{}'.format(ALA_pt,'\t\t',words[i],'\n'))
                    ALA_pt+=1
            with open('MDT.txt') as f6:
                data1=f6.read()
            if(words[0] in data1):
                break
            with open('raw_MDT.txt') as f2:
                while True:
                    line=f2.readline()
                    if(line==''):
                        break
                    else:
                        words=line.strip('\n').split(' ')
                        if(len(words)>1 and '&' in words[2]):
                            l=[]
                            for i in range(len(words)):
                                if(words[i][0]=='&'):
                                    indx=Argument_l.index(words[i][1])
                                    l.append('#{}'.format(indx))
                                else:
                                    l.append(words[i])
                            data=' '.join(l)
                            with open('MDT.txt','a') as f6:
                                f6.write('{}{}'.format(data,'\n'))  
                        else:
                            words=line.strip('\n').split('\t')
                            if(words[1]=='MEND'):
                                with open('MDT.txt','a') as f6:
                                    f6.write('{}'.format(line))
                            continue
            