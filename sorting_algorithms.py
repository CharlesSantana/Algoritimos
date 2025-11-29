# -*- coding: utf-8 -*-
"""
Implementações dos algoritmos de ordenação solicitados,
incluindo a contagem de operações (comparações, trocas e recursões).
"""
import time
import random


# Estrutura para armazenar os resultados da ordenação
class SortResult:
    def __init__(self, arr, comparisons=0, swaps=0, recursions=0):
        self.arr = arr
        self.comparisons = comparisons
        self.swaps = swaps
        self.recursions = recursions

# 1. Bubble Sort (Ordenação por Bolha)
def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    
    # Cria uma cópia para não modificar a lista original
    local_arr = arr[:]

    for i in range(n):
        # Flag para otimização: se não houver trocas em uma passagem, a lista está ordenada
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1 # Contagem de comparação
            if local_arr[j] > local_arr[j + 1]:
                local_arr[j], local_arr[j + 1] = local_arr[j + 1], local_arr[j]
                swaps += 1 # Contagem de troca
                swapped = True
        
        # Se não houve troca nesta passagem, a lista está ordenada
        if not swapped:
            break
            
    return SortResult(local_arr, comparisons, swaps)

# 2. Insertion Sort (Ordenação por Inserção)
def insertion_sort(arr):
    comparisons = 0
    swaps = 0
    local_arr = arr[:]

    for i in range(1, len(local_arr)):
        key = local_arr[i]
        j = i - 1

        # A condição do while (j >= 0 and key < local_arr[j]) é a comparação principal
        while j >= 0:
            comparisons += 1 # Contagem de comparação (para a condição key < local_arr[j])
            if key < local_arr[j]:
                local_arr[j + 1] = local_arr[j]
                swaps += 1 # Contagem de troca (na verdade, um deslocamento)
                j -= 1
            else:
                # Se a condição for falsa, a comparação ainda ocorreu, mas o loop para
                break
        
        # Se o loop parou por j < 0, a última comparação (j=-1) não ocorreu,
        # mas o contador já está correto, pois a comparação 'j >= 0' é implícita.
        # No caso de j >= 0 e key >= local_arr[j], a comparação ocorreu e o loop parou.
        
        # Insere 'key' na sua posição correta
        local_arr[j + 1] = key
        
    return SortResult(local_arr, comparisons, swaps)

# 3. Selection Sort (Ordenação por Seleção)
def selection_sort(arr):
    comparisons = 0
    swaps = 0
    local_arr = arr[:]

    for i in range(len(local_arr)):
        min_idx = i

        for j in range(i + 1, len(local_arr)):
            comparisons += 1 # Contagem de comparação
            if local_arr[j] < local_arr[min_idx]:
                min_idx = j

        # Troca o elemento mínimo encontrado com o elemento na posição 'i'
        if min_idx != i:
            local_arr[i], local_arr[min_idx] = local_arr[min_idx], local_arr[i]
            swaps += 1 # Contagem de troca
            
    return SortResult(local_arr, comparisons, swaps)

# 4. Merge Sort (Ordenação por Mistura)
def merge_sort(arr):
    # Dicionário para armazenar as contagens, passado por referência
    counts = {'comparisons': 0, 'recursions': 0}
    
    def merge_sort_recursive(arr, counts):
        if len(arr) > 1:
            counts['recursions'] += 1 # Contagem de chamada recursiva
            
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]

            # Chamadas recursivas
            merge_sort_recursive(L, counts)
            merge_sort_recursive(R, counts)

            i = j = k = 0

            # Mescla as duas metades ordenadas (L e R) de volta em arr[]
            while i < len(L) and j < len(R):
                counts['comparisons'] += 1 # Contagem de comparação
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            # Verifica se restaram elementos em L
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            # Verifica se restaram elementos em R
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
        
        # Nota: Merge Sort não realiza "trocas" no sentido de permutar elementos
        # in-place, mas sim "movimentações" ou "cópia" de dados. Para fins de
        # análise de complexidade, focaremos em comparações e recursões.
        # O número de movimentações é aproximadamente 3*N, mas não será contado
        # explicitamente como "swaps" para evitar confusão com os outros algoritmos.
        return arr

    local_arr = arr[:]
    sorted_arr = merge_sort_recursive(local_arr, counts)
    
    # O número de recursões é o total de chamadas, mas a contagem é feita
    # no início da função recursiva, então já está correta.
    return SortResult(sorted_arr, counts['comparisons'], swaps=0, recursions=counts['recursions'])

# 5. Quick Sort (Ordenação Rápida)
def quick_sort(arr):
    counts = {'comparisons': 0, 'swaps': 0, 'recursions': 0}
    local_arr = arr[:]
    
    def partition(arr, low, high, counts):
        # Modificação para evitar o pior caso: escolhe um pivô aleatório
        # e o move para o final para que o resto da lógica funcione como antes.
        rand_pivot_idx = random.randint(low, high)
        arr[rand_pivot_idx], arr[high] = arr[high], arr[rand_pivot_idx]
        
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            counts['comparisons'] += 1 # Contagem de comparação
            if arr[j] <= pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
                counts['swaps'] += 1 # Contagem de troca

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        counts['swaps'] += 1 # Troca final do pivô
        return i + 1

    def quick_sort_recursive(arr, low, high, counts):
        if low < high:
            counts['recursions'] += 1 # Contagem de chamada recursiva (após a primeira chamada)
            
            pi = partition(arr, low, high, counts)

            # Chamadas recursivas
            quick_sort_recursive(arr, low, pi - 1, counts)
            quick_sort_recursive(arr, pi + 1, high, counts)
        
        return arr

    # A primeira chamada não conta como recursão para manter a contagem alinhada
    # com as chamadas que realmente dividem o problema.
    if len(local_arr) > 1:
        quick_sort_recursive(local_arr, 0, len(local_arr) - 1, counts)
    
    return SortResult(local_arr, counts['comparisons'], counts['swaps'], counts['recursions'])

