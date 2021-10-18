exp = [2340,4556,5567,3544]
#total = exp[0]+exp[1]+exp[2]+exp[3]
#print(total)

total = 0
for item in exp:
    total = total + item
print(total)

#Same problem using the range len

exp = [2340,4556,5567,3544]
total = 0
for i in range (len(exp)):
    print('Month:',(i+1),'expense:',exp[i])
    total = total+exp[i]
print('total expense is :',total)




