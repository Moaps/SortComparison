import time

class InsertionSort:
    @staticmethod
    def sort(vetor):
        comparacoes = 0
        trocas = 0
        inicio = time.time()
        for i in range(1, len(vetor)):
            chave = vetor[i]
            j = i - 1
            while j >= 0 and vetor[j] > chave:
                comparacoes += 1
                vetor[j + 1] = vetor[j]
                j -= 1
                trocas += 1
            vetor[j + 1] = chave
            comparacoes += 1 if j >= 0 else 0
        fim = time.time()
        tempo_execucao = fim - inicio
        return vetor, comparacoes, trocas, tempo_execucao