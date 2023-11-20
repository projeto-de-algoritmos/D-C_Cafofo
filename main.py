import json
from invertion import MergeAndInverte

minhas_preferencia = {
    "respostas": {
        "Limpeza di\u00e1ria": 2,
        "Dividir gastos com mercado": 1,
        "Pet": 5,
        "Dormir antes das 23h": 5,
        "Receber visitas": 5,
        "Ouvir m\u00fasica alta": 1,
        "Fazer barulho": 2
        }
    }


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

def calcula_resultado():
    with open('entrevistas.json', 'r') as arquivo:
        entrevistas = [json.loads(line) for line in arquivo]

    min_inversao = 7
    pessoa_com_maior_pontuacao = None
    
    meus_pontos = [ x for x in minhas_preferencia['respostas'].values()]
    inversion = MergeAndInverte(meus_pontos)
    my_inversion = inversion.inversion

    for entrevista in entrevistas:
        lista_pontos = [ x for x in entrevista['respostas'].values()]
        inversion = MergeAndInverte(lista_pontos)
        candidate_inversion = inversion.inversion
        
        pontuacao = abs(my_inversion - candidate_inversion)

        if pontuacao <= min_inversao:
            min_inversao = pontuacao
            pessoa_com_maior_pontuacao = entrevista

    return pessoa_com_maior_pontuacao

def ver_resultados():
    melhor_match = calcula_resultado()
    print("A melhor opção é: ")
    print(f"Nome: {melhor_match['nome']} - telefone: {melhor_match['telefone']}")

while True:
    print("\nMenu:")
    print("1. Nova entrevista")
    print("2. Ver resultados")
    print("3. Sair")

    escolha = input("Escolha a opção (1/2/3): ")

    if escolha == '1':
        print("")
        nova_entrevista()
    elif escolha == '2':
        print("")
        ver_resultados()
        break
    elif escolha == '3':
        print("Saindo do programa. Até mais!")
        print("")
        break
    else:
        print("Opção inválida. Tente novamente.")
