from merge_sort import merge_sort

def combate(jogador1, jogador2):
    """
    Função que recebe os pesos das cartas jogadas
    por cada participante.
    Parametros:
        jogador1(list): Pesos das cartas do primeiro jogador.
        jogador2(list): Pesos das cartas do segundo jogador.    
    Retorno:
        Resultado da partida, sendo:
            0(int): empate
            1(int): primeiro jogador venceu
            2(int): segundo jogador venceu
"""
    merge_sort(jogador1)
    merge_sort(jogador2)

    pontuaçao1 = 0
    pontuaçao2 = 0
    vida_perdida = 0
    vida_perdida1 = 0
    vida_perdida2 = 0

    for i in range(len(jogador1)):
        if jogador1[i] > jogador2[i]:
            pontuaçao1 += 1
            vida_perdida = jogador1[i] - jogador2[i]
            vida_perdida2 += vida_perdida
        elif jogador2[i] > jogador1[i]:
            pontuaçao2 += 1
            vida_perdida = jogador2[i] - jogador1[i]
            vida_perdida1 += vida_perdida
    if pontuaçao1 > pontuaçao2:
        return 1
    elif pontuaçao2 > pontuaçao1:
        return 2
    else:
        if vida_perdida1 > vida_perdida2:
            return 2 
        elif vida_perdida2 > vida_perdida1:
            return 1 
        else:
            return 0
