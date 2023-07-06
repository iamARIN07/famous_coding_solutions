# sort by values
dict1 = {433: 'apple',
         156: 'mango',
         789: 'orange',
         500: 'chillis'}

dict2 = {key:value for key,value in sorted(dict1.items(), key=lambda x: x[1])}
print(dict2)

# sort by key
dict3 = {433: 'apple',
         156: 'mango',
         789: 'orange',
         500: 'chillis'}

sorted_dict3 = sorted(dict3)
dict4 = {}

for i in sorted_dict3:
    dict4[i] = dict3[i]

print(dict4)


