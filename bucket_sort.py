import time


class BucketSort:
    @staticmethod
    def sort(vetor):
        comparacoes = 0
        trocas = 0
        inicio = time.time()

        # Encontra o valor máximo e mínimo no vetor
        max_value = max(vetor)
        min_value = min(vetor)

        # Calcula o número de baldes
        bucket_count = len(vetor) // 5
        buckets = [[] for _ in range(bucket_count)]

        # Distribui os elementos do vetor nos baldes
        for i in range(len(vetor)):
            comparacoes += 1
            index = int((vetor[i] - min_value) / (max_value - min_value + 1) * bucket_count)
            buckets[index].append(vetor[i])

        # Ordena cada balde usando Insertion Sort
        for bucket in buckets:
            for i in range(1, len(bucket)):
                chave = bucket[i]
                j = i - 1
                while j >= 0 and bucket[j] > chave:
                    comparacoes += 1
                    bucket[j + 1] = bucket[j]
                    j -= 1
                    trocas += 1
                bucket[j + 1] = chave
                comparacoes += 1 if j >= 0 else 0

        # Concatena os baldes para formar o vetor ordenado
        vetor_ordenado = []
        for bucket in buckets:
            vetor_ordenado.extend(bucket)

        fim = time.time()
        tempo_execucao = fim - inicio
        return vetor_ordenado, comparacoes, trocas, tempo_execucao