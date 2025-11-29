# Análise e Comparação de Algoritmos de Ordenação
Acesse https://sortalgos-opvmfuxm.manus.space/

## 1. Introdução

Este relatório apresenta uma análise detalhada de seis algoritmos de ordenação fundamentais: Bubble Sort, Insertion Sort, Selection Sort, Merge Sort, Quick Sort e Shell Sort. O objetivo é fornecer uma compreensão teórica de suas lógicas, quantificar suas operações principais (comparações e trocas) e avaliar seu desempenho prático em diferentes cenários de entrada.

A implementação de todos os algoritmos foi realizada em **Python**, com foco na clareza e simplicidade do código, conforme solicitado.

## 2. Explicação da Lógica dos Algoritmos

Cada algoritmo de ordenação emprega uma estratégia distinta para organizar os elementos de uma lista.

| Algoritmo | Estratégia Principal | Descrição da Lógica |
| :--- | :--- | :--- |
| **Bubble Sort** | Comparação Direta | Percorre repetidamente a lista, compara pares de elementos adjacentes e os troca se estiverem na ordem errada. O maior elemento "borbulha" para o final da lista a cada passagem. |
| **Insertion Sort** | Inserção | Constrói a lista final ordenada um item por vez. Cada elemento é removido da entrada, comparado com os elementos já ordenados e inserido em sua posição correta. |
| **Selection Sort** | Seleção | Divide a lista em duas partes: ordenada e não ordenada. Repetidamente, encontra o elemento mínimo na parte não ordenada e o move para o final da parte ordenada. |
| **Merge Sort** | Divisão e Conquista | Divide a lista em duas metades até que cada sublista contenha apenas um elemento (que é, por definição, ordenado). Em seguida, mescla (merge) as sublistas de volta, garantindo que a mesclagem resulte em uma lista ordenada. |
| **Quick Sort** | Divisão e Conquista | Escolhe um elemento chamado **pivô** e particiona o restante da lista em duas sublistas: elementos menores que o pivô e elementos maiores que o pivô. O processo é aplicado recursivamente às sublistas. |
| **Shell Sort** | Inserção com Incrementos | É uma extensão do Insertion Sort. Ele ordena elementos que estão distantes um do outro, usando um intervalo (gap) que é gradualmente reduzido. Isso permite que elementos fora de posição se movam grandes distâncias mais rapidamente. |

## 3. Análise da Complexidade de Tempo (Big O)

A complexidade de tempo, expressa na notação Big O, descreve como o tempo de execução de um algoritmo cresce em função do tamanho da entrada ($N$).

| Algoritmo | Melhor Caso | Caso Médio | Pior Caso |
| :--- | :--- | :--- | :--- |
| **Bubble Sort** | $O(N)$ | $O(N^2)$ | $O(N^2)$ |
| **Insertion Sort** | $O(N)$ | $O(N^2)$ | $O(N^2)$ |
| **Selection Sort** | $O(N^2)$ | $O(N^2)$ | $O(N^2)$ |
| **Merge Sort** | $O(N \log N)$ | $O(N \log N)$ | $O(N \log N)$ |
| **Quick Sort** | $O(N \log N)$ | $O(N \log N)$ | $O(N^2)$ |
| **Shell Sort** | $O(N \log N)$ | $O(N \log^2 N)$ ou $O(N^{4/3})$ | $O(N^2)$ |

## 4. Análise Experimental

Os testes experimentais foram realizados com listas de tamanhos $N = \{10, 100, 1.000, 10.000\}$ e três tipos de entrada: **S** (Ordenada), **R** (Inversamente Ordenada) e **A** (Aleatória).

### Tabela de Tempos de Execução (Segundos)

O tempo de execução é crucial para avaliar o desempenho prático.

## Tabela de Tempos de Execução (Segundos)

Os tempos de execução são apresentados em segundos (s) para diferentes tamanhos de entrada (N) e tipos de ordenação (S: Ordenada, R: Inversamente Ordenada, A: Aleatória).

