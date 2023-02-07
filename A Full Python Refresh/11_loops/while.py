#number = 7

#user_input = input("Voce quer jogar? y/n ")
    
#while user_input != "n":
    
#    user_number = int(input("Digite um numero: "))
#    if user_number == number:
#        print("Parabens, voce acertou")
#    elif abs(user_number - number) == 1:
#        print("Voce errou por um")
#    else: 
#        print("Desculpa voce errou")

#    user_input = input("Voce quer jogar? y/n ")
#_________________________________________________________________
    
number = 7

    
while True:
    user_input = input("Voce quer jogar? y/n ")

    if user_input == "n":
        break
    
    user_number = int(input("Digite um numero: "))
    if user_number == number:
        print("Parabens, voce acertou")
    elif abs(user_number - number) == 1:
        print("Voce errou por um")
    else: 
        print("Desculpa voce errou")
