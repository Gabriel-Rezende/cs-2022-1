
from ordenacao import *
import random
import time


if __name__ == '__main__':
    # Rodando Recursivamente para 100 registros
    start = time.time()
    A = random.sample(range(0, 100), 100)
    aux = [0] * len(A)
    mergesort_recursivo(A, aux, 0, len(A) - 1)
    print('MergeSort Recursivo 100 registros: ', time.time()-start, 'segundos.')

    # Rodando Recursivamente para 1000 registros
    start = time.time()
    A = random.sample(range(0, 1000), 1000)
    aux = [0] * len(A)
    mergesort_recursivo(A, aux, 0, len(A) - 1)
    print('MergeSort Recursivo 1000 registros: ', time.time()-start, 'segundos.')

    # Rodando Recursivamente para 10000 registros
    start = time.time()
    A = random.sample(range(0, 10000), 10000)
    aux = [0] * len(A)
    mergesort_recursivo(A, aux, 0, len(A) - 1)
    print('MergeSort Recursivo 10000 registros: ', time.time()-start, 'segundos.')

    # Rodando iterativamente para 100 registros
    start = time.time()
    A = random.sample(range(0, 100), 100)
    aux = [0] * len(A)
    mergesort_iterativo(A)
    print('MergeSort Iterativo 100 registros: ', time.time()-start, 'segundos.')

    # Rodando iterativamente para 1000 registros
    start = time.time()
    A = random.sample(range(0, 1000), 1000)
    aux = [0] * len(A)
    mergesort_iterativo(A)
    print('MergeSort Iterativo 1000 registros: ', time.time()-start, 'segundos.')

    # Rodando iterativamente para 10000 registros
    start = time.time()
    A = random.sample(range(0, 10000), 10000)
    aux = [0] * len(A)
    mergesort_iterativo(A)
    print('MergeSort Iterativo 10000 registros: ', time.time()-start, 'segundos.')