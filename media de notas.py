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

if semestre == "1. semestre":

    while True:
        print("\n=== DISCIPLINAS DO PRIMEIRO SEMESTRE ===")
        print("1. Matemática Aplicada à Computação")
        print("2. Redes de Computadores")
        print("3. Arquitetura e Fundamentos de Computadores")
        print("4. Projeto de Vida")

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

elif semestre == "2. semestre":

    while True:
        print("\n=== DISCIPLINAS DO SEGUNDO SEMESTRE ===")
        print("1. Algoritmos e Lógica de Programação")
        print("2. Engenharia de Software")
        print("3. Produção do Conhecimento Científico, Tecnológico e Disrupção")
        print("4. Linguagens e Técnicas de Programção")

        disciplina = input("\ninsira sua disciplina")

        if disciplina == "1":
            disciplina = "Algoritmos e Lógica de Programação"
            break
        elif disciplina == "2":
            disciplina = "Engenharia de Software"
            break
        elif disciplina == "3":
            disciplina = "Produção do Conhecimento Científico, Tecnológico e Disrupção"
            break
        elif disciplina == "4":
            disciplina = "Linguagens e Técnicas de Programção"
            break
        else: 
            print("Opção Inválida")

elif semestre == "3. semestre":
    
    while True:
        print("\n===DISCIPLINAS DO TERCEIRO SEMESTRE")
        print("1. Análise e Projeto Orientado a Objetos")
        print("2. Estrutura de Dados")
        print("3. Mentalidade Criativa e Empreendedora")
        print("4. Programação Front End")

        disciplina = input("\nInsira sua disciplina")

        if disciplina == "1":
            disciplina = "Análise e Projeto Orientado a Objetos"
        elif disciplina == "2":
            disciplina = "Estrutura de Dados"
        elif disciplina== "3":
            disciplina = "Mentalidade Criativa e Empreendedora"
        elif disciplina == "4":
            disciplina = "Programação Front End"
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
#media+situação#
media = (nota1 + nota2)/2
if media >= 60:
    situação = "APROVADO!"
elif media > 20: 
    situação = "RECUPERAÇÃO!"
else:
    situação = "REPROVADO!"

#BOLETIM GERAL#

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
print("Situação  :", situação)

if situação == "APROVADO!":
    print(f"\nParabéns, {nome} Voce passou!")
elif situação == "RECUPERAÇÃO!":
        print(f"\nInfelizmente {nome}, Terá que fazer a recuperação")
else: 
        print(f"\n{nome}... voce está reprovado, tente novamente quando possível")
