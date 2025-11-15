rows=int(input("Number of rows: "))
cols=int(input("Number of columns: "))
serv1=[]
for i in range(rows):
    row=[]
    for j in range(cols):
        x=int(input())
        row.append(x)
    serv1.append(row)

print(serv1)

serv2=serv1
serv3=serv1
serv4=serv1

s1=list(bin(int(input("Enter query for server 1 (row): ")))[2:])
t1=list(bin(int(input("Enter query for server 1 (column): ")))[2:])
cs=int(input("Enter CHANGE index of row: "))
ct=int(input("Enter CHANGE index of column: "))
s2=[]
t2=[]

for i in range(len(s1)):
    if i==cs:
        s2.append('1' if s1[i]=='0' else '0')
    else:
        s2.append(s1[i])
    if i==ct:
        t2.append('1' if t1[i]=='0' else '0')
    else:
        t2.append(t1[i])

sum1=0
sum2=0
sum3=0
sum4=0

for i in range(len(s1)):
    for j in range(len(t1)):
        if s1[i]==t1[j] and s1[i]=='1':
            sum1^=serv1[i][j]
        if s2[i]==t1[j] and s2[i]=='1':
            sum2^=serv2[i][j]
        if s1[i]==t2[j] and s1[i]=='1':
            sum3^=serv3[i][j]
        if s2[i]==t2[j] and s2[i]=='1':
            sum4^=serv4[i][j]

res=sum1^sum2^sum3^sum4
print("Result: ",res)

with open("log_four_database_problem.txt","a") as f:
    f.write("New Entry:\n")
    f.write("Matrix:\n")
    for row in serv1:
        f.write(str(row)+"\n")
    f.write("Row Query: "+ "".join(s1) + "\n")
    f.write("Column Query: "+ "".join(t1) + "\n")
    f.write("Changed Row Index: "+ str(cs) + "\n")
    f.write("Changed Column Index: "+ str(ct) + "\n")
    f.write("Modified Row: "+ "".join(s2) + "\n")
    f.write("Modified Column: "+ "".join(t2) + "\n")
    f.write("Sum1: "+ str(sum1) + "\n")
    f.write("Sum2: "+ str(sum2) + "\n")
    f.write("Sum3: "+ str(sum3) + "\n")
    f.write("Sum4: "+ str(sum4) + "\n")
    f.write("Result: "+ str(res) + "\n")
