with open('input.txt', 'r') as f:
   a=f.readline()
   a=n.split()
for i in a:
    if ord(i) in range(65,91):
        nr=''
        with open('litereA.txt', 'w') as f:
            nr+=f.write(i)
    if ord(i) in range(48,58):
        nn=''
        with open('cifre.txt', 'w') as f:
            nn+=f.write(i)
    if (ord(i) in range(33,48)) or (ord(i) in range(58,64)) or (ord(i) in range(91,97)) or (ord(i) in range(123,127)):
        nc=''
        with open('operatori.txt', 'w') as f:
            nc+=f.write(i)
    if ord(i) in range(97,123):
        nm=''  
          with open('litereB.txt', 'w') as f:
              nm+=f.write(i)
