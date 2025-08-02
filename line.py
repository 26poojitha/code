Idel=input("enter exact line:")
with open('log.txt','r') as f:
    lines=f.readlines()
with open('log.txt','w') as f:
    for line in lines:
        if line.strip()!=Idel.strip():
            f.write(line)