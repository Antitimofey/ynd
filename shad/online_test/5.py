#=======================имхо нормально работает=============================


import numpy as np
from scipy.sparse import random, csr_matrix
from scipy.sparse.linalg import gmres, bicgstab, spsolve
import time



def generate_odd_matrix(n: int):

    

    A = np.zeros((n//2, n//2), dtype='f')

    A[0][:2] = 1, -1/n
    for i in range(1, n//2 - 1):
        A[i][i-1:i+2] = -1*(n-i-1)/n, 1, -1*(i+1)/n

    A[n//2-1][n//2-2:] = -1*(n - n//2)/n, (n - n//2)/n

    return A


def generate_even_matrix(n: int):
    A = np.zeros((n//2, n//2), dtype='f')

    A[0][:2] = 1, -1/n
    for i in range(1, n//2 - 1):
        A[i][i-1:i+2] = -1*(n-i-1)/n, 1, -1*(i+1)/n

    A[n//2-1][n//2-2:] = -1, 1

    return A


def generate_matrix(n: int):
    if (n % 2 == 0):
        return generate_even_matrix(n)
    return generate_odd_matrix(n)


def get_pos_delta(node_cnt: int, start_pos: int, wanted_pos: int):
    return min(node_cnt - abs(start_pos - wanted_pos), abs(start_pos - wanted_pos))



def main():

    node_count, start_pos, wanted_pos = list(map(int, input().split()))


    # костыль, чтобы не обрабатывать матрицу (1,1)
    if (node_count == 3):
        print(1.5)
        return


    A = generate_matrix(node_count)

    b = np.ones(node_count//2)


    #x, info = gmres(A, b, rtol=1e-6, maxiter=10000)

    x, info = bicgstab(A, b, rtol=1e-6, maxiter=10000)

    #x = spsolve(A, b) # x - не разреженная, долго будет думать

    #print('\ndesigion is', x)
    print(x[get_pos_delta(node_count, start_pos, wanted_pos) - 1])



main()