# Versão Recursiva

def merge_recursivo(A, aux, esquerda, meio, direita):
    # Método para juntar dois vetores ordenados
    for k in range(esquerda, direita + 1):
        aux[k] = A[k]
    i = esquerda
    j = meio + 1
    for k in range(esquerda, direita + 1):
        if i > meio:
            A[k] = aux[j]
            j += 1
        elif j > direita:
            A[k] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            A[k] = aux[j]
            j += 1
        else:
            A[k] = aux[i]
            i += 1


def mergesort_recursivo(A, aux, esquerda, direita):
    # Se o da direita já estiver maior que o da esquerda, retorna nada
    if direita <= esquerda:
        return
    meio = (esquerda + direita) // 2

    # Ordena a primeira metade do arranjo.
    mergesort_recursivo(A, aux, esquerda, meio)

    # Ordena a segunda metade do arranjo.
    mergesort_recursivo(A, aux, meio + 1, direita)

    # Combina as duas metades ordenadas anteriormente.
    merge_recursivo(A, aux, esquerda, meio, direita)


def merge_iterativo(S, temp, From, mid, to):
 
    a = From
    b = From
    c = mid + 1
 
    while b <= mid and c <= to:
        if S[b] < S[c]:
            temp[a] = S[b]
            b = b + 1
        else:
            temp[a] = S[c]
            c = c + 1
        a = a + 1
 
    while b < len(S) and b <= mid:
        temp[a] = S[b]
        a = a + 1
        b = b + 1
 

    for b in range(From, to + 1):
        S[b] = temp[b]
 
 

def mergesort_iterativo(S):
 
    low = 0
    high = len(S) - 1

    temp = S.copy()
 
    d = 1
    while d <= high - low:
 
        for b in range(low, high, 2*d):
            From = b
            mid = b + d - 1
            to = min(b + 2*d - 1, high)
            merge_iterativo(S, temp, From, mid, to)
        d = 2*d