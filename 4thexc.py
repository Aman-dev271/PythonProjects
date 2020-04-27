s= [2,3,4,5,'amandeep',333,444,55,666,77788,77,80,12,1,23]
list1 = []

for item in s:
    if type(item) == int and item > 6:
        print("your add the" ,',', item ,',',"value in the list")
        list1.append(item)
        
    else:
        print("not can't be add")

print("your new list is :" ,list1)
for i in list1:
    if i > 333:
        print(i)
    else:
        print("it is not possible")  


