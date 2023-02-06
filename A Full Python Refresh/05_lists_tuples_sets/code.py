# lists
l = ["Bob", "Rolf", "Anne"]
l[0] = "Lucas"  # podemos fazer isso
# tuples
# não pode modificar uma tupla, adicionar ou remover elementos

t = ("Bob", "Rolf", "Anne")
t[0] = "Lucas"  # não podemos fazer isso

# sets (conjuntos)
# pode modificar o set mas não pode ter o mesmo valor duas vezes
# o set não mantém a ordem que foi criado
s = {"Bob", "Rolf", "Anne", "Anne"}

print(l[0])
print(t)
print(s)
