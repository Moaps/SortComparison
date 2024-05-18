import time

class BubbleSort:
    @staticmethod
    def sort(vetor):
        comparacoes = 0  # Variável para contar o número de comparações
        trocas = 0  # Variável para contar o número de trocas
        inicio = time.time()  # Inicia a contagem do tempo
        for i in range(len(vetor)):
            for j in range(0, len(vetor) - i - 1):
                comparacoes += 1  # Incrementa a contagem de comparações
                if vetor[j] > vetor[j + 1]:
                    vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]
                    trocas += 1  # Incrementa a contagem de trocas
        fim = time.time()  # Termina a contagem do tempo
        tempo_execucao = fim - inicio  # Calcula o tempo de execução
        return vetor, comparacoes, trocas, tempo_execucao