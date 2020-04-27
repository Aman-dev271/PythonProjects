# # 0 1 2 3 5 8 13 21 34
# a = 0 
# b = 1
# c = a+b
# print(c)
# e = b+c
# print(e)
# f = e+c
# print(f)
# g = e+f
# print(g)
# def fibonacci(n):
#     if n == 0:
#         return  0
#     elif n == 1:
#         return 1
#     else :
#         return fibonacci(n-1)+fibonacci(n-2)
# number = int(input("enter the"))
# print(fibonacci(number))




# # Program to display the Fibonacci sequence up to n-th term

# nterms = int(input("How many terms? "))

# # first two terms
# n1, n2 = 0, 1
# count = 0

# # check if the number of terms is valid
# if nterms <= 0:
#    print("Please enter a positive integer")
# elif nterms == 1:
#    print("Fibonacci sequence upto",nterms,":")
#    print(n1)
# else:
#    print("Fibonacci sequence:")
#    while count < nterms:
#        print(n1)
#        nth = n1 + n2
#        # update values
#        n1 = n2
#        n2 = nth
#        count += 1









input_number = int(input("enter the number "))
n1 = 0
n2 = 1
c = 0
if input_number<=0:
    print("plese enter the positive integer")
elif input_number == 1:
    print("your answer is = ",input_number)
    print(n1)
else:
    while c < input_number:
        print(n1 ,end=",")
        nth  = n1 +n2
        # update the value
        n1 = n2
        n2 = nth
        c +=1