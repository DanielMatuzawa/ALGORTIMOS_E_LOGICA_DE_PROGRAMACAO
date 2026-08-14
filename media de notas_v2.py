def pedir_nota():
    while True:
        try:
            nota = float(input("Insira sua nota: "))

            if 0 <= nota <= 100:
                return nota
            else:
                print("A nota deve estar entre 0 e 100")

        except ValueError:
            print("Digite uma nota válida!")


nota1 = pedir_nota()
nota2 = pedir_nota()


def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2


media = calcular_media(nota1, nota2)


def verificar_situacao(media):
    if media <= 20:
        return "REPROVADO"
    elif media < 60:
        return "RECUPERAÇÃO"
    else:
        return "APROVADO"


situacao = verificar_situacao(media)


print(f"Sua média foi {media}")
print(f"Sua situação: {situacao}")
