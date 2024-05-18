import time

class SelectionSort:
    @staticmethod
    def sort(vetor):
        comparacoes = 0
        trocas = 0
        inicio = time.time()
        for i in range(len(vetor)):
            min_idx = i
            for j in range(i+1, len(vetor)):
                comparacoes += 1
                if vetor[j] < vetor[min_idx]:
                    min_idx = j
            vetor[i], vetor[min_idx] = vetor[min_idx], vetor[i]
            trocas += 1
        fim = time.time()
        tempo_execucao = fim - inicio
        return vetor, comparacoes, trocas, tempo_execucao