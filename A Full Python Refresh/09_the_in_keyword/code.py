friends = ["Rolf", "Bob", "Jen"]
print("Jen" in friends) #true

friends2 = ("Rolf", "Bob", "Jen")
print("Jen" in friends2) #true

friends3 = {"Rolf", "Bob", "Jen"}
print("Jen" in friends3) #true

movies_watched = {"Matrix", "Godfather", "MIB"}
user_movie = input("Digite um filme que voce assistiu: ")

print(user_movie in movies_watched)
