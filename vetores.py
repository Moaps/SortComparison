import numpy as np

class Vetores:
    def __init__(self, tamanho):
        self.tamanho = tamanho

    def gerar_vetor_ordenado(self):
        vetor = np.random.randint(1, 100000, size=self.tamanho)
        return np.sort(vetor)

    def gerar_vetor_inversamente_ordenado(self):
        return self.gerar_vetor_ordenado()[::-1]

    def gerar_vetor_aleatorio(self):
        return np.random.randint(1, 100000, size=self.tamanho)