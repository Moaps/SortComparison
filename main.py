from vetores import Vetores
from bubble_sort import BubbleSort
from bucket_sort import BucketSort
from heap_sort import HeapSort
from insertion_sort import InsertionSort
from merge_sort import MergeSort
from quick_sort import QuickSort
from selection_sort import SelectionSort
import copy


def main():
    tamanho = 16000
    vetores = Vetores(tamanho)

    algoritmos = {
        "BubbleSort": BubbleSort.sort,
        "BucketSort": BucketSort.sort,
        "HeapSort": HeapSort.sort,
        "InsertionSort": InsertionSort.sort,
        "MergeSort": MergeSort.sort,
        "QuickSort": QuickSort.sort,
        "SelectionSort": SelectionSort.sort
    }

    for tipo, vetor in {
        "Ordenado": vetores.gerar_vetor_ordenado(),
        "Inversamente Ordenado": vetores.gerar_vetor_inversamente_ordenado(),
        "Aleatório": vetores.gerar_vetor_aleatorio()
    }.items():
        for nome_algoritmo, funcao_sort in algoritmos.items():
            vetor_copia = copy.copy(vetor)
            vetor_ordenado, comparacoes, trocas, tempo_execucao = funcao_sort(vetor_copia)

            print(f"{nome_algoritmo} - {tipo} (primeiros 10 elementos): {vetor_ordenado[:10]}")
            print(f"Comparações para vetor {tipo.lower()}: {comparacoes}")
            print(f"Trocas para vetor {tipo.lower()}: {trocas}")
            print(f"Tempo de execução para vetor {tipo.lower()}: {tempo_execucao:.6f} segundos\n")


if __name__ == "__main__":
    main()