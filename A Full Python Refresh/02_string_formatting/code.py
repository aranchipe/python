# Uma string f permite colocar variaveis no meio da sring
name = "Sofia"
greeting = f"Hello {name}"

print(greeting)

name2 = "Lucas"
greeting2 = "hello, {}"
with_name = greeting2.format(name2)

print(greeting2)
print(with_name)
