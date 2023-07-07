list1 = [2,5,3,10,20,14,17]
n = len(list1)

for i in range(n):
    for j in range(i+1,n):
        if list1[j]<list1[i]:
            list1[i],list1[j] = list1[j],list1[i]

print(list1)
