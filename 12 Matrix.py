import random
from math import sqrt, sin, cos, e, pi
import numpy as np

'''
Все обозначения из книги, читай условия.
M - строка
N - столбец
'''


def N1():
    M = random.randrange(2,10)
    N = random.randrange(2,10)
    print("M = ",M,"; N = ",N)
    a = np.zeros((M, N))
    for i in range(M):
        for j in range(N):
            a[i][j] = (i+1)*10

    print(a)

def N2():
    M = random.randrange(2,10)
    N = random.randrange(2,10)
    print("M = ",M,"; N = ",N)
    a = np.zeros((M, N))
    for i in range(M):
        for j in range(N):
            a[i][j] = (j+1)*5

    print(a)

def N3():
    M = random.randrange(2,10)
    N = random.randrange(2,10)
    A = [random.randint(-10, 10) for i in range(M)]
    print("M = ", M,"; N = ", N, 'A = ', A )
    a = np.zeros((M, N))
    for i in range(M):
        for j in range(N):
            a[i][j] = A[i]

    print(a)


def N4():
    M = random.randrange(2,10)
    N = random.randrange(2,10)
    A = [random.randint(-10, 10) for i in range(N)]
    print("M = ", M,"; N = ", N, 'A = ', A )
    a = np.zeros((M, N))
    for i in range(M):
        for j in range(N):
            a[i][j] = A[j]


    print(a)


def N5():
    M = random.randrange(2,10)
    N = random.randrange(2,10)
    D = random.randrange(2,10)
    A = [random.randint(-10, 10) for i in range(M)]
    print("M = ", M,"; N = ", N, '; A = ', A, '; D = ', D )
    a = np.zeros((M, N))
    for i in range(M):
        for j in range(N):
            a[i][j] = A[i] + D * j

    print(a)

def N6():
    M = random.randrange(2,10)
    N = random.randrange(2,10)
    D = random.randrange(2,10)
    A = [random.randint(-10, 10) for i in range(N)]
    print("M = ", M,"; N = ", N, '; A = ', A, '; D = ', D )
   # a = np.zeros((M, N))
    a = [[0 for i in range(N)] for i in range(M)]

    for i in range(M):
        for j in range(N):
            a[i][j] = A[j] * D**i


    for i in a:
        print(i)


def N7():
    M = random.randrange(2, 10)
    N = random.randrange(2, 10)
    K = random.randrange(1, M)

    print("M = ", M, "; N = ", N, "; K = ", K)
    a = np.zeros((M, N))
    for i in range(M):
        for j in range(N):
            a[i][j] = j*i

    print(a, '\n', '\n', a[K-1])


def N8():
    M = random.randrange(2, 10)
    N = random.randrange(2, 10)
    K = random.randrange(1, N)

    print("M = ", M, "; N = ", N, "; K = ", K)
    a = np.zeros((M, N))
    for i in range(M):
        for j in range(N):
            a[i][j] = j*i

    print(a, '\n', '\n')

    for i in range(M):
        print(a[i][K-1], end = ', ')


def N9():
    M = random.randrange(2, 10)
    N = random.randrange(2, 10)

    print("M = ", M, "; N = ", N)
    a = np.zeros((M, N))
    for i in range(M):
        for j in range(N):
            a[i][j] = j*i

    print(a, '\n', '\n')

    '''
    Выводим элементы с четными номерами из всех строк:
    '''
    for i in range(M):
        for j in range(0, N, 2):
            print(f'Номер элемента {j}, строка {i} - ', a[i][j])

    '''
    Выводим элементы из строк с четными номерами:
    '''
    print()

    for i in range(0, M, 2):
        for j in range(0, N):
            print(f'Номер элемента {j}, строка {i} - ', a[i][j])


def N10():
    M = random.randrange(2, 10)
    N = random.randrange(2, 10)

    print("M = ", M, "; N = ", N)
    a = np.zeros((M, N))
    for i in range(M):
        for j in range(N):
            a[i][j] = j*i

    print(a, '\n', '\n')

    '''
    Выводим элементы с нечетными номерами из всех столбцов:
    '''
    for i in range(N):
        for j in range(1, M, 2):
            print(f'Номер элемента {j}, столбец {i} - ', a[j][i])

    '''
    Выводим элементы из столбцов с нечетными номерами:
    '''
    print()

    for i in range(1, N, 2):
        for j in range(M):
            print(f'Номер элемента {j}, столбец {i} - ', a[j][i])


