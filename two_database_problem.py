serv1=[11,12,13,14,15]
serv2=[11,12,13,14,15]

query = int(input("Enter query for server 1: "))
str1 = list(bin(query)[2:])
change = int(input("Enter CHANGE index: "))

str2=[]
for i in range(len(str1)):
    if i == change:
        str2.append('1' if str1[i] == '0' else '0')
    else:
        str2.append(str1[i])

sum1 = 0
sum2 = 0
for i in range(len(str1)):
    sum1 ^= int(str1[i]) * serv1[i]
    sum2 ^= int(str2[i]) * serv2[i]

res = sum1 ^ sum2
print("Result:", res)

with open("log_two_database_problem.txt", "a") as f:
    f.write("New Entry \n")
    f.write("Server Data: "+ str(serv1) + "\n")
    f.write("Query Input: " + str(query) + "\n")
    f.write("Binary (str1): " + "".join(str1) + "\n")
    f.write("Change Index: " + str(change) + "\n")
    f.write("Modified Binary (str2): " + "".join(str2) + "\n")
    f.write("Sum1: " + str(sum1) + "\n")
    f.write("Sum2: " + str(sum2) + "\n")
    f.write("Result: " + str(res) + "\n")
