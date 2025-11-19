rows=int(input("Number of rows: "))
cols=int(input("Number of columns: "))
serv1=[]
for i in range(rows):
    row=[int(input()) for j in range(cols)]
    serv1.append(row)

print("The matrix is:")
for row in serv1:
    print(row)

serv2=[r[:] for r in serv1]
serv3=[r[:] for r in serv1]
serv4=[r[:] for r in serv1]

s1=list(input("Enter query for server 1 (row): ").strip())
t1=list(input("Enter query for server 1 (column): ").strip())
cs=int(input("Enter CHANGE index of row: "))
ct=int(input("Enter CHANGE index of column: "))

if len(s1)<rows:
    s1=['0']*(rows-len(s1))+s1
else:
    s1=s1[-rows:]
if len(t1)<cols:
    t1=['0']*(cols-len(t1))+t1
else:
    t1=t1[-cols:]

s2=[]
for i in range(len(s1)):
    if i==cs:
        if s1[i]=='0':
            s2.append('1')
        else:
            s2.append('0')
    else:
        s2.append(s1[i])

t2=[]
for j in range(len(t1)):
    if j==ct:
        if t1[j]=='0':
            t2.append('1')
        else:
            t2.append('0')
    else:
        t2.append(t1[j])


sum1=sum2=sum3=sum4=0
for i in range(rows):
    for j in range(cols):
        if s1[i]=='1' and t1[j]=='1':
            sum1 ^= serv1[i][j]
        if s2[i]=='1' and t1[j]=='1':
            sum2 ^= serv2[i][j]
        if s1[i]=='1' and t2[j]=='1':
            sum3 ^= serv3[i][j]
        if s2[i]=='1' and t2[j]=='1':
            sum4 ^= serv4[i][j]

res = sum1 ^ sum2 ^ sum3 ^ sum4
print("Result:", res)