def N11():
    M = random.randint(2, 10)
    N = random.randint(2, 10)

    print("M = ", M, "; N = ", N)
    a = np.zeros((M,N))
    for i in range(M):
        for j in range(N):
            a[i][j] = j*i

    print(a, '\n', '\n')


    for i in range(M):
        if i%2 == 0:
            for j in range(N):
                print(a[i][j], end = ', ' )
        else:
            for j in range(N, 0, -1):
                k = j - 1
                print(a[i][k], end = ', ')
        print()


def N12():
    M = random.randint(2, 10)
    N = random.randint(2, 10)

    print("M = ", M, "; N = ", N)
    a = np.zeros((M,N))
    for i in range(M):
        for j in range(N):
            a[i][j] = j*i

    print(a, '\n', '\n')


    for i in range(M):
            for j in range(N):
                if j%2 == 0:
                    print(a[i][j], end = ', ')

                else:
                    print(a[M-1-i][j], end = ', ')
            print()


def N13():
    M = random.randint(2, 10)
    print('M = ', M)

    a = np.zeros((M, M))
    for i in range(M):
        for j in range(M):
            a[i][j] = j-1*i*2

    print(a)

    for i in range(M):
        for j in range(M-i):
            print(a[i][j], end = ', ')
            if j == M-i-1:
                print('столбец', end = ', ')
                for k in range(i+1, M):
                    print(a[k][j], end = ', ')
        print()


def N14():
    M = random.randint(2, 10)
    print('M = ', M)

    a = np.zeros((M, M))
    for i in range(M):
        for j in range(M):
            a[i][j] = j*i
    print(a)

    for i in range(M):
        for j in range(M-i):
            print(a[j][i], end = ', ')
            if j == M-i-1:
                print('строка', end = ', ')
                for k in range(i+1, M):
                    print(a[j][k], end = ', ')
        print()


def N15():
    M = 0
    while M%2 == 0 :
        M = random.randint(2, 11)
    print('M = ', M)

    a = np.zeros((M, M))
    for i in range(M):
        for j in range(M):
            a[i][j] = j-1*i*2
    print(a)

    k = 0
    while k <= M//2:
        j = 0 + k
        #print('Горизонталь слева - направо:')
        for i in range(0+k, M-k):
            print(a[j][i], end = ', ')
            if i == M - 1 - k:
                print()
                #print('Вертикаль сверху - вниз:')
                for j in range(1+k, M-k):
                    print(a[j][i], end = ', ')
                    if j == M - 1 - k:
                        print()
                        #print('Горизонталь справа - налево:')
                        for i in range(M-1-k, 0+k, -1):
                            v = i - 1
                            print(a[j][v], end = ', ')
                            if v == 0 + k:
                                print()
                                #print('Горизонталь снизу - вверх:')
                                for j in range(M-1-k, 1+k, -1):
                                    w = j - 1
                                    print(a[w][v], end = ', ')
                                print()

        k+=1



def N16():
    M = 0
    while M%2 == 0 :
        M = random.randint(2, 5)
    print('M = ', M)

    a = np.zeros((M, M))
    for i in range(M):
        for j in range(M):
            a[i][j] = j-1*i*2
    print(a)

    k = 0
    while k <= M//2:
        j = 0 + k
        #print('Горизонталь слева - направо:')
        for i in range(0+k, M-k):
            print(a[i][j], end = ', ')
            if i == M - 1 - k:
                print()
                #print('Вертикаль сверху - вниз:')
                for j in range(1+k, M-k):
                    print(a[i][j], end = ', ')
                    if j == M - 1 - k:
                        print()
                        #print('Горизонталь справа - налево:')
                        for i in range(M-1-k, 0+k, -1):
                            v = i - 1
                            print(a[v][j], end = ', ')
                            if v == 0 + k:
                                print()
                                #print('Горизонталь снизу - вверх:')
                                for j in range(M-1-k, 1+k, -1):
                                    w = j - 1
                                    print(a[v][w], end = ', ')
                                print()

        k+=1


def N17():
    M = random.randrange(2, 10)
    N = random.randrange(2, 10)
    K = random.randrange(1, M)

    print("M = ", M, "; N = ", N, "; K = ", K)
    a = np.zeros((M, N))
    for i in range(M):
        for j in range(N):
            a[i][j] = j*i

    print(a, '\n', '\n')

    Summa = 0
    Product = 1

    for i in range(N):
        Summa += a[K][i]
        Product *= a[K][i]
        print(a[K][i], end = ', ')
    print()
    print('Summa = ', Summa, 'Product = ', Product)



