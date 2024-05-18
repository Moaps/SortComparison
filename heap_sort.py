import time

class HeapSort:
    comparacoes = 0
    trocas = 0

    @staticmethod
    def sort(vetor):
        inicio = time.time()
        HeapSort.comparacoes = 0
        HeapSort.trocas = 0
        n = len(vetor)

        for i in range(n // 2 - 1, -1, -1):
            HeapSort._heapify(vetor, n, i)

        for i in range(n-1, 0, -1):
            vetor[i], vetor[0] = vetor[0], vetor[i]
            HeapSort.trocas += 1
            HeapSort._heapify(vetor, i, 0)

        fim = time.time()
        tempo_execucao = fim - inicio
        return vetor, HeapSort.comparacoes, HeapSort.trocas, tempo_execucao

    @staticmethod
    def _heapify(vetor, n, i):
        maior = i
        esquerda = 2 * i + 1
        direita = 2 * i + 2

        if esquerda < n:
            HeapSort.comparacoes += 1
            if vetor[esquerda] > vetor[maior]:
                maior = esquerda

        if direita < n:
            HeapSort.comparacoes += 1
            if vetor[direita] > vetor[maior]:
                maior = direita

        if maior != i:
            vetor[i], vetor[maior] = vetor[maior], vetor[i]
            HeapSort.trocas += 1
            HeapSort._heapify(vetor, n, maior)