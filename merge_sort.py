import time

class MergeSort:
    comparacoes = 0
    trocas = 0

    @staticmethod
    def sort(vetor):
        inicio = time.time()
        MergeSort.comparacoes = 0
        MergeSort.trocas = 0
        vetor_ordenado = MergeSort._merge_sort(vetor)
        fim = time.time()
        tempo_execucao = fim - inicio
        return vetor_ordenado, MergeSort.comparacoes, MergeSort.trocas, tempo_execucao

    @staticmethod
    def _merge_sort(vetor):
        if len(vetor) > 1:
            meio = len(vetor) // 2
            esquerda = vetor[:meio]
            direita = vetor[meio:]

            MergeSort._merge_sort(esquerda)
            MergeSort._merge_sort(direita)

            i = j = k = 0
            while i < len(esquerda) and j < len(direita):
                MergeSort.comparacoes += 1
                if esquerda[i] < direita[j]:
                    vetor[k] = esquerda[i]
                    i += 1
                else:
                    vetor[k] = direita[j]
                    j += 1
                k += 1
                MergeSort.trocas += 1

            while i < len(esquerda):
                vetor[k] = esquerda[i]
                i += 1
                k += 1

            while j < len(direita):
                vetor[k] = direita[j]
                j += 1
                k += 1

        return vetor