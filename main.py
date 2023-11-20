import json

def nova_entrevista():
    nome = input("Digite o nome do candidato: ")
    telefone = input("Digite o telefone do candidato: ")

    respostas = {}
    print("De 0 a 5, quais desses aspectos são importantes para você/te agradam? (sendo 0 nada e 5 muito)")
    perguntas = [
        "Limpeza diária",
        "Dividir gastos com mercado",
        "Pet",
        "Dormir antes das 23h",
        "Receber visitas",
        "Ouvir música alta",
        "Fazer barulho"
    ]

    for pergunta in perguntas:
        resposta = int(input(f"{pergunta}: "))
        respostas[pergunta] = resposta

    with open('entrevistas.json', 'a') as arquivo:
        json.dump({ 'nome': nome, 'telefone': telefone, 'respostas': respostas }, arquivo)
        arquivo.write('\n')

def ver_resultados():
    pass

while True:
    print("\nMenu:")
    print("1. Nova entrevista")
    print("2. Ver resultados")
    print("3. Sair")

    escolha = input("Escolha a opção (1/2/3): ")

    if escolha == '1':
        nova_entrevista()
    elif escolha == '2':
        ver_resultados()
    elif escolha == '3':
        print("Saindo do programa. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")
