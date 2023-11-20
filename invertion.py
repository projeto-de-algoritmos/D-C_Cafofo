class MergeAndInverte():
    def __init__(self, my_list):
        self.inversion = 0
        self.my_list = self.merge_sort(my_list)

    def merge_sort(self, lista):
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

        esquerda = self.merge_sort(esquerda)
        direita = self.merge_sort(direita)

        return self.merge(esquerda, direita)

    def merge(self, esq, dir):
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
                self.inversion += 1
                j += 1

        while i < len(esq):
            lista_ordenada.append(esq[i])
            i += 1

        while j < len(dir):
            lista_ordenada.append(dir[j])
            j += 1

        return lista_ordenada
