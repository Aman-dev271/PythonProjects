n = 18
number_of_guesses = 1
print("nuber of guesses is limited to only 9 time :")
while(number_of_guesses<=9):
    guess_number = int(input("Enter the numbe "))
    if guess_number <18:
        print("you entered less number input greater number, \n")
    elif guess_number >18:
        print("ypu entered greater number plese enter smaller number")
    else:
        print("you won\n")
        print(number_of_guesses,"no of gyesses he took to finish ")
        break
    print(9-number_of_guesses,"no of gueses left")
    number_of_guesses = number_of_guesses+1
if (number_of_guesses >9):
    print("game over")