| Algoritmo      |   N=10 (S) |   N=10 (R) |   N=10 (A) |   N=100 (S) |   N=100 (R) |   N=100 (A) |   N=1000 (S) |   N=1000 (R) |   N=1000 (A) |   N=10000 (S) |   N=10000 (R) |   N=10000 (A) |
|:---------------|-----------:|-----------:|-----------:|------------:|------------:|------------:|-------------:|-------------:|-------------:|--------------:|--------------:|--------------:|
| Bubble Sort    |    7e-06   |    1e-05   |    5e-06   |    6e-06    |    0.000617 |    0.00047  |     6.9e-05  |     0.074345 |     0.057475 |      0.000775 |      8.83083  |      6.09202  |
| Insertion Sort |    1.6e-05 |    7e-06   |    3e-06   |    9e-06    |    0.000476 |    0.000252 |     0.000109 |     0.052397 |     0.027058 |      0.001168 |      5.64457  |      2.89965  |
| Selection Sort |    1.9e-05 |    6e-06   |    5e-06   |    0.000258 |    0.000261 |    0.000254 |     0.028969 |     0.029411 |     0.029524 |      2.94243  |      2.97881  |      3.54976  |
| Merge Sort     |    4.2e-05 |    1.9e-05 |    1.3e-05 |    0.000159 |    0.000182 |    0.000243 |     0.002856 |     0.002071 |     0.002243 |      0.021914 |      0.021584 |      0.029299 |
| Quick Sort     |    4.3e-05 |    1.3e-05 |    1.3e-05 |    0.000149 |    0.000192 |    0.000158 |     0.002854 |     0.00233  |     0.002263 |      0.031966 |      0.031554 |      0.032213 |
| Shell Sort     |    2.8e-05 |    6e-06   |    5e-06   |    4.3e-05  |    6.3e-05  |    9.3e-05  |     0.000783 |     0.001338 |     0.001808 |      0.012272 |      0.020000 |      0.036817 |

### Tabela de Comparações e Trocas

Esta tabela quantifica as operações principais, que são os fatores determinantes da complexidade de tempo.

## Tabela de Comparações e Trocas

Quantidade de operações principais (Comparações e Trocas) para diferentes cenários.

| Algoritmo      |   Comp. (N=10, S) |   Trocas (N=10, S) |   Comp. (N=10, R) |   Trocas (N=10, R) |   Comp. (N=10, A) |   Trocas (N=10, A) |   Comp. (N=100, S) |   Trocas (N=100, S) |   Comp. (N=100, R) |   Trocas (N=100, R) |   Comp. (N=100, A) |   Trocas (N=100, A) |   Comp. (N=1000, S) |   Trocas (N=1000, S) |   Comp. (N=1000, R) |   Trocas (N=1000, R) |   Comp. (N=1000, A) |   Trocas (N=1000, A) | Comp. (N=10000, S)   |   Trocas (N=10000, S) | Comp. (N=10000, R)   | Trocas (N=10000, R)   | Comp. (N=10000, A)   | Trocas (N=10000, A)   |
|:---------------|------------------:|-------------------:|------------------:|-------------------:|------------------:|-------------------:|-------------------:|--------------------:|-------------------:|--------------------:|-------------------:|--------------------:|--------------------:|---------------------:|--------------------:|---------------------:|--------------------:|---------------------:|:---------------------|----------------------:|:---------------------|:----------------------|:---------------------|:----------------------|
| Bubble Sort    |                 9 |                  0 |                45 |                 45 |                35 |                 14 |              99    |                   0 |              4.95  |               4.95  |              4.922 |               2.31  |             999     |                 0    |             499.5   |              499.5   |             497.789 |              243.767 | 9.999                |                 0     | 49.995.000           | 49.995.000            | 49.962.615           | 25.267.223            |
| Insertion Sort |                 9 |                  0 |                45 |                 45 |                24 |                 16 |              99    |                   0 |              4.95  |               4.95  |              2.75  |               2.658 |             999     |                 0    |             499.5   |              499.5   |             249.988 |              248.995 | 9.999                |                 0     | 49.995.000           | 49.995.000            | 24.837.085           | 24.827.093            |
| Selection Sort |                45 |                  0 |                45 |                  5 |                45 |                  8 |               4.95 |                   0 |              4.95  |              50     |              4.95  |              93     |             499.5   |                 0    |             499.5   |              500     |             499.5   |              996     | 49.995.000           |                 0     | 49.995.000           | 5.000                 | 49.995.000           | 9.997                 |
| Merge Sort     |                15 |                  0 |                19 |                  0 |                25 |                  0 |             316    |                   0 |            356     |               0     |            540     |               0     |               4.932 |                 0    |               5.044 |                0     |               8.705 |                0     | 64.608               |                 0     | 69.008               | 0                     | 120.578              | 0                     |
| Quick Sort     |                23 |                 14 |                21 |                 20 |                30 |                 14 |             575    |                 395 |            753     |             431     |            599     |             421     |              10.791 |                 6.23 |              10.493 |                6.125 |              10.807 |                5.651 | 163.907              |                89.141 | 144.943              | 81.357                | 158.068              | 90.335                |
| Shell Sort     |                22 |                  0 |                27 |                 13 |                35 |                 16 |             503    |                   0 |            668     |             260     |            955     |             507     |               8.006 |                 0    |              11.716 |                4.700 |              15.469 |                7.987 | 120.005              |                 0     | 172.578              | 62.560                | 264.608              | 149.572               |

