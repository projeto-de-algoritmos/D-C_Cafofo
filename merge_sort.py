def merge_sort(lista):
    """
    Função que realiza a divisão da lista e faz a chamada
    recursiva para cada uma delas, além de conter
    a condição de parada.
    Parametro:
        lista(list): Lista inicial desordenada.
    """
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    esquerda = lista[:meio]
    direita = lista[meio:]

    return merge(esquerda, direita)

def merge(esq, dir):
    """
    Função que ordena os elementos da lista e os
    adiciona a uma nova função que será retornada.
    Paramentros:
        esq(list): Lista com metade inicial dos elementos totais,
        dir(list): Lista com metade final dos elementos totais.
    Retorno:
        lista_ordenada(list): Lista com a mescla das duas listas
        passadas como parametro, ordenadas entre si.
    """
    i = 0
    j = 0
    lista_ordenada = []

    while i < len(esq) and j < len(dir):
        if esq[i] < dir[j]:
            lista_ordenada.append(esq[i])
            i += 1
        else:
            lista_ordenada.append(dir[j])
            j += 1

    while i < len(esq):
        lista_ordenada.append(esq[i])
        i += 1

    lista_ordenada.extend(esq[i:])
    lista_ordenada.extend(dir[i:])
    
    return lista_ordenada
