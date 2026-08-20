
def positivo_negativo():
    print("Número Positivo ou Negativo")

    n= float(input("Insira um número: "))
    if n > 0:
        print("O número é Positivo!")
    elif n < 0:
        print("O número é Negativo")
    else:
        print("Zero!")
positivo_negativo()

def maior_2numeros():

    print("Maior Número: ")

    a = float(input("Insira um número: "))
    b = float(input("Insira um número: "))

    if a > b:
        print(f"O número {a} é maior que {b}")
    elif a < b:
        print(f"O número {b} é maior que {a}")
    else:
        print("Os núemros são iguais!")
maior_numero()

def par_impar():

    print("Par ou ìmpar")

    a = float(input("Insira um número: "))

    if a %2 == 0:
        print("O número é Par")
    else:
        print("O número é Impar")
par_impar()

def maior_3numeros():
    print("Maior dos 3 números")

    a = float(input("Insira um número: "))
    b = float(input("Insira um número: "))
    c = float(input("Insira um número: "))

    maior1 = ((a+b+abs(a-b))/2)
    maior2 = ((maior1+c+abs(maior1-c))/2)

    print(f"o maior entre os números {a,b,c} é o {maior2}")
maior_3numeros()


def maior_5numeros():
    print("Maior dos 5 números")

    ##armazena os numeros
    numeros = []


    for i in range(5):
        numero = float(input("Insira um número: "))
        ##ligado com os []
        numeros.append(numero)
        ##max encontra o maior valor, existe min, sum, len...
    maior = max(numeros)

    print(f"O valor maior é: {maior}")

maior_5numeros()