### Tabela de Chamadas Recursivas

Para os algoritmos de Divisão e Conquista (Merge Sort e Quick Sort), o número de chamadas recursivas é um indicador da profundidade da árvore de execução.

## Tabela de Chamadas Recursivas

Número de chamadas recursivas para os algoritmos de Divisão e Conquista.

| Algoritmo   |   N=10 (S) |   N=10 (R) |   N=10 (A) |   N=100 (S) |   N=100 (R) |   N=100 (A) |   N=1000 (S) |   N=1000 (R) |   N=1000 (A) |   N=10000 (S) |   N=10000 (R) |   N=10000 (A) |
|:------------|-----------:|-----------:|-----------:|------------:|------------:|------------:|-------------:|-------------:|-------------:|--------------:|--------------:|--------------:|
| Merge Sort  |          9 |          9 |          9 |          99 |          99 |          99 |          999 |          999 |          999 |         9.999 |         9.999 |         9.999 |
| Quick Sort  |          7 |          8 |          8 |          66 |          68 |          68 |          664 |          665 |          665 |         6.691 |         6.692 |         6.692 |

### Gráfico Comparativo de Desempenho

O gráfico a seguir ilustra visualmente a diferença de desempenho entre os algoritmos no caso aleatório, utilizando escalas logarítmicas para melhor visualização da diferença de crescimento.

