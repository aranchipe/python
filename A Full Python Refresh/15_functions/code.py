def hello(): 
    print("Hello")

def user_age_in_seconds():
    user_age = int(input("Digite sua idade: "))
    age_seconds = user_age * 365 * 24 * 60 * 60
    print(f"Sua idade em segundos e de: {age_seconds} segundos")

hello()
user_age_in_seconds()
