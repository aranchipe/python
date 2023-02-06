# sempre retorna uma string
name = input("Digite seu nome: ")

velocidade_input = input("A quantos km/h você está dirigindo: ")
velocidade_int = int(velocidade_input)
ms = velocidade_int / 3.6
print(f"{name}, você está a {ms:.3f} m/s")  # numero de casas decimais (3)
