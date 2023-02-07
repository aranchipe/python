x = 5 == 5 # true
print(x)

x = "5" == 5 #false (diferente do js)
print(x)

y = 5 != 5
print(y) # false

friends = ["Rolf", "Bob"]
abroad = ["Rolf", "Bob"]

print (friends == abroad) #true
print (friends is abroad) #false #apesar de terem os mesmos elementos, 
                                 #sao duas variaveis diferentes
                                 # nao se usa

abroad = friends
print (abroad is friends) #true

