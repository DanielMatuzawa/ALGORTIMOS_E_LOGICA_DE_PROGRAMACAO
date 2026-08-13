print("===BOLETIM DE NOTAS===")

while True:
        nome = input("\nInsira seu nome: ")
        if nome != "":
            break
        else:
            print("Voce precisar digitar seu nome!")


curso = input("\nInsira seu curso: ")
disciplina = input("\nInsira sua disciplina: ")
semestre = input("\nInsira seu semestre: ")


###SISTEMAS DE NOTAS### 

while True:
    try:
        nota1 = int(input("\ninsira sua primeira nota: "))
        if 0 <= nota1 <=100:
            break
        else: print("A nota deve estar entre 0 e 100")
    except ValueError:
        print("Digite uma nota válida!")
      
while True:
    try:
        nota2 = int(input("\ninsira sua primeira nota: "))
        if 0 <= nota2 <=100:
            break
        else:
            print("A nota deve estar entre 0 e 100")
    except ValueError:
        print("Digite uma nota válida!")

media = (nota1 + nota2)/2

###SISTEMA DE MÉDIA###

if media >= 60:
    print("\nAPROVADO!")
elif media > 20:
    print("\nRECUPERAÇÃO!")
else:
    print("\nREPROVADO!")
