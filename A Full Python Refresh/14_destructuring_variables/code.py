x, y = 5, 11

print(x)
print(y)

student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}
print(list(student_attendance.items()))

for student, attendance in student_attendance.items(): #ultima aula
    print(f"{student}: {attendance}")


people = [
    {
        "nome": "Bob",
        "idade": 25,
        "profissao": "medico"
    },
    {
        "nome": "Pedro",
        "idade": 27,
        "profissao": "professor"
    },
    {
        "nome": "Joao",
        "idade": 30,
        "profissao": "pintor"
    }
]

for pessoa in people:
    for prop, val in pessoa.items():
        print(f"{prop}: {val}")


person = ("Bob", 42, "Mechanic")
nome, _, profissao = person

print(nome, profissao)


_, head, *tail = [1,2,3,4,5] # pega todos os elementos menos o especificado
print(head) #2
print(tail) # [3, 4, 5]