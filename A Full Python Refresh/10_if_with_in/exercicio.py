number = 7

user_input = input("Digite 'y' se quiser jogar: ")

if user_input == "y":
    user_number = int(input("Digite um numero: "))
    if user_number == number:
        print("Parabens, voce acertou")
    elif abs(user_number - number) == 1:
        print("Voce errou por um")
    else: 
        print("Desculpa voce errou")