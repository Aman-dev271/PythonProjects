nm1 = int(input("enter the first number"))
nm2 = int(input("enter the 2nd number"))
choose  = input("select the operator that you want to choose : -,+,*,/")
if nm1 == 45 and nm2 ==3 and choose == '*':
    print("your answer is:"'555')
elif nm1 == 56 and nm2 == 9 and choose == '+':
    print("your answer is:" '77')
elif nm1 == 56 and nm2 == 6 and choose == "/":
    print("your answer is : "' 4')
elif choose == '+':
    print("your answer is:", nm1+nm2)
elif choose == '-':
    print("your answer is:", nm1-nm2)
elif choose == '*':
    print("your answer is:" ,nm1*nm2)
elif choose == '/':
    print("your answer is:",nm1/nm2)
