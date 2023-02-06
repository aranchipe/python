# lists
l = ["Bob", "Rolf", "Anne"]
l[0] = "Lucas"
l.append("Pedro")
l.remove("Pedro")
# __________________________________________________________________________________________
# tuples
# não pode modificar uma tupla, adicionar ou remover elementos
t = ("Bob", "Rolf", "Anne")
# t[0] = "Lucas"  # não podemos fazer isso
# t.append("Lucas")  # não podemos fazer isso
# __________________________________________________________________________________________
# sets (conjuntos)
# pode modificar o set mas não pode ter o mesmo valor duas vezes
# o set não mantém a ordem que foi criado
s = {"Bob", "Rolf", "Anne"}
s.add("Lucas")

print(l)
print(t)
print(s)
