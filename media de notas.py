print("=== BOLETIM DE NOTAS ===")
#NOME#
while True:
        nome = input("\nInsira seu nome: ")
        if nome != "":
            break
        else:
            print("Voce precisar digitar seu nome!")

#CURSOS#
while True:
    print("\n=== CURSOS ===")
    print("\n1.Engenharia de Software")

    curso = input("\nDigite o número do seu curso: ")

    if curso == "1":
        curso = "Engenharia de Software"
        break
    else:
        print("Opção Inválida")

#SEMESTRES#
while True: 
    print("\n=== SEMESTRES ===")
    print("1. semestre")
    print("2. semestre")
    print("3. semestre")
    print("4. semestre")
    print("5. semestre")
    print("6. semestre")
    print("7. semestre")
    print("8. semestre")
    semestre = input("\nInsira seu semestre: ")

    if semestre == "1":
        semestre = "1. semestre"
        break
    elif semestre == "2":
        semestre = "2. semestre"
        break
    elif semestre == "3":
        semestre = "3. semestre"
        break    
    elif semestre == "4":
        semestre = "4. semestre"
        break
    elif semestre == "5":
        semestre = "5. semestre"
        break
    elif semestre == "6":
        semestre = "6. semestre"
        break
    elif semestre == "7":
        semestre = "7. semestre"
        break
    elif semestre == "8":
        semestre = "8. semestre"
        break
else:
    print("Opção Inválida")

#DISCIPLINAS#
while True:
    print("\n=== SUAS DISCIPLINAS ===")
    print("\n1.Matemática Aplicada à Computação")
    print("\n2.Redes de Computadores")
    print("\n3.Arquitetura e Fundamentos de Computadores")
    print("\n4.Projeto de Vida")
    disciplina = input("\nInsira sua disciplina: ")

    if disciplina == "1":
        disciplina = "Matemática Aplicada à Computação"
        break
    elif disciplina == "2":
        disciplina = "Redes de Computadores"
        break
    elif disciplina == "3":
        disciplina = "Arquitetura e Fundamentos de Computadores"
        break
    elif disciplina == "4":
        disciplina = "Projeto de Vida"
        break
    else:
        print("Opção Inválida")

###NOTAS### 

#nota1
while True:
    try:
        nota1 = float(input("\ninsira sua primeira nota: "))
        if 0 <= nota1 <=100:
            break
        else: print("A nota deve estar entre 0 e 100")
    except ValueError:
        print("Digite uma nota válida!")
#nota2
while True:
    try:
        nota2 = float(input("\ninsira sua primeira nota: "))
        if 0 <= nota2 <=100:
            break
        else:
            print("A nota deve estar entre 0 e 100")
    except ValueError:
        print("Opção válida!")


#BOLETIM GERAL#
media = (nota1 + nota2)/2
print("\nAluno:", nome)
print("===================")
print("Curso:", curso)
print("===================")
print("Semestre:", semestre)
print("===================")
print("Disciplina:", disciplina)
print("===================")
print("=BOLETIM DE NOTAS=")
print("===================")
print("=  Nota 1 :", nota1)
print("=  Nota 2 :", nota2)
print("=  Média  :", media)
print("===================")
if media >= 60:
    print("APROVADO!")
elif media > 20:
    print("RECUPERAÇÃO!")
else:
    print("REPROVADO!")