![Gráfico Comparativo de Desempenho (Caso Aleatório)](https://private-us-east-1.manuscdn.com/sessionFile/kXikwKXwYX0k6Tbs8zA1U7/sandbox/lwCfNRIjCbP65f7WmXkMXm-images_1764396871968_na1fn_L2hvbWUvdWJ1bnR1L3NvcnRpbmdfcHJvamVjdC9wZXJmb3JtYW5jZV9wbG90.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUva1hpa3dLWHdZWDBrNlRiczh6QTFVNy9zYW5kYm94L2x3Q2ZOUklqQ2JQNjVmN1dtWGtNWG0taW1hZ2VzXzE3NjQzOTY4NzE5NjhfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzTnZjblJwYm1kZmNISnZhbVZqZEM5d1pYSm1iM0p0WVc1alpWOXdiRzkwLnBuZyIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc5ODc2MTYwMH19fV19&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=FcE9HpEbytie495Z-UYPf7IYIAmuWHJPHxW2u7BQS1wWjFN5NdBbAqLbZqGNnsQTLRSv0~0kui8zgmlCxEgGi5kTpeFpZSGXQ2SmvzhwFVxp5cngCrAcDmkWlXJaGSsb2366wn-irJDvXp2Uu-nT-F2kWkFPK~My96AiVgZZvi1MGEM~tjrxVAmOUVzvc-6jtWeI2Ig8xHiuXp4gVqDtRb8Jryb5HdbWYnKfF7UECc3IrW3fgcBfQ8aWpJPzyzackK4EF1oHpqznuf-XPH3Cb0atgwGHkUiuQ3wK50f6S5LgPtqtDgT6wri88iXlHNA8EC5QPr2AhJu20yYuG55prw__)

O gráfico a seguir foca apenas nos algoritmos mais rápidos ($O(N \log N)$) para uma visualização mais clara de suas diferenças.

![Gráfico Comparativo de Desempenho (Algoritmos O(N log N) - Caso Aleatório)](https://private-us-east-1.manuscdn.com/sessionFile/kXikwKXwYX0k6Tbs8zA1U7/sandbox/lwCfNRIjCbP65f7WmXkMXm-images_1764396871968_na1fn_L2hvbWUvdWJ1bnR1L3NvcnRpbmdfcHJvamVjdC9wZXJmb3JtYW5jZV9wbG90X2Zhc3Q.png?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9wcml2YXRlLXVzLWVhc3QtMS5tYW51c2Nkbi5jb20vc2Vzc2lvbkZpbGUva1hpa3dLWHdZWDBrNlRiczh6QTFVNy9zYW5kYm94L2x3Q2ZOUklqQ2JQNjVmN1dtWGtNWG0taW1hZ2VzXzE3NjQzOTY4NzE5NjhfbmExZm5fTDJodmJXVXZkV0oxYm5SMUwzTnZjblJwYm1kZmNISnZhbVZqZEM5d1pYSm1iM0p0WVc1alpWOXdiRzkwWDJaaGMzUS5wbmciLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE3OTg3NjE2MDB9fX1dfQ__&Key-Pair-Id=K2HSFNDJXOU9YS&Signature=XrsKFuZWCm8x1dW3zn5f5r7ql4EX9GJQTwq6XK5RBRhlzPH5Qy2p~~2K18EpCWoB5zSb2XVsrB~REE688AxpjWfgSYTOYxauq4YenFw4yW4J9l69v8B2FP~ZrKbD7p1nxqQqXpDu-X6jxjp3APufTB5cUQ9sSWUPkX52~6Ar8RWk1SuXmoyWV4pkRM7B4SsUttgp3LbwqbLhEj45cVfG4BgrKEEunPKhVsksCJm-Eq4Kjd2dXMIqPeJKp7WAlpmSkM8vaqOHYdTc716qIAIpqiX0of9Us2lhryr6e1ESB6ASzrK2NKifN2hLohL8E2FQH~orJoW2L0NsHjLqc3hIhA__)

## 5. Conclusão Reflexiva

### 5.1. Comparação entre Desempenho Teórico e Prático

Os resultados experimentais confirmam amplamente a análise teórica de complexidade:

*   **Algoritmos $O(N^2)$ (Bubble, Insertion, Selection):** Estes algoritmos demonstraram um crescimento de tempo de execução dramaticamente maior para $N=10.000$, especialmente nos casos pior e médio. O **Selection Sort** manteve um número fixo de comparações ($N^2/2$), mas o **Insertion Sort** e o **Bubble Sort** foram significativamente mais rápidos no **Melhor Caso** ($O(N)$), onde a lista já estava ordenada, confirmando a otimização de suas lógicas.
*   **Algoritmos $O(N \log N)$ (Merge, Quick, Shell):** Estes algoritmos escalaram muito melhor, com tempos de execução em $N=10.000$ ordens de magnitude menores que os algoritmos $O(N^2)$.
    *   O **Merge Sort** apresentou o desempenho mais estável, com complexidade $O(N \log N)$ em todos os casos, o que é visível pela baixa variação no número de comparações.
    *   O **Quick Sort** (com pivô aleatório) manteve um desempenho prático excelente, próximo ao Merge Sort, confirmando seu status como um dos algoritmos mais rápidos na prática.

### 5.2. Situações de Uso Adequado

A escolha do algoritmo ideal depende das características da entrada e dos requisitos de estabilidade e memória.

| Algoritmo | Situação Mais Adequada |
| :--- | :--- |
| **Bubble Sort** | **Não recomendado** para uso geral. Apenas para fins didáticos ou para listas muito pequenas. |
| **Insertion Sort** | **Listas quase ordenadas** ou **listas muito pequenas**. Seu $O(N)$ no melhor caso o torna eficiente para manter uma lista já quase ordenada. |
| **Selection Sort** | Situações onde o **número de trocas deve ser minimizado**. Ele realiza no máximo $N$ trocas, sendo útil em cenários onde a escrita na memória é custosa. |
| **Merge Sort** | **Ordenação de grandes volumes de dados** onde a estabilidade é crucial (mantém a ordem relativa de elementos iguais) e o desempenho no pior caso deve ser garantido ($O(N \log N)$). Ideal para ordenação externa. |
| **Quick Sort** | **Uso geral e de alto desempenho**. É o algoritmo mais rápido na prática para a maioria das entradas aleatórias, devido à sua excelente localidade de referência e baixo custo de constantes. |
| **Shell Sort** | **Alternativa ao Insertion Sort** para listas de tamanho moderado, sendo mais rápido que os algoritmos $O(N^2)$ simples, mas sem a sobrecarga de recursão do Merge/Quick Sort. |

## 6. Código-Fonte

O código-fonte completo, incluindo as implementações com contagem de operações e o script de análise experimental, está disponível no arquivo `sorting_algorithms.py`.

## 7. Anexos

Os seguintes arquivos foram gerados durante a análise:

*   **Código-fonte:** `sorting_algorithms.py`
*   **Tabelas de Análise:** `analysis_tables.md` (conteúdo inserido na Seção 4)
*   **Gráfico Comparativo:** `performance_plot.png` e `performance_plot_fast.png`

---

(Conteudo Interativo https://sortalgos-opvmfuxm.manus.space/)
