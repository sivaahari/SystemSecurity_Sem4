serv=[]
size=int(input("Enter the size of database: "))

for i in range(size):
    serv.append(int(input()))

m=int(input("Enter a PRIME number: "))

qr=[]
nqr=[]

for i in range(1,m):
    if pow(i,(m-1)//2,m)==1:
        qr.append(i)
    else:
        nqr.append(i)

query=[]
for i in range(0,size):
    query.append(int(input()))

res=[]
prod=0
for i in range(size):
    res.append(query[i]**serv[i])
    prod*=res[i]

if prod%m in qr:
    print("The bit is 0")
else:
    print("The bit is 1")    
