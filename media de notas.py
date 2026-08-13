print("===BOLETIM DE NOTAS===")

nome = input("\nInsira seu nome: ")
curso = input("\nInsira seu curso: ")
disciplina = input("\nInsira sua disciplina: ")
semestre = input("\nInsira seu semestre: ")
nota1 = int(input("\ninsira sua primeira nota: "))
nota2 = int(input("\ninsira sua segunda nota: "))

media = (nota1 + nota2)/2

if media >= 60 and media <= 100:
    print("\nAPROVADO!")
elif media <= 20:
    print("\nREPROVADO!")
elif media < 20 and media >60:
    print("\nRECUPERAÇÃO!")
else:
    print("\nERRO INSIRA NOVAMENTE A NOTA")