# 6. Shell Sort (Ordenação Shell)
def shell_sort(arr):
    comparisons = 0
    swaps = 0
    local_arr = arr[:]
    n = len(local_arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = local_arr[i]
            j = i

            # O loop while contém a comparação principal
            while j >= gap:
                comparisons += 1 # Contagem de comparação (para a condição arr[j - gap] > temp)
                if local_arr[j - gap] > temp:
                    local_arr[j] = local_arr[j - gap]
                    swaps += 1 # Contagem de troca (deslocamento)
                    j -= gap
                else:
                    # Se a condição for falsa, a comparação ocorreu e o loop para
                    break

            local_arr[j] = temp
        gap //= 2
        
    return SortResult(local_arr, comparisons, swaps)

# ==============================================================================
# Funções Auxiliares para Teste Experimental
# ==============================================================================

def generate_data(size, data_type):
    """Gera listas de dados para teste."""
    if data_type == 'random':
        data = [random.randint(1, size * 10) for _ in range(size)]
    elif data_type == 'sorted':
        data = list(range(1, size + 1))
    elif data_type == 'reverse':
        data = list(range(size, 0, -1))
    else:
        raise ValueError("Tipo de dado inválido.")
    return data

def run_test(algorithm_func, data):
    """Executa o algoritmo e mede o tempo e as operações."""
    # Cria uma cópia profunda da lista para garantir que o algoritmo
    # comece sempre com a mesma entrada.
    test_data = data[:]
    
    start_time = time.perf_counter()
    result = algorithm_func(test_data)
    end_time = time.perf_counter()
    
    execution_time = end_time - start_time
    
    return {
        'time': execution_time,
        'comparisons': result.comparisons,
        'swaps': result.swaps,
        'recursions': result.recursions
    }

# ==============================================================================
# Função Principal de Execução
# ==============================================================================

def main_experiment():
    # Definição dos parâmetros do experimento
    sizes = [10, 100, 1000, 10000]
    data_types = ['sorted', 'reverse', 'random']
    
    # Mapeamento dos algoritmos para suas funções
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Insertion Sort": insertion_sort,
        "Selection Sort": selection_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort,
        "Shell Sort": shell_sort
    }
    
    # Estruturas para armazenar os resultados
    results_time = {}
    results_ops = {}
    results_recursions = {}

    print("Iniciando o experimento...")

    for name, func in algorithms.items():
        print(f"\nTestando {name}...")
        results_time[name] = {}
        results_ops[name] = {}
        results_recursions[name] = {}
        
        for size in sizes:
            results_time[name][size] = {}
            results_ops[name][size] = {}
            results_recursions[name][size] = {}
            
            for data_type in data_types:
                # Geração de dados
                data = generate_data(size, data_type)
                
                # Execução do teste
                test_result = run_test(func, data)
                
                # Armazenamento dos resultados
                results_time[name][size][data_type] = test_result['time']
                results_ops[name][size][data_type] = {
                    'comparisons': test_result['comparisons'],
                    'swaps': test_result['swaps']
                }
                
                # Armazenamento de recursões (apenas para Merge e Quick Sort)
                if name in ["Merge Sort", "Quick Sort"]:
                    results_recursions[name][size][data_type] = test_result['recursions']
                
                print(f"  Tamanho {size}, Tipo {data_type}: Tempo={test_result['time']:.6f}s, Comparações={test_result['comparisons']}, Trocas={test_result['swaps']}")

    print("\nExperimento concluído.")
    
    # Retorna os resultados para processamento posterior (tabelas e gráficos)
    return results_time, results_ops, results_recursions

if __name__ == '__main__':
    # Executa o experimento e armazena os resultados em arquivos temporários
    time_data, ops_data, rec_data = main_experiment()
    
    # Salva os dados brutos em arquivos para uso nas próximas fases
    import json
    
    with open('time_data.json', 'w') as f:
        json.dump(time_data, f, indent=4)
        
    with open('ops_data.json', 'w') as f:
        json.dump(ops_data, f, indent=4)
        
    with open('rec_data.json', 'w') as f:
        json.dump(rec_data, f, indent=4)
        
    print("\nDados do experimento salvos em time_data.json, ops_data.json e rec_data.json.")
    
    # Exemplo de uso de um algoritmo simples para verificação
    # test_list = [64, 34, 25, 12, 22, 11, 90]
    # result = bubble_sort(test_list)
    # print(f"\nTeste Bubble Sort: {result.arr}, Comparações: {result.comparisons}, Trocas: {result.swaps}")
