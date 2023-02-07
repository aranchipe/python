lucas = {"idade": 25, "peso": 75, "email": "aranchipe98@gmail.com"} #objetos


print(lucas["email"])  #nao utiliza ponto para acessar a propriedade

lucas["cpf"] = "07798817530"
print(lucas)


friends = [
    {
        "nome": "Pedro",
        "idade": 14,
    },
    {
        "nome": "Jose",
        "idade": 24,
    },
    {
        "nome": "Joao",
        "idade": 22,
    },
    {
        "nome": "Gustavo",
        "idade": 25,
    },
]

print(friends[0]["nome"])



#______________________________________________________

student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}


for student in student_attendance:
    print(f"{student}: {student_attendance[student]}")

    # ou

for student, attendance in student_attendance.items(): # retorna todos os items do objeo
                                                       # propriedades e valores
    print(f"{student}: {attendance}")

attendance_values = student_attendance.values() # retorna os valores do objeto
print(sum(attendance_values)/len(attendance_values))



