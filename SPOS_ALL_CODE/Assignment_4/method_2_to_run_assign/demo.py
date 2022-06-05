import readline
import string
with open('Expanded_Source_Code.txt','w') as f4:
    f4.write('')
with open('ALA.txt') as f1:
                l=[]
                line=f1.readline()
                while True:
                    line=f1.readline()
                    if(line==''):
                        break
                    else:
                        data=line.strip('\n').split('\t\t')
                        for i in data:
                            l.append(i)
with open('output.txt') as f1:
    while(True):
        line=f1.readline()
        if line=='':
            break
        else:
            words=line.strip('\n').split(' ')
            with open('MNT.txt') as f2:
                data=f2.read()
            if(words[0] in data):
                with open('MDT.txt') as f3:
                    line1=f3.readline()
                    while words[0] not in line1:
                        line1=f3.readline()
                    while True:
                        if(line1==''):
                            break
                        else:
                            with open('Expanded_Source_Code.txt','a') as f4:
                                while 'MEND' not in line1:
                                    line1=line1.strip('\n').split(' ')
                                    new_line=[]
                                    for i in line1:
                                        if('\t' in i):
                                            i=i.split('\t')
                                            for j in i:
                                                new_line.append(j)
                                        else:
                                            new_line.append(i)
                                    new_line=new_line[1:]
                                    for j in range(1,len(new_line)):
                                        if(new_line[j][1] in l):
                                            indx=l.index(new_line[j][1])
                                            new_line[j]=l[indx+1]
                                    new_line.append('\n')
                                    new_line=' '.join(new_line)
                                    f4.write(new_line)
                                    line1=f3.readline()
                            break