one= int(input("How many Row you want to print"))
two = int(input("Type 1 or 0"))
new  = bool(two)
if new == True:
    for i in range(1,one+1):
        for j in range(1, i+1):
            print("*" ,end= " ")
        print()
elif new == False:
    for i in range(one , 0,-1):
        for j in range(1,i+1):
            print("*" , end="")
        print()
