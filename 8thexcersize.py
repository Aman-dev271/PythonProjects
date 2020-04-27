import random
Usar_Name = input("Enter Your Name\n")

def game():
    computer_choice = ['snake' , 'water' , 'gun']
    rain =random.choice(computer_choice)
    user_choice = input("choose One of these 1.Snake 2.Water 3.Gun\n")
    comp_win_list = []
    user_win_list = []
    
    print("you selecet the ", user_choice)
    if rain == 'snake' and user_choice == 'gun':
        print("computer choos ",rain)
        print("Snake mar gya")
        print(Usar_Name,"is winner you choose :",user_choice)
        val = 1
        user_win_list.append(val)
        
        print("Win! ",Usar_Name)
    elif rain == 'water' and  user_choice == 'gun':
        print(rain)
        print("gun pani mai doob gee")
        print("computer is winner")
        print(Usar_Name , "is choose:",user_choice,"so user is looser")
        val = 1
        comp_win_list.append(val)
       
        print("Win! computer ")
        
    elif rain == 'gun' and  user_choice == 'gun':
        print("computer choos ",rain)
        print("draw")
        print("computer and ",Usar_Name ,"is same so this is Draw")
        
        val = 1
        
        user_win_list.append(val)
        
        comp_win_list.append(val)
        
    elif rain == 'snake' and user_choice == 'snake':
        print("computer choos ",rain)
        print("draw")
        print("computer and ",Usar_Name ,"is same so this is Draw")
        val = 1
        
        user_win_list.append(val)
        
        comp_win_list.append(val)
    elif rain == 'water' and  user_choice == 'snake':
        print("computer choose ",rain)
        print("snake ne pani pee liya ")
        print(Usar_Name,"is Won!")
        print("computer looser")
        val = 1
        user_win_list.append(val)
        print("Win! ",Usar_Name)
    elif rain == 'gun' and  user_choice == 'snake':
        print("computer choos ",rain)
        print("snake ko gun  ne mar diya")
        print("computer  is  Won!")
        print(Usar_Name,"is looser")
        val = 1
        comp_win_list.append(val)
        print("Win! computer")
    elif rain == 'snake' and user_choice == 'water':
        print("computer choos ",rain)
        print("snake ne pani pee liya ")
        print("computer is Winner!")
        print(Usar_Name,"is looser")
        val = 1
        comp_win_list.append(val)
        print("Win! computer")
    elif rain == 'water' and  user_choice == 'water':
        print("computer choos ",rain)
        print("Draw")
        print("computer and ",Usar_Name ,"is same so this is Draw")
        val = 1
        user_win_list.append(val)
        comp_win_list.append(val)


    elif rain == 'gun' and  user_choice == 'water':
        print("computer choos ",rain)
        print("gun pani mai doob gyee")
        print(Usar_Name,"is  Winner!")
        print("computer is looser")
        val = 1
        user_win_list.append(val)
        print("Win! ",Usar_Name)

i = 0
while i < 9:
    game()
    i = i+1