def N18():
    M = random.randrange(2, 10)
    N = random.randrange(2, 10)
    K = random.randrange(1, M)

    print("M = ", M, "; N = ", N, "; K = ", K)
    a = np.zeros((M, N))
    for i in range(M):
        for j in range(N):
            a[i][j] = j*i

    print(a, '\n', '\n')

    Summa = 0
    Product = 1

    for i in range(M):
        Summa += a[i][K]
        Product *= a[i][K]
        print(a[i][K], end = ', ')
    print()
    print('Summa = ', Summa, 'Product = ', Product)



def N19():
    M = random.randrange(2, 10)
    N = random.randrange(2, 10)


    print("M = ", M, "; N = ", N)
    a = np.zeros((M, N))
    for i in range(M):
        for j in range(N):
            a[i][j] = j*i

    print(a, '\n', '\n')


    Summa_m = {}
    for j in range(M):
        Summa = 0
        for i in range(N):
            Summa += a[j][i]
            print(a[j][i], end = ', ')
        print()
        Summa_m[j] = Summa


    print()
    print('Summa = ', Summa_m)



def N20():
   M = random.randrange(2, 10)
   N = random.randrange(2, 10)


   print("M = ", M, "; N = ", N)
   a = np.zeros((M, N))
   for i in range(M):
       for j in range(N):
           a[i][j] = j+1*i

   print(a, '\n', '\n')


   Product_m = {}
   for j in range(N):
       Product = 1
       for i in range(M):
           Product *= a[i][j]
           print(a[i][j], end = ', ')
       print()
       Product_m[j] = Product


   print()
   print('Product = ', Product_m)


def N21():
   M = random.randrange(2, 10)
   N = random.randrange(2, 10)


   print("M = ", M, "; N = ", N)
   a = np.zeros((M, N))
   for i in range(M):
       for j in range(N):
           a[i][j] = j+1*i

   print(a, '\n', '\n')


   Averaged_d = {}
   for i in range(1, M, 2):
       Averaged = 0
       for j in range(N):
           Averaged += a[i][j]
           print(a[i][j], end = ', ')
       print()
       Averaged_d[i] = Averaged / (j+1)


   print()
   print('Averaged = ', Averaged_d)



def N22():
   M = random.randrange(2, 10)
   N = random.randrange(2, 10)


   print("M = ", M, "; N = ", N)
   a = np.zeros((M, N))
   for i in range(M):
       for j in range(N):
           a[i][j] = j+1*i

   print(a, '\n', '\n')


   Averaged_d = {}
   for i in range(0, N, 2):
       Averaged = 0
       for j in range(M):
           Averaged += a[j][i]
           print(a[j][i], end = ', ')
       print()
       Averaged_d[i] = Averaged / (j+1)


   print()
   print('Averaged = ', Averaged_d)


def N23():
   M = random.randrange(2, 10)
   N = random.randrange(2, 10)


   print("M = ", M, "; N = ", N)
   a = np.zeros((M, N))
   for i in range(M):
       for j in range(N):
           a[i][j] = random.randint(0, 15)

   print(a, '\n', '\n')


   for i in range(M):
       Min = 10**10
       for j in range(N):
           print(a[i][j], end = ', ')
           if a[i][j] < Min:
               Min = a[i][j]
       print()
       print(f'{i}:', i, '\t Min = ', Min)



       print()



def N24():
   M = random.randrange(2, 10)
   N = random.randrange(2, 10)


   print("M = ", M, "; N = ", N)
   a = np.zeros((M, N))
   for i in range(M):
       for j in range(N):
           a[i][j] = random.randint(0, 15)

   print(a, '\n', '\n')


   for i in range(N):
       Max = 10**(-10)
       for j in range(M):
           print(a[j][i], end = ', ')
           if a[j][i] > Max:
               Max = a[j][i]
       print()
       print(f'{i}:', i, '\t Max = ', Max)



       print()

'''
С 25 по 30, задачи довольно однотипны и невызывают интереса.
'''



def N31():
    M = random.randrange(2, 10)
    N = random.randrange(2, 10)


    print("M = ", M, "; N = ", N)
    a = np.zeros((M, N))

    for i in range(M):
        for j in range(N):
            a[i][j] = random.randint(0, 15)

    print(a, '\n', '\n')

    Avr = 0
    for i in range(M):
        for j in range(N):
           Avr+= a[i][j]
    Avr /= M * N
    print('Avr = ', Avr)

    delta = 0
    Avr_close = 10**10
    for i in range(M):
        for j in range(N):
            delta = abs(Avr - a[i][j])
            if delta < Avr_close:
                Avr_close = delta
                row = i
                colomn = j
    print('Row:', row+1, '\nColomn:', colomn+1, '\nNumber = ', a[row][colomn])







N31()



















