lst = [8,7,2,5,3,1]
find_sum = 10

n = len(lst)
for i in range(n):
    for j in range(i+1,n):
        if lst[i] + lst[j] == find_sum:
            print(lst[i],lst[j])
