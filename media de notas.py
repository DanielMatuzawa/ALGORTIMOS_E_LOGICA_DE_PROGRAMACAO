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
            
elif semestre == "4. semestre":

    while True:
        print("\n=== DISCIPLINAS DO QUARTO SEMESTRE ===")
        print("1. Banco de Dados")
        print("2. Engenharia de Requisitos")
        print("3. Estudo Contemporâneo e Transversal: Indústria e Transformação Digital")
        print("4. Estudo Contemporâneo e Transversal: Inovação e Pensamento Criativo")
        print("5. Programação Orientada a Objetos")
        print("6. Sistemas Operacionais")

        disciplina = input("\nInsira sua disciplina: ")

        if disciplina == "1":
            disciplina = "Banco de Dados"
            break
        elif disciplina == "2":
            disciplina = "Engenharia de Requisitos"
            break
        elif disciplina == "3":
            disciplina = "Estudo Contemporâneo e Transversal: Indústria e Transformação Digital"
            break
        elif disciplina == "4":
            disciplina = "Estudo Contemporâneo e Transversal: Inovação e Pensamento Criativo"
            break
        elif disciplina == "5":
            disciplina = "Programação Orientada a Objetos"
            break
        elif disciplina == "6":
            disciplina = "Sistemas Operacionais"
            break
        else:
            print("Opção Inválida")


elif semestre == "5. semestre":

    while True:
        print("\n=== DISCIPLINAS DO QUINTO SEMESTRE ===")
        print("1. Estruturas, Pesquisa e Ordenação de Dados")
        print("2. Estudo Contemporâneo e Transversal: Leitura de Imagens, Gráficos e Mapas")
        print("3. Estudo Contemporâneo e Transversal: Propriedade Intelectual")
        print("4. Interface Humano-Computador")
        print("5. Libras")
        print("6. Manutenção de Software")
        print("7. Programação Avançada")

        disciplina = input("\nInsira sua disciplina: ")

        if disciplina == "1":
            disciplina = "Estruturas, Pesquisa e Ordenação de Dados"
            break
        elif disciplina == "2":
            disciplina = "Estudo Contemporâneo e Transversal: Leitura de Imagens, Gráficos e Mapas"
            break
        elif disciplina == "3":
            disciplina = "Estudo Contemporâneo e Transversal: Propriedade Intelectual"
            break
        elif disciplina == "4":
            disciplina = "Interface Humano-Computador"
            break
        elif disciplina == "5":
            disciplina = "Libras"
            break
        elif disciplina == "6":
            disciplina = "Manutenção de Software"
            break
        elif disciplina == "7":
            disciplina = "Programação Avançada"
            break
        else:
            print("Opção Inválida")


elif semestre == "6. semestre":

    while True:
        print("\n=== DISCIPLINAS DO SEXTO SEMESTRE ===")
        print("1. Banco de Dados NoSQL")
        print("2. Estudo Contemporâneo e Transversal: Direitos Humanos, Cidadania e Inclusão")
        print("3. Estudo Contemporâneo e Transversal: Relações Étnico-Raciais e Diferentes Culturas")
        print("4. Paradigmas de Linguagens de Programação")
        print("5. Processos de Software")
        print("6. Projeto, Implementação e Teste de Software")

        disciplina = input("\nInsira sua disciplina: ")

        if disciplina == "1":
            disciplina = "Banco de Dados NoSQL"
            break
        elif disciplina == "2":
            disciplina = "Estudo Contemporâneo e Transversal: Direitos Humanos, Cidadania e Inclusão"
            break
        elif disciplina == "3":
            disciplina = "Estudo Contemporâneo e Transversal: Relações Étnico-Raciais e Diferentes Culturas"
            break
        elif disciplina == "4":
            disciplina = "Paradigmas de Linguagens de Programação"
            break
        elif disciplina == "5":
            disciplina = "Processos de Software"
            break
        elif disciplina == "6":
            disciplina = "Projeto, Implementação e Teste de Software"
            break
        else:
            print("Opção Inválida")


elif semestre == "7. semestre":

    while True:
        print("\n=== DISCIPLINAS DO SÉTIMO SEMESTRE ===")
        print("1. Estudo Contemporâneo e Transversal: Protagonismo e Autonomia Intelectual Criativa")
        print("2. Estudo Contemporâneo e Transversal: Relação de Consumo e Sustentabilidade")
        print("3. Experiência Profissional: Desenvolvimento de Aplicações")
        print("4. Inteligência Artificial")
        print("5. Programação para Dispositivos Móveis")
        print("6. Segurança e Auditoria de Sistemas")
        print("7. Teoria da Computação")

        disciplina = input("\nInsira sua disciplina: ")

        if disciplina == "1":
            disciplina = "Estudo Contemporâneo e Transversal: Protagonismo e Autonomia Intelectual Criativa"
            break
        elif disciplina == "2":
            disciplina = "Estudo Contemporâneo e Transversal: Relação de Consumo e Sustentabilidade"
            break
        elif disciplina == "3":
            disciplina = "Experiência Profissional: Desenvolvimento de Aplicações"
            break
        elif disciplina == "4":
            disciplina = "Inteligência Artificial"
            break
        elif disciplina == "5":
            disciplina = "Programação para Dispositivos Móveis"
            break
        elif disciplina == "6":
            disciplina = "Segurança e Auditoria de Sistemas"
            break
        elif disciplina == "7":
            disciplina = "Teoria da Computação"
            break
        else:
            print("Opção Inválida")


elif semestre == "8. semestre":

    while True:
        print("\n=== DISCIPLINAS DO OITAVO SEMESTRE ===")
        print("1. Arquitetura de Software")
        print("2. Estudo Contemporâneo e Transversal: Administração de Conflito")
        print("3. Estudo Contemporâneo e Transversal: Inteligência Emocional")
        print("4. Experiência Profissional: Fábrica de Software")
        print("5. Gestão de Projetos Tecnológicos")
        print("6. Qualidade de Software")
        print("7. Tecnologias Emergentes em Engenharia de Software")

        disciplina = input("\nInsira sua disciplina: ")

        if disciplina == "1":
            disciplina = "Arquitetura de Software"
            break
        elif disciplina == "2":
            disciplina = "Estudo Contemporâneo e Transversal: Administração de Conflito"
            break
        elif disciplina == "3":
            disciplina = "Estudo Contemporâneo e Transversal: Inteligência Emocional"
            break
        elif disciplina == "4":
            disciplina = "Experiência Profissional: Fábrica de Software"
            break
        elif disciplina == "5":
            disciplina = "Gestão de Projetos Tecnológicos"
            break
        elif disciplina == "6":
            disciplina = "Qualidade de Software"
            break
        elif disciplina == "7":
            disciplina = "Tecnologias Emergentes em Engenharia de Software"
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



