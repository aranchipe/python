movies_watched = {"matrix", "godfather", "mib"}
user_movie = input("Digite um filme que voce assistiu: ").lower()

if user_movie in movies_watched:
    print(f"I watched {user_movie} too")
else: 
    print(f"I have not watched {user_movie}")