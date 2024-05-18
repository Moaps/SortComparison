import time

class QuickSort:
    comparacoes = 0
    trocas = 0

    @staticmethod
    def sort(vetor):
        inicio = time.time()
        QuickSort.comparacoes = 0
        QuickSort.trocas = 0
        QuickSort._quick_sort_iterativo(vetor, 0, len(vetor) - 1)
        fim = time.time()
        tempo_execucao = fim - inicio
        return vetor, QuickSort.comparacoes, QuickSort.trocas, tempo_execucao

    @staticmethod
    def _quick_sort_iterativo(vetor, low, high):
        # Criação de uma pilha auxiliar
        size = high - low + 1
        stack = [0] * size

        # Inicialização da pilha
        top = -1
        top = top + 1
        stack[top] = low
        top = top + 1
        stack[top] = high

        # Continue popping from stack while is not empty
        while top >= 0:
            # Pop high and low
            high = stack[top]
            top = top - 1
            low = stack[top]
            top = top - 1

            # Set pivot element at its correct position in sorted array
            p = QuickSort._partition(vetor, low, high)

            # If there are elements on left side of pivot, then push left side to stack
            if p - 1 > low:
                top = top + 1
                stack[top] = low
                top = top + 1
                stack[top] = p - 1

            # If there are elements on right side of pivot, then push right side to stack
            if p + 1 < high:
                top = top + 1
                stack[top] = p + 1
                top = top + 1
                stack[top] = high

    @staticmethod
    def _partition(vetor, low, high):
        pivot = vetor[high]
        i = low - 1
        for j in range(low, high):
            QuickSort.comparacoes += 1
            if vetor[j] < pivot:
                i += 1
                vetor[i], vetor[j] = vetor[j], vetor[i]
                QuickSort.trocas += 1
        vetor[i + 1], vetor[high] = vetor[high], vetor[i + 1]
        QuickSort.trocas += 1
        return i + 1