test_list = ['gfg', 'is', 'best1234']
 
# printing original list
print("The original list : " + str(test_list))
 
# Convert String list to ascii values
# using loop + ord()
res = []
for ele in test_list:
    res.extend(ord(num) for num in ele)
 
# printing result
print("The ascii list is : " + str(res))