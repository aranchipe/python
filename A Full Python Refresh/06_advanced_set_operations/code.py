friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

local_friends = friends.difference(abroad) # faz a diferenca dos conjuntos

print(local_friends)

set_vazio = set() # set vazio
set_vazio.add("Lucas")
print(set_vazio)

local = {"Rolf"}
abroad2 = {"Bob", "Anne"}

total = local.union(abroad2) # junta os dois conjuntos
print(total)

art = {"Bob", "Jen", "Rolf", "Charles"}
science = {"Bob", "Jen", "Adam", "Anne"}

both = art.intersection(science) # faz a intersecao
print(both)