1#
'''
import random
N = random.randint(5,10)
print(N)
M = [i*2+1 for i in range(N)]
print(M)
'''
2#
'''
import random
N = random.randint(5,10)
print(N)
M = [2**i for i in range(1,N)]
print(M )
'''
3#
'''
import random
N = random.randint(1,10)
A = random.randint(1,10)
D = random.randint(1,10)
print(N,A,D)
M = [A+i*D for i in range(N)]
print(M)

'''
4#
'''
import random
N = random.randint(1,10)
A = random.randint(1,10)
D = random.randint(1,10)
print(N,A,D)
M = [A*D**i for i in range(N)]
print(M)
'''

5#
'''
import random
N = random.randint(2,100)
print(N)
a = [1,1]
for i in range(2,N):
    x = a[i-2] + a[i-1]
    a.append(x)
print(a)
'''


6#
'''
import random
N = random.randint(2, 10)
A = random.randint(2, 10)
B = random.randint(2, 10)

print(N,A,B)
a = [A,B]
while N > 0:
    x=0
    for i in a:
        x+=i
    a.append(x)
    N-=1

print(a)
'''

7#
'''
import random
N = random.randint(5, 10)
print(N)
a=[i for i in range(N,1,-1)]
print(a)
print()
m = [i for i in range(N)]
print(m)

k = []
for i in m[::-1]:
    k.append(i)
print(k)
'''




import random

def N8():
    N = random.randint(5, 10)
    print(N)
    a = [random.randint(1, 20) for i in range(N)]
    print(a)
    index = 0
    call = 0
    print('Нечетное число;', 'Индекс;')
    for i in a:
        if i % 2!=0:
            print(i,'-', index)
            call+=1
        index+=1
    print('\n',call)



def N9():
    N = random.randint(5, 10)
    print(N)
    a = [random.randint(1, 20) for i in range(N)]
    print(a)
    index = len(a)-1
    call = 0
    print('Четное число;', 'Индекс;')
    for i in a[::-1]:
        if i % 2==0:
            print(i,'-', index)
            call+=1
        index-=1
    print('\n',call)




def N10():
    N = random.randint(5, 10)
    print(N)
    a = [random.randint(1, 20) for i in range(N)]
    print(a)
    index = 0
    call = 0
    print('Четное число;', 'Индекс;')
    for i in a:
        if i % 2==0:
            print(i,'-', index)
            call+=1
        index+=1
    print('\n',call)
    print()
    index = len(a)-1
    call = 0
    print('Нечетное число;', 'Индекс;')
    for i in a[::-1]:
        if i % 2!=0:
            print(i,'-', index)
            call+=1
        index-=1
    print('\n',call)




def N11():
    N = random.randint(10, 15)
    K = random.randint(1, N)
    A = [random.randint(1, 20) for i in range(N)]
    print(N,';',K,';',A)
    n = K
    while n < N:
        n += K
        print(n,';',A[n])


def N12():
    N = 1
    while N%2 != 0:
        N = random.randint(2, 20)
    print(N)
    A = [random.randint(1, 20) for i in range(N)]
    print(A)
    i = 0
    while i != len(A):
        print(i,';',A[i])
        i+=2

# 13,14,15 - Похожие, скучные условия

def N16():
    N = random.randint(5, 15)
    A = [i for i in range(N)]
    B = []
    print(N,';',A)
    print()
    k = -1
    for i in range(N):
        B.append(A[i])
        if N%2 != 0:
             if A[i] == A[int(N/2) + 1]:
                 break
             if A[i] == A[int(N/2)]:
                 break
        B.append(A[k])
        if A[i+1] == A[k]:
            break
        k-=1
    print(B)


def N17():
    N = random.randint(5, 15)
    A = [i for i in range(N)]
    B = []
    print(N,';',A)
    print()
    k = -1
    j = 0
    for i in range(N):
        B.append(A[j])
        if len(B) == len(A):
            break
        B.append(A[j+1])
        if len(B) == len(A):
            break
        B.append(A[k])
        if len(B) == len(A):
            break
        B.append(A[k-1])
        if len(B) == len(A):
            break
        k-=2
        j+=2
    print(B)



def N18():
    A = [random.randint(1, 20) for i in range(10)]
    print(A)
    flag = True
    for i in range(len(A)-1):
        if A[i] < A[-1]:
            print(i,':',A[i])
            flag = False
            break
    if flag == True:
        print(0)



def N19():
    A = [random.randint(1, 20) for i in range(10)]
    print(A)
    flag = True
    for i in range(len(A)-1):
        if A[0] < A[i] and A[i] < A[-1]:
            print(i,':',A[i])
            flag = False
            break
    if flag == True:
        print(0)



def N20():
    N = random.randint(5, 20)
    L = random.randint(4, N-1)
    K = random.randint(2, L-1)
    print('N =',N,'K =',K,'L =',L)
    A = [random.randint(2, 20) for i in range(N)]
    print('A =',A)
    S = 0
    print('Interval:')
    for i in range(K,L+1):
        print(A[i] ,end=' ')
        S+=A[i]
    print()
    print('S = ',S)





def N21():
    N = random.randint(5, 20)
    L = random.randint(4, N-1)
    K = random.randint(2, L-1)
    print('N =',N,'K =',K,'L =',L)
    A = [random.randint(2, 20) for i in range(N)]
    print('A =',A)
    S = 0
    total_number = L - K +1
    print('TL = ', total_number)
    print('Interval:')
    for i in range(K,L+1):
        print(A[i] ,end=' ')
        S+=A[i]
    print()
    print('S = ', S/total_number )


def N22():
    N = random.randint(5, 20)
    L = random.randint(4, N-1)
    K = random.randint(2, L-1)
    print('N =',N,'K =',K,'L =',L)
    A = [random.randint(2, 20) for i in range(N)]
    print('A =',A)
    S = 0
    Left = A[0:K:1]
    Right = A[L+1:N:1]
    New = Left+Right
    for i in New:
        S+=i
    print()
    print(Left,Right)
    print('S = ',S)

    A1 = [j for i, j in enumerate(A) if i not in range(K,L+1)]
    print()
    print(A1)


def N23():
    N = random.randint(5, 20)
    L = random.randint(4, N-1)
    K = random.randint(2, L-1)
    print('N =',N,'K =',K,'L =',L)
    A = [random.randint(2, 20) for i in range(N)]
    print('A =',A)
    S = 0
    Left = A[0:K:1]
    Right = A[L+1:N:1]
    New = Left+Right
    for i in New:
        S+=i
    S = S/len(New)
    print()
    print(Left,Right)
    print('S = ',S)
    print()



def N24():
    A = [random.randint(2, 20) for i in range(15)]
    B = []
    for i in A:
        if i not in B:
            B.append(i)
    C = []
    for i in range(len(B)-1):
        C.append(B[i+1]-B[i])
    print(B,'\n',C)
    if C[0] == C[-1]:
        print(C[0])
    else:
        print(0)

def N25():
    pass

def N26():
     N = random.randint(2, 10)
     A = [random.randint(1, 10) for i in range(N)]
     print(A)
     index = 0
     for i in range(len(A)-1):
         if (A[i]%2 == 0) == (A[i+1] % 2 == 0):
             index = i +1
             break
     print(index)

def N27():
     N = random.randint(2, 10)
     A = [random.randint(-10, 10) for i in range(N)]
     print(A)
     index = 0
     for i in range(len(A)-1):
         if (A[i] > 0) == (A[i+1] > 0):
             index = i + 1
             break
     print(index)


def N28():
      N = random.randint(2, 10)
      A = [random.randint(1, 20) for i in range(N)]
      print(A)
      print(A[0::2])
      print(min(A[0::2]))

def N29():
      N = random.randint(2, 10)
      A = [random.randint(1, 20) for i in range(N)]
      print(A)
      print(A[1::2])
      print(max(A[1::2]))


def N30():
    N = random.randint(2, 15)
    A = [random.randint(1, 20) for i in range(N)]
    print(A)
    counter = 0
    for i in range(len(A)-1):
        if A[i] > A[i+1]:
            print('Номер элемента: ',i)
            counter+=1
    print()
    print('Общие количество элементов: ',counter)

def N31():
    N = random.randint(2, 15)
    A = [random.randint(1, 20) for i in range(N)]
    print(A)
    counter = 0
    for i in range(len(A)-1,0,-1):
        if A[i] > A[i-1]:
            print('Номер элемента: ',i)
            counter+=1
    print()
    print('Общие количество элементов: ',counter)



def N32():
    N = random.randint(2, 15)
    A = [random.randint(1, 20) for i in range(N)]
    print(A)
    for i in range(1,len(A)-2):
        if  A[i-1] > A[i] < A[i+1]:
            print('Номер элемента: ',i)
            break
    print()


def N33():
    N = random.randint(2, 15)
    A = [random.randint(1, 20) for i in range(N)]
    print(A)
    for i in range(len(A)-2,0,-1):
        if  A[i-1] < A[i] > A[i+1]:
            print('Номер элемента: ',i)
            break
    print()

def N34():
    N = random.randint(2, 15)
    A = [random.randint(1, 20) for i in range(N)]
    B = []
    print(A)
    for i in range(1,len(A)-2):
        if  A[i-1] > A[i] < A[i+1]:
            B.append(A[i])
            print('Номер элемента: ',i,';',A[i])
    print()
    if B:
        print(max(B))


def N35():
    N = random.randint(2, 15)
    A = [random.randint(1, 20) for i in range(N)]
    print(A)
    B = []
    for i in range(len(A)-2,0,-1):
        if  A[i-1] < A[i] > A[i+1]:
            B.append(A[i])
            print('Номер элемента: ',i,';',A[i])

    print()
    if B:
        print(min(B))




def N36():
    N = random.randint(2, 15)
    A = [random.randint(1, 20) for i in range(N)]
    print(A)
    B = []
    #B.append(A[0])

    for i in range(1,len(A)-1):
        if (A[i-1] < A[i] > A[i+1]) or (A[i-1] > A[i] < A[i+1]):
            print(i,A[i])
        else:
            B.append(A[i])
    #B.append(A[-1])
    print()
    print(B)
    if B:
        print(max(B))
    else:
        print(0)



def N37():
    N = random.randint(2, 15)
    A = [random.randint(1, 6) for i in range(N)]
    print(A)
    flag = True
    counter = 0
    for i in range(len(A)-1):
        if A[i] < A[i+1]:
            print(A[i])
            if flag:
                counter+=1
                flag = False
        else:
            flag = True
    print()
    print(counter)


def N38():
    N = random.randint(2, 15)
    A = [random.randint(1, 6) for i in range(N)]
    print(A)
    flag = True
    counter = 0
    for i in range(len(A)-1):
        if A[i] > A[i+1]:
            print(A[i])
            if flag:
                counter+=1
                flag = False
        else:
            flag = True
    print()
    print(counter)







def N39():
    N = random.randint(2, 15)
    A = [random.randint(1, 6) for i in range(N)]
    print(A)
    flag = True
    counter = 0
    for i in range(len(A)-1):
        if A[i] < A[i+1]:
            if flag:
                counter+=1
                flag = False
        else:
            flag = True

    flag = True
    for i in range(len(A)-1):
        if A[i] > A[i+1]:
            if flag:
                counter+=1
                flag = False
        else:
            flag = True
    print()

    print(counter)




def N40():
    N = random.randint(3, 15)
    R = random.randint(6, 12)
    A = [random.uniform(1, 20) for i in range(N)]
    print(N, R, A)
    Min = abs(R-A[0])
    i_min = 0
    for i in A:
        if abs(R-i) < Min:
            Min = abs(R-i)
            i_min = i
    print(i_min)


def N41():
     N = random.randint(3, 15)
     A = [random.randint(1, 20) for i in range(N)]
     print(A)
     Max = 0
     i_1 = 0
     i_2 = 0
     for i in range(len(A)-1):
         if (A[i] + A[i+1]) > Max:
             Max = (A[i] + A[i+1])
             i_1 = A[i]
             i_2 = A[i+1]

     print(i_1, i_2)


def N42():
    N = random.randint(3, 15)
    R = random.randint(6, 20)
    A = [random.randint(1, 12) for i in range(N)]
    print(N, R, A)
    Min = 10**6
    i_1 = 0
    i_2 = 0
    for i in range(len(A)-1):
        if abs(R-(A[i]+A[i+1])) < Min:
            Min = abs(R-(A[i]+A[i+1]))
            i_1 = A[i]
            i_2 = A[i+1]

    print(Min, i_1, i_2)


def N43():
     N = random.randint(3, 15)
     A = [i for i in range(N)]
     B = sorted([random.randint(1,10) for i in range(N)])
     print(A,'\n',B)
     print()
     C_1 = []
     C_2 = []
     k = 0
     for i in A:
         if i not in C_1:
             C_1.append(i)
     for i in C_1:
         k+=1
     print('КОличество элементов в списке А: ',k)

     k = 0
     for i in B:
         if i not in C_2:
             C_2.append(i)
     for i in C_2:
         k+=1
     print('КОличество элементов в списке B: ',k)



def N44():
     N = random.randint(3, 15)
     A = [i for i in range(N)]
     A.append(N-2)
     print(A)
     flag = False
     for i in range(len(A)):
         for j in range(i+1, len(A)):
             if A[i] == A[j]:
                 print(i, j)
                 flag = True
                 break
         if flag:
             break

def N45():
    N = random.randint(3, 15)
    A = [random.randint(1, 20) for i in range(N)]
    print(A)
    Min = 10**6
    i_1 = None
    i_2 = None
    for i in range(len(A)-1):
        if abs(A[i]-A[i+1]) < Min:
            Min = abs(A[i]-A[i+1])
            i_1 = i
            i_2 = i+1

    print(i_1, i_2)



def N46():
    N = random.randint(3, 15)
    R = random.randint(6, 20)
    A = [random.randint(1, 12) for i in range(N)]
    print(N, R, A)
    Min = 10**6
    i_1 = 0
    i_2 = 0
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if abs(R-(A[i]+A[j])) < Min:
                Min = abs(R-(A[i]+A[j]))
                i_1 = i
                i_2 = j

    print(Min, i_1, i_2)


def N47():
     N = random.randint(3, 15)
     A = ([random.randint(1,15) for i in range(N)])
     print(A)
     print()
     C_1 = []
     k = 0
     for i in A:
         if i not in C_1:
             C_1.append(i)
     for i in C_1:
         k+=1
     print('КОличество уникальных элементов в списке А: ',k)


def N48():
     N = random.randint(3, 15)
     A = ([random.randint(1,6) for i in range(N)])
     print(A)
     counter = 1
     max_counter = 0
     index = None
     for i in range(len(A)):
         counter = 1
         for j in range(i+1,len(A)):
             if A[i] == A[j]:
                 counter+=1
                 if counter > max_counter:
                     max_counter = counter
                     index = A[i]
     print(index,max_counter)



def N49():
     N = random.randint(3, 15)
     A = [i for i in range(N)]
     B = ([random.randint(1,16) for i in range(N)])
     print(B)
     flag = False
     for i in range(len(A)):
         if B[i] not in A:
             print(B[i],i)
             flag = True
             break
     if flag == False:
         print(0)


def N50():

    flag = True
    while flag:
        N = random.randint(3, 15)
        A = [i for i in range(N)]
        B = ([random.randint(1,16) for i in range(N)])
        flag = False
        for i in range(len(A)):
            if B[i] not in A:
                flag = True
        if flag == False:
            print(N,B)

    counter = 0
    for i in range(len(B)):
        for j in range(i+1,len(B)):
            if B[i] > B[j]:
                counter+=1

    print(counter)






def N51():
    N = random.randint(3, 10)
    A = [random.randint(1, 15) for i in range(N)]
    B = [random.randint(1, 15) for i in range(N)]
    print(A,B)
    A,B = B,A
    print(A,B)




def N52():
    N = random.randint(3, 10)
    A = [random.randint(1, 15) for i in range(N)]
    B = []
    print(A)
    for i in range(len(A)):
        B.append(2*A[i] if A[i] < 5 else A[i]/2)
    print(B)



def N53():
    N = random.randint(3, 10)
    A = [random.randint(1, 15) for i in range(N)]
    B = [random.randint(1, 15) for i in range(N)]
    C = []
    print(A,'\n',B)
    for i in range(len(A)):
        C.append(max(A[i],B[i]))
    print(C)


def N54():
    N = random.randint(3, 10)
    A = [random.randint(1, 15) for i in range(N)]
    B = []
    print(A)
    for i in range(len(A)):
        if A[i]%2 == 0 :
            B.append(A[i])
    print(B,len(B))


def N55():
    N = random.randint(2, 16)
    A = [random.randint(1, 15) for i in range(N)]
    B = []
    print(A)
    B = A[1::2]
    print(B)


def N56():
    N = random.randint(2, 16)
    A = [random.randint(1, 15) for i in range(N)]
    B = []
    print(A)
    B = A[0::3]
    print(B)


def N57():
    N = random.randint(2, 16)
    A = [random.randint(1, 15) for i in range(N)]
    B = []
    print(A)
    B = A[0::2] + A[1::2]
    print(B)


def N58():
    N = random.randint(2, 16)
    A = [random.randint(1, 15) for i in range(N)]
    A = [i for i in range(N)]
    B = []

    print(A)
    for i in range(len(A)):
        S = 0
        for j in range(i+1):
            S+=A[j]
        B.append(S)
    print(B)


    '''for i in range(1,N) :
    b.append(a[i] + b[i-1])
    '''

def N59():
    N = random.randint(2, 16)
    A = [random.randint(1, 15) for i in range(N)]
    A = [i for i in range(N)]
    B = []

    print(A)
    for i in range(len(A)):
        S = 0
        for j in range(i+1):
            S+=A[j]
        if j == 0 :
            j = 1
        S = S/j
        B.append(S)
    print(B)



def N60():
   N = random.randint(5, 15)
   A = [random.randint(1, 15) for i in range(N)]
   print(A)
   B = []
   for i in range(len(A)):
       s = 0
       for j in range(i,len(A)):
           s+=A[j]
       B.append(s)
   print(B)


def N61():
   N = random.randint(5, 6)
   A = [random.randint(1, 15) for i in range(N)]
   print(A)
   B = []
   for i in range(len(A)):
       s = 0
       for j in range(i,len(A)):
           s+=A[j]
       s = s/(j-i+1)
       B.append(s)
   print(B)



def N62():
    N = random.randint(5,10)
    A = [random.randint(-10, 10) for i in range(N)]
    print(N,A)
    B = []
    C = []
    for i in A:
        if i >= 0:
            B.append(i)
        else:
            C.append(i)
    print(len(B),B)
    print(len(C),C)

def N63():
    N = 5
    a = sorted([random.randrange(0,10) for i in range(N)])
    b = sorted([random.randrange(0,10) for i in range(N)])
    print("Array a:\n",a)
    print("Array b:\n",b)
    c = sorted(a+b)
    print("Length of c:\n",len(c))
    print("Array c:\n",c)

    c_2 = []
    i = 0
    j = 0
    while len(c_2) < len(a+b):
        if j == len(b) and i < len(a):
            c_2.append(a[i])
            i+=1
            continue
        if i < len(a) and a[i] <= b[j]:
            c_2.append(a[i])
            i+=1
        else:
            c_2.append(b[j])
            j+=1
    print(c_2)



def N64():
    N_a = random.randint(3,6)
    N_b = random.randint(3,6)
    N_c = random.randint(3,6)
    a = sorted([random.randint(0, 10) for i in range(N_a)], reverse=True)
    b = sorted([random.randint(0, 10) for i in range(N_b)], reverse=True)
    c = sorted([random.randint(0, 10) for i in range(N_c)], reverse=True)
    print(a,b,c)
    d = sorted(a+b+c,reverse=True)
    print("Length of c:\n",len(d))
    print("Array c:\n", d)

    d_2,d_3 = [],[]
    i,j = 0,0

    while len(d_3) < len(a+b):
        if j == len(b) and i < len(a):
            d_3.append(a[i])
            i+=1
            continue
        if i < len(a) and a[i] >= b[j]:
            d_3.append(a[i])
            i+=1
        else:
            d_3.append(b[j])
            j+=1
    i,j = 0,0
    while len(d_2) < len(a+b+c):
        if j == len(c) and i < len(d_3):
            d_2.append(d_3[i])
            i+=1
            continue
        if i < len(d_3) and d_3[i] >= c[j]:
            d_2.append(d_3[i])
            i+=1
        else:
            d_2.append(c[j])
            j+=1
    print(d_2)



def N65():
    N = random.randint(5, 10)
    K = random.randint(0, N-1)
    A = [random.randint(0,10) for i in range(N)]
    print(N,K,A)
    x = A[K]
    for i in range(len(A)):
        A[i]+=x
    print(A)


def N66():
    N = random.randint(5, 10)
    A = [random.randint(0,10) for i in range(N)]
    print(A)

    x = 0
    for i in range(len(A)):
        if A[i]%2 == 0:
            x = A[i]
            print(x)
            break

    for i in range(len(A)):
        if A[i]%2 == 0:
            A[i]+=x
    print(A)


def N67():
    N = random.randint(5, 10)
    A = [random.randint(0,10) for i in range(N)]
    print(A)

    x = 0
    for i in range(len(A)-1,0,-1):
        if A[i]%2 != 0:
            x = A[i]
            print(x)
            break

    for i in range(len(A)):
        if A[i]%2 != 0:
            A[i]+=x
    print(A)


def N68():
    N = random.randint(5,10)
    A = [random.randint(0,10) for i in range(N)]
    print(A)

    Min = min(A)
    Min_ind = A.index(Min)
    Max = max(A)
    Max_ind = A.index(Max)

    A[Min_ind],A[Max_ind] = A[Max_ind],A[Min_ind]
    print(A)
    A[Min_ind],A[Max_ind] = A[Max_ind],A[Min_ind]

    "OR"

    Min,Max = 1000,-1000
    Min_ind,Max_ind = 0,0
    for i in range(len(A)):
        if A[i] < Min:
            Min = A[i]
            Min_ind = i
        if A[i] > Max:
            Max = A[i]
            Max_ind = i

    A[Min_ind],A[Max_ind] = A[Max_ind],A[Min_ind]
    print(A)


def N69():
    N = 2 * random.randrange(1,9)
    A = [random.randint(0, 10) for i in range(N)]
    print(A)

    i,j = 0,1
    for k in range(len(A)//2):
        A[i],A[j] = A[j],A[i]
        i+=2
        j+=2
    print(A)


def N70():
    N = 2 * random.randrange(1,9)
    A = [random.randint(0, 10) for i in range(N)]
    print(A)

    left = A[0:len(A)//2:1]
    print(left)
    right = A[len(A)//2:len(A):1]
    print(right)
    left,right = right,left
    A_new = left+right
    print(A_new)


def N71():
    N = random.randint(5, 10)
    A = [random.randint(0,10) for i in range(N)]
    print(A)

    for i in range(len(A)//2):
        A[i],A[N-i-1] = A[N-i-1],A[i]
    print(A)

def N72():
    N = random.randint(5, 10)
    A = [random.randint(0,10) for i in range(N+1)]
    print(A)
    L = random.randint(3,N)
    K = random.randint(1,L)

    i = 0
    while i < (L-K+1)//2 :
        print(A[K+i],A[L-i])
        A[K+i],A[L-i] = A[L-i],A[K+i]
        i+=1
    print(K,L,A)


def N73():
    N = random.randint(8, 15)
    A = [random.randint(0,10) for i in range(N+1)]
    print(A)
    L = random.randint(5,N)
    K = random.randint(1,L)

    i = 1
    while i < (L-K+1)//2 :
        print(A[K+i],A[L-i])
        A[K+i],A[L-i] = A[L-i],A[K+i]
        i+=1
    print(K,L,A)





def N74():
    N = random.randint(5,10)
    A = [random.randint(0,10) for i in range(N)]
    print(A)

    Min,Max = 1000,-1000
    Min_ind,Max_ind = 0,0
    for i in range(len(A)):
        if A[i] < Min:
            Min = A[i]
            Min_ind = i
        if A[i] > Max:
            Max = A[i]
            Max_ind = i



    if Min_ind < Max_ind:
        start_ind = Min_ind
        end_ind = Max_ind
    else:
        start_ind = Max_ind
        end_ind = Min_ind

    i = start_ind + 1
    while i < end_ind:
        A[i] = 0
        i+=1


    print(Min_ind,Max_ind)
    print(Min,Max)
    print(A)




def N75():
    N = random.randint(5,10)
    A = [random.randint(0,10) for i in range(N)]
    print(A)

    Min,Max = 1000,-1000
    Min_ind,Max_ind = 0,0
    for i in range(len(A)):
        if A[i] < Min:
            Min = A[i]
            Min_ind = i
        if A[i] > Max:
            Max = A[i]
            Max_ind = i

    if Min_ind < Max_ind:
        start_ind = Min_ind
        end_ind = Max_ind
    else:
        start_ind = Max_ind
        end_ind = Min_ind

    i = start_ind
    j = end_ind
    for k in range(abs((start_ind - end_ind))//2 + 1):
        A[i],A[j] = A[j],A[i]
        i+=1
        j-=1


    print(Min_ind,Max_ind)
    print(Min,Max)
    print(A)

def N76():
    N = random.randint(5,10)
    A = [random.randint(0,10) for i in range(N)]
    B = []
    print(A)
    for i in range(1,len(A)-1):
        if A[i]>A[i-1] and A[i]>A[i+1]:
            B.append(i)
    for j in B:
        A[j] = 0
    print(A)
    '''Нужно сначала найти все эти локальные, и только после обнулять, иначе
    Мы начнем обнулять во время поиска и обнулим весь массив, поиск будет некорректным'''


def N77():
    N = random.randint(5,10)
    A = [random.randint(0,10) for i in range(N)]
    B = []
    print(A)
    for i in range(1,len(A)-1):
        if A[i]<A[i-1] and A[i]<A[i+1]:
            B.append(i)
    for j in B:
        A[j] = A[j]**2

    print(A)


def N78():
    N = random.randint(5,10)
    A = [random.randint(0,10) for i in range(N)]
    B = []
    print(A)
    B.append((A[0]+A[1]) / 2)
    for i in range(1,len(A)-1):
        B.append((A[i]+A[i+1]+A[i-1]) / 3)
    B.append((A[-1]+A[-2]) / 2)
    print(B)

def N79():
    N = random.randint(5, 10)
    A = [random.randint(0, 10) for i in range(N)]
    print(A)
    for i in range(len(A)-1,-1,-1):
        A[i] = A[i-1]
        if i == 0:
            A[i] = 0
    print(A)

def N80():
    N = random.randint(5, 10)
    A = [random.randint(0, 10) for i in range(N)]
    print(A)
    for i in range(0,len(A)-1):
        A[i] = A[i+1]
        if i+1 == len(A)-1:
            A[i+1] = 0
    print(A)


def N81():
    N = random.randint(5, 10)
    K = random.randint(1,N)
    A = [random.randint(0, 10) for i in range(N)]
    print(A,';',K)
    for i in range(0,len(A)-K):
        A[K+i] = A[i]

    for i in range(0,K):
        A[i] = 0
    print(A)

def N82():
    N = random.randint(5, 10)
    K = random.randint(1,N)
    A = [random.randint(0, 10) for i in range(N)]
    print(A,';',K)
    k = 0
    for i in range(len(A)-1,K,-1):
        A[K-k] = A[i]
        k+=1

    for i in range(len(A)-1,K,-1):
        A[i] = 0
    print(A)


def N83():
     N = random.randint(5, 10)
     A = [i for i in range(N)]
     print(A)
     B = A[-1]
     for i in range(len(A)-1,0,-1):
         A[i] = A[i-1]
     A[0] = B
     print(A)


def N84():
     N = random.randint(5, 10)
     A = [i for i in range(N)]
     print(A)
     B = A[0]
     for i in range(0,len(A)-1):
         A[i] = A[i+1]
     A[-1] = B
     print(A)


def N85():
    N = random.randint(5, 10)
    A = [i for i in range(N)]
    B = []
    K = random.randint(1,4)
    print(A,K)
    for i in range(K):
        B.append(A[-K+i])
    for i in range(0,len(A)-K):
        B.append(A[i])
    print(B)




def N86():
    N = random.randint(5, 10)
    A = [i for i in range(N)]
    B = []
    K = random.randint(1,4)
    print(A,K)

    for i in range(K,len(A)):
        B.append(A[i])
    for i in range(K):
        B.append(A[i])
        '''По сути я делаю срезу массива, но не пользуюсь встроенными.
        Можно решить через срез, разбить на 2 среза и соединить в обратном порядке,
        вот и все.'''
    print(B)



def N87():
    N = random.randint(3, 10)
    K = random.randint(1, 10)
    A = [i for i in range(N)]
    A[0]=K
    i = 0
    while A[i] > A[i+1]:
        M = A[i+1]
        if A[i]>A[i+1]:
            A[i+1] = A[i]
            A[i] = M
        i+=1
        if i+1 == len(A):
            break

    print(A)



def N88():
    N = random.randint(6, 10)
    K = random.randint(1, 6)
    A = [i for i in range(N)]
    A[-1] = K
    i = -1
    print(A)
    while A[i] < A[i-1]:
        M = A[i-1]
        if A[i] < A[i-1]:
            A[i-1] = A[i]
            A[i] = M
        i-=1
        if abs(i-1) == len(A):
            break
    print(A)


def N89():
    N = random.randint(8, 12)
    K = random.randint(1, 12)
    P = random.randint(1,11)
    A = [i for i in range(N)]
    A[P] = K
    print(A)
    i = 0
    flag = True
    while flag:
        if A[i] > A[i+1]:
            A[i+1],A[i] = A[i],A[i+1]
            flag = False
        i+=1
        if A[i] < A[i-1]:
            A[i+1],A[i] = A[i],A[i+1]

    print(A)


def N90():
    N = random.randint(8,12)
    K = random.randint(1,N)
    A = [i for i in range(N)]
    print(A, K)
    A.pop(K)
    print(A)

def N91():
    N = random.randint(8,16)
    L = random.randint(3,N)
    K = random.randint(1,L)
    A = [i for i in range(N)]
    print(f'От {K} до {L} длина - {len(A)} {A}')
    del A[K:L+1]
    print(f'длина - {len(A)} {A}')

def N92():
    N = random.randint(8,16)
    A = [i for i in range(N)]
    print(len(A), '; ', A)
    A = [i for i in A if i%2==0]

    '''for i in A:
        if i % 2 != 0:
            A.pop(A.index(i))'''
    print(len(A), '; ', A)

def N93():
    N = random.randint(8,16)
    A = [i for i in range(N)]
    print(len(A), '; ', A)
    del A[::2]
    print(len(A), '; ', A)

def N94():
    N = random.randint(8,16)
    A = [i for i in range(N)]
    print(len(A), '; ', A)
    del A[1::2]
    print(len(A), '; ', A)


def N95():
    N = random.randint(8,8)
    A = [random.randint(0,4) for i in range(N)]
    print(A)
    N = len(A) -1
    for i in range(N):
        if i == N:
            break
        if A[i] == A[i+1]:
            A.pop(i+1)
            N-=1
    print(A)


def N96():
    N = random.randint(8,16)
    A = [random.randint(0,8) for i in range(N)]
    B = []
    print(A)
    i = 0
    while i <= len(A)-1:
        if A[i] not in B:
            B.append(A[i])
        else:
            A.pop(i)
            i-=1
        i+=1
    print(A, B)


def N97():
    N = random.randint(8,16)
    A = [random.randint(0,8) for i in range(N)]
    B = []
    print(A)
    i = len(A)-1
    while i >= 0:
        if A[i] not in B:
            B.append(A[i])
        else:
            A.pop(i)
        i-=1
    print(A, B)


def N98():
    N = random.randint(8,16)
    A = [random.randint(0,8) for i in range(N)]
    i = 0
    print(A)
    while i <= len(A)-1:
        x = A[i]
        k = 0
        for y in A:
            if x == y:
                k+=1
        if k < 3:
            flag = True
            while flag:
                try:
                    A.remove(x)
                except:
                    flag = False
        else:
            i+=1
    print(A)


def N99():
    N = random.randint(8,16)
    A = [random.randint(0,8) for i in range(N)]
    i = 0
    print(A)
    while i < len(A) :
        x = A[i]
        k = 0
        for y in A :
            if x == y :
                k += 1
        if k > 2 :
            flag = True
            while flag :
                try:
                    A.remove(x)
                except ValueError:
                    flag = False
        else :
            i += 1
    print(A)



def N100():
    N = random.randint(8,16)
    A = [random.randint(0,8) for i in range(N)]
    i = 0
    print(A)
    while i < len(A) :
        x = A[i]
        k = 0
        for y in A :
            if x == y :
                k += 1
        if k == 2:
            flag = True
            while flag :
                try:
                    A.remove(x)
                except ValueError:
                    flag = False
        else :
            i += 1
    print(A)


def N101():
    N = random.randint(5,10)
    K = random.randint(0,N-1)
    A = [random.randint(0,10) for i in range(N)]
    zero = [0]
    print(K,A)
    N_A = A[:K] + zero + A[K:]
    print(N_A)



def N102():
    N = random.randint(5,10)
    K = random.randint(1,N-1)
    A = [random.randint(5,10) for i in range(N)]
    zero = [0]
    print(K,A)
    N_A = A[:K+1] + zero + A[K+1:]
    print(N_A)




def N103():
    N = random.randint(5,10)
    A = [random.randint(1, 10) for i in range(N)]
    print(A)
    zero = [0]
    Max = max(A)
    Max_ind = A.index(Max)
    Min = min(A)
    Min_ind = A.index(Min)
    print(Max_ind, Max, Min_ind, Min)

    if Max_ind < Min_ind:
        N_A = A[:Max_ind+1] + zero + A[Max_ind+1:Min_ind] + zero + A[Min_ind:]

    else:
        N_A = A[:Min_ind] + zero + A[Min_ind:Max_ind+1] + zero + A[Max_ind+1:]

    print(N_A)



def N104():
    N = random.randint(5,10)
    K = random.randint(1, N)
    M = random.randint(1, 10)
    A = [random.randint(1, 10) for i in range(N)]
    print(A,K)
    N_A = A[:K] + M*[0] + A[K:]
    print(N_A)


def N105():
    N = random.randint(5,10)
    K = random.randint(1, N)
    M = random.randint(1, 10)
    A = [random.randint(1, 10) for i in range(N)]
    print(A,K)
    N_A = A[:K+1] + M*[0] + A[K+1:]
    print(N_A)


def N106():
   N = random.randrange(2,13)
   a = [random.randrange(0,5) for i in range(N)]
   print("N = ", N)
   print("Array:\n",a)
   M = N//2
   a.extend([0]*M)
   print("Modified Array 2:\n",a)
   j = 0
   for i in range(N-1,0,-2) :
       a[(N+M-1)-j] = a[i]
       a[(N+M-2)-j] = a[i-(N%2)]
       a[(N+M-3)-j] = a[i-1]
       j += 3
       print(a)
   print("Modified Array 2:\n",a)
   print("Length:\n",len(a))



def N107():

    N = random.randrange(2,10)
    #a = [i+1 for i in range(N)]
    a = [random.randrange(2,10) for i in range(N)]
    print("N = ", N)
    print("Array:\n",a)
    M = (N+1)//2
    a.extend([0]*M*2)
    print("Modified Array 2:\n",a)
    j = 0
    for i in range(N-1,-1,-2) :
        a[(N+M*2-1)-j] = a[i]
        a[(N+M*2-2)-j] = a[i-((N+1)%2)]
        a[(N+M*2-3)-j] = a[i-((N+1)%2)]
        a[(N+M*2-4)-j] = a[i-1]
        j += 4
    print("Modified Array 2:\n",a)
    print("Length:\n",len(a))



"""
Skip 108 - 111 чет в лом их делать.
"""


def N112(): # Сортировка пузырьков
    N = random.randint(2,6)
    A = [random.randint(1, 10) for i in range(N)]
    print(A)
    for j in range(N-1):
        i = 0
        for i in range(N-1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
    print(A)
    return A



def N113(): # Сортировка простым выбором
    N = random.randint(2,6)
    A = [random.randint(1, 10) for i in range(N)]
    print(A)
    for i in range(N-1):
        Max = -999999
        for j in range(0, N-i):
            if A[j] > Max:
                ind_max = j
                Max = A[j]

        A[ind_max], A[N-1-i] = A[N-1-i], A[ind_max]

    print(A)




def N114(): # Сортировка вставками
    N = random.randint(2,6)
    A = [random.randint(1, 10) for i in range(N)]
    print(A)

    Len = len(A) - 1

    for i in range(Len):
        flag = True
        j = i
        while flag:
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                if j >= 1:
                    j-=1
            else:
                flag = False
    print(A)


def N115():
    N = random.randint(2,6)
    A = [random.randint(1, 10) for i in range(N)]
    Num_A = [i for i in range(N)]
    print(A, '\n', Num_A)

    for j in range(N-1):
        i = 0
        for i in range(N-1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                Num_A[i], Num_A[i+1] = Num_A[i+1], Num_A[i]
    print(A, '\n', Num_A)




def N116():
    N = random.randint(2,15)
    A = [random.randint(1, 5) for i in range(N)]
    print(A, len(A)-1)

    Series_mass = []
    Series_num = []
    Len_series_mass = []
    Len_series_num = 1

    for i in range(0, len(A)-1):

        if Series_num == []:
            Series_num.append(A[i])

        if A[i] != A[i+1]:
            Series_mass.append(Series_num)
            Len_series_mass.append(Len_series_num)
            Series_num = []
            Len_series_num = 1

            if A[i+1] == A[-1] and i+1 == len(A)-1:
                Series_num.append(A[i+1])
                Series_mass.append(Series_num)
                Len_series_mass.append(Len_series_num)
                break

        else:
            Len_series_num += 1
            Series_num.append((A[i+1]))

            if A[i+1] == A[-1] and i+1 == len(A)-1:
                Series_mass.append(Series_num)
                Len_series_mass.append(Len_series_num)
                break

    print(Series_mass, '\n', Len_series_mass)






def N117():
    N = random.randint(2,15)
    A = [random.randint(1, 5) for i in range(N)]
    print(A, len(A)-1)

    Series_mass = []
    Series_num = []
    Len_series_mass = []
    Len_series_num = 1
    zero = 0
    j = 0

    for i in range(0, len(A)-1):

        if Series_num == []:
            Series_num.append(zero)
            Series_num.append(A[j])

        if A[j] != A[j+1]:
            Series_mass.append(Series_num)
            Len_series_mass.append(Len_series_num + 1)
            Series_num = []
            Len_series_num = 1

            if A[j+1] == A[-1] and j+1 == len(A)-1:
                Series_num.append(zero)
                Series_num.append(A[j+1])
                Series_mass.append(Series_num)
                Len_series_mass.append(Len_series_num + 1)
                break

        else:
            Len_series_num += 1
            Series_num.append((A[j+1]))

            if A[j+1] == A[-1] and j+1 == len(A)-1:
                Series_mass.append(Series_num)
                Len_series_mass.append(Len_series_num + 1)
                break
        j += 1

    print(Series_mass, '\n', Len_series_mass)


def N118():
    N = random.randint(2,15)
    A = [random.randint(1, 5) for i in range(N)]
    print(A, len(A)-1)

    Series_mass = []
    Series_num = []
    Len_series_mass = []
    Len_series_num = 1
    zero = 0
    j = 0

    for i in range(0, len(A)-1):

        if Series_num == []:
            Series_num.append(A[j])

        if A[j] != A[j+1]:
            Series_num.append(zero)
            Series_mass.append(Series_num)
            Len_series_mass.append(Len_series_num + 1)
            Series_num = []
            Len_series_num = 1

            if A[j+1] == A[-1] and j+1 == len(A)-1:
                Series_num.append(A[j+1])
                Series_num.append(zero)
                Series_mass.append(Series_num)
                Len_series_mass.append(Len_series_num + 1)
                break

        else:
            Len_series_num += 1
            Series_num.append((A[j+1]))

            if A[j+1] == A[-1] and j+1 == len(A)-1:
                Series_num.append(zero)
                Series_mass.append(Series_num)
                Len_series_mass.append(Len_series_num + 1)
                break
        j += 1

    print(Series_mass, '\n', Len_series_mass)


def N119():
    '''
    Тоже самое, что и 118, но вместо нуля, вставляется любой элемент.

    Returns
    -------
    None.

    '''

def N120():
    N = random.randint(2,15)
    A = [random.randint(1, 5) for i in range(N)]
    print(A, len(A)-1)

    Series_mass = []
    Series_num = []
    Len_series_mass = []
    Len_series_num = 1

    for i in range(0, len(A)-1):

        if Series_num == []:
            Series_num.append(A[i])

        if A[i] != A[i+1]:
            Series_mass.append(Series_num)
            Len_series_mass.append(Len_series_num)
            Series_num = []
            Len_series_num = 1

            if A[i+1] == A[-1] and i+1 == len(A)-1:
                Series_num.append(A[i+1])
                Series_mass.append(Series_num)
                Len_series_mass.append(Len_series_num)
                break

        else:
            Len_series_num += 1
            Series_num.append((A[i+1]))

            if A[i+1] == A[-1] and i+1 == len(A)-1:
                Series_mass.append(Series_num)
                Len_series_mass.append(Len_series_num)
                break

    print(Series_mass, '\n', Len_series_mass)


    for j in range(0, len(Series_mass)):

        if len(Series_mass[j]) > 1:
            break

        if j == len(Series_mass) - 1:
            print('Restart')
            N120()

    print()
    for i in range(0, len(Series_mass)):
            Series_mass[i].pop()
            Len_series_mass[i] = Len_series_mass[i] - 1

    print(Series_mass, '\n', Len_series_mass)



def N121():
    N = random.randint(2,15)
    A = [random.randint(1, 4) for i in range(N)]
    K = random.randint(1, 10)
    print(A, len(A)-1, K)

    Series_mass = []
    Series_num = []
    Len_series_mass = []
    Len_series_num = 1

    for i in range(0, len(A)-1):

        if Series_num == []:
            Series_num.append(A[i])

        if A[i] != A[i+1]:
            Series_mass.append(Series_num)
            Len_series_mass.append(Len_series_num)
            Series_num = []
            Len_series_num = 1

            if A[i+1] == A[-1] and i+1 == len(A)-1:
                Series_num.append(A[i+1])
                Series_mass.append(Series_num)
                Len_series_mass.append(Len_series_num)
                break

        else:
            Len_series_num += 1
            Series_num.append((A[i+1]))

            if A[i+1] == A[-1] and i+1 == len(A)-1:
                Series_mass.append(Series_num)
                Len_series_mass.append(Len_series_num)
                break
    print(Series_mass, '\n', Len_series_mass)

    if K > len(Series_mass):
        print('K')

    else:
        Series_mass[K] = Series_mass[K] + Series_mass[K]
        Len_series_mass[K] = Len_series_mass[K] * 2
        print(Series_mass, '\n', Len_series_mass)


def N122():
    N = random.randint(2,15)
    A = [random.randint(1, 4) for i in range(N)]
    K = random.randint(2, 10)
    print(A, len(A)-1, K)

    Series_mass = []
    Series_num = []
    Len_series_mass = []
    Len_series_num = 1

    for i in range(0, len(A)-1):

        if Series_num == []:
            Series_num.append(A[i])

        if A[i] != A[i+1]:
            Series_mass.append(Series_num)
            Len_series_mass.append(Len_series_num)
            Series_num = []
            Len_series_num = 1

            if A[i+1] == A[-1] and i+1 == len(A)-1:
                Series_num.append(A[i+1])
                Series_mass.append(Series_num)
                Len_series_mass.append(Len_series_num)
                break

        else:
            Len_series_num += 1
            Series_num.append((A[i+1]))

            if A[i+1] == A[-1] and i+1 == len(A)-1:
                Series_mass.append(Series_num)
                Len_series_mass.append(Len_series_num)
                break
    print(Series_mass, '\n', Len_series_mass)

    if K < len(Len_series_mass):
       del(Series_mass[K-1])
       del(Len_series_mass[K-1])
       print(Series_mass, '\n', Len_series_mass)


def N123():
    N = random.randint(2,15)
    A = [random.randint(1, 4) for i in range(N)]
    K = random.randint(2, 10)
    print(A, len(A)-1, K)

    Series_mass = []
    Series_num = []
    Len_series_mass = []
    Len_series_num = 1

    for i in range(0, len(A)-1):

        if Series_num == []:
            Series_num.append(A[i])

        if A[i] != A[i+1]:
            Series_mass.append(Series_num)
            Len_series_mass.append(Len_series_num)
            Series_num = []
            Len_series_num = 1

            if A[i+1] == A[-1] and i+1 == len(A)-1:
                Series_num.append(A[i+1])
                Series_mass.append(Series_num)
                Len_series_mass.append(Len_series_num)
                break

        else:
            Len_series_num += 1
            Series_num.append((A[i+1]))

            if A[i+1] == A[-1] and i+1 == len(A)-1:
                Series_mass.append(Series_num)
                Len_series_mass.append(Len_series_num)
                break
    print(Series_mass, '\n', Len_series_mass)

    if K < len(Len_series_mass):
       print()
       Series_mass[0], Series_mass[K-1] = Series_mass[K-1], Series_mass[0]
       Len_series_mass[0], Len_series_mass[K-1] = Len_series_mass[K-1], Len_series_mass[0]
       print(Series_mass, '\n', Len_series_mass)


def N124():
    N = random.randint(2,15)
    A = [random.randint(1, 4) for i in range(N)]
    K = random.randint(2, 10)
    print(A, len(A)-1, K)

    Series_mass = []
    Series_num = []
    Len_series_mass = []
    Len_series_num = 1

    for i in range(0, len(A)-1):

        if Series_num == []:
            Series_num.append(A[i])

        if A[i] != A[i+1]:
            Series_mass.append(Series_num)
            Len_series_mass.append(Len_series_num)
            Series_num = []
            Len_series_num = 1

            if A[i+1] == A[-1] and i+1 == len(A)-1:
                Series_num.append(A[i+1])
                Series_mass.append(Series_num)
                Len_series_mass.append(Len_series_num)
                break

        else:
            Len_series_num += 1
            Series_num.append((A[i+1]))

            if A[i+1] == A[-1] and i+1 == len(A)-1:
                Series_mass.append(Series_num)
                Len_series_mass.append(Len_series_num)
                break
    print(Series_mass, '\n', Len_series_mass)

    if K < len(Len_series_mass):
       print()
       Series_mass[-1], Series_mass[K-1] = Series_mass[K-1], Series_mass[-1]
       Len_series_mass[-1], Len_series_mass[K-1] = Len_series_mass[K-1], Len_series_mass[-1]
       print(Series_mass, '\n', Len_series_mass)

def N125():
    N = random.randint(2,15)
    A = [random.randint(1, 4) for i in range(N)]
    L = random.randint(1, 5)
    print(A, len(A)-1, L)

    Series_mass = []
    Series_num = []
    Len_series_mass = []
    Len_series_num = 1

    for i in range(0, len(A)-1):

        if Series_num == []:
            Series_num.append(A[i])

        if A[i] != A[i+1]:
            Series_mass.append(Series_num)
            Len_series_mass.append(Len_series_num)
            Series_num = []
            Len_series_num = 1

            if A[i+1] == A[-1] and i+1 == len(A)-1:
                Series_num.append(A[i+1])
                Series_mass.append(Series_num)
                Len_series_mass.append(Len_series_num)
                break

        else:
            Len_series_num += 1
            Series_num.append((A[i+1]))

            if A[i+1] == A[-1] and i+1 == len(A)-1:
                Series_mass.append(Series_num)
                Len_series_mass.append(Len_series_num)
                break
    print(Series_mass, '\n', Len_series_mass)

    for i in range(len(Len_series_mass)):
        if L > Len_series_mass[i]:
            Series_mass[i] = [0]
            Len_series_mass[i] = 1
    print()
    print(Series_mass, '\n', Len_series_mass)


def N126():
    N = random.randint(2,15)
    A = [random.randint(1, 4) for i in range(N)]
    L = random.randint(2, 5)
    print(A, len(A)-1, L)

    Series_mass = []
    Series_num = []
    Len_series_mass = []
    Len_series_num = 1

    for i in range(0, len(A)-1):

        if Series_num == []:
            Series_num.append(A[i])

        if A[i] != A[i+1]:
            Series_mass.append(Series_num)
            Len_series_mass.append(Len_series_num)
            Series_num = []
            Len_series_num = 1

            if A[i+1] == A[-1] and i+1 == len(A)-1:
                Series_num.append(A[i+1])
                Series_mass.append(Series_num)
                Len_series_mass.append(Len_series_num)
                break

        else:
            Len_series_num += 1
            Series_num.append((A[i+1]))

            if A[i+1] == A[-1] and i+1 == len(A)-1:
                Series_mass.append(Series_num)
                Len_series_mass.append(Len_series_num)
                break
    print(Series_mass, '\n', Len_series_mass)

    for i in range(len(Len_series_mass)):
        if L == Len_series_mass[i]:
            Series_mass[i] = [0]
            Len_series_mass[i] = 1
    print()
    print(Series_mass, '\n', Len_series_mass)


def N127():
    N = random.randint(2,15)
    A = [random.randint(1, 4) for i in range(N)]
    L = random.randint(2, 5)
    print(A, len(A)-1, L)

    Series_mass = []
    Series_num = []
    Len_series_mass = []
    Len_series_num = 1

    for i in range(0, len(A)-1):

        if Series_num == []:
            Series_num.append(A[i])

        if A[i] != A[i+1]:
            Series_mass.append(Series_num)
            Len_series_mass.append(Len_series_num)
            Series_num = []
            Len_series_num = 1

            if A[i+1] == A[-1] and i+1 == len(A)-1:
                Series_num.append(A[i+1])
                Series_mass.append(Series_num)
                Len_series_mass.append(Len_series_num)
                break

        else:
            Len_series_num += 1
            Series_num.append((A[i+1]))

            if A[i+1] == A[-1] and i+1 == len(A)-1:
                Series_mass.append(Series_num)
                Len_series_mass.append(Len_series_num)
                break
    print(Series_mass, '\n', Len_series_mass)

    for i in range(len(Len_series_mass)):
        if L < Len_series_mass[i]:
            Series_mass[i] = [0]
            Len_series_mass[i] = 1
    print()
    print(Series_mass, '\n', Len_series_mass)



def N128():
    N = random.randint(2,15)
    A = [random.randint(1, 4) for i in range(N)]

    print(A, len(A)-1)

    Series_mass = []
    Series_num = []
    Len_series_mass = []
    Len_series_num = 1

    for i in range(0, len(A)-1):

        if Series_num == []:
            Series_num.append(A[i])

        if A[i] != A[i+1]:
            Series_mass.append(Series_num)
            Len_series_mass.append(Len_series_num)
            Series_num = []
            Len_series_num = 1

            if A[i+1] == A[-1] and i+1 == len(A)-1:
                Series_num.append(A[i+1])
                Series_mass.append(Series_num)
                Len_series_mass.append(Len_series_num)
                break

        else:
            Len_series_num += 1
            Series_num.append((A[i+1]))

            if A[i+1] == A[-1] and i+1 == len(A)-1:
                Series_mass.append(Series_num)
                Len_series_mass.append(Len_series_num)
                break
    print(Series_mass, '\n', Len_series_mass)

    index = Len_series_mass.index(max(Len_series_mass))
    Series_mass[index].append('*')


    print(Series_mass, '\n', Len_series_mass)

def N129():
    N = random.randint(2,15)
    A = [random.randint(1, 4) for i in range(N)]

    print(A, len(A)-1)

    Series_mass = []
    Series_num = []
    Len_series_mass = []
    Len_series_num = 1

    for i in range(0, len(A)-1):

        if Series_num == []:
            Series_num.append(A[i])

        if A[i] != A[i+1]:
            Series_mass.append(Series_num)
            Len_series_mass.append(Len_series_num)
            Series_num = []
            Len_series_num = 1

            if A[i+1] == A[-1] and i+1 == len(A)-1:
                Series_num.append(A[i+1])
                Series_mass.append(Series_num)
                Len_series_mass.append(Len_series_num)
                break

        else:
            Len_series_num += 1
            Series_num.append((A[i+1]))

            if A[i+1] == A[-1] and i+1 == len(A)-1:
                Series_mass.append(Series_num)
                Len_series_mass.append(Len_series_num)
                break
    print(Series_mass, '\n', Len_series_mass)

    Max = 0
    ind_max = 0
    for i in range(len(Len_series_mass)-1, 0, -1):
        if Len_series_mass[i] > Max:
            Max = Len_series_mass[i]
            ind_max = i

    Series_mass[ind_max].append('*')

    print(Series_mass, '\n', Len_series_mass)

def N130():
    N = random.randint(2,15)
    A = [random.randint(1, 4) for i in range(N)]

    print(A, len(A)-1)

    Series_mass = []
    Series_num = []
    Len_series_mass = []
    Len_series_num = 1

    for i in range(0, len(A)-1):

        if Series_num == []:
            Series_num.append(A[i])

        if A[i] != A[i+1]:
            Series_mass.append(Series_num)
            Len_series_mass.append(Len_series_num)
            Series_num = []
            Len_series_num = 1

            if A[i+1] == A[-1] and i+1 == len(A)-1:
                Series_num.append(A[i+1])
                Series_mass.append(Series_num)
                Len_series_mass.append(Len_series_num)
                break

        else:
            Len_series_num += 1
            Series_num.append((A[i+1]))

            if A[i+1] == A[-1] and i+1 == len(A)-1:
                Series_mass.append(Series_num)
                Len_series_mass.append(Len_series_num)
                break
    print(Series_mass, '\n', Len_series_mass)

    Max = max(Len_series_mass)
    for i in range(len(Len_series_mass)):
        if len(Series_mass[i]) == Max:
            Series_mass[i].append('*')

    print(Series_mass, '\n', Len_series_mass, Max)

from math import sqrt
import matplotlib.pyplot as plt

def N131():



    fig = plt.figure()
    ax = fig.add_subplot()
    N = random.randint(2, 10)
    A = [[random.randint(-10,10) for i in range(2)] for i in range(N)]
    B = [random.randint(-10,10) for i in range(2)]
    print(A,N,B)
    j = 0
    R_mass = []
    for i in range(len(A)):
        R = sqrt((B[j] - A[i][j])**2 + (B[j+1] - A[i][j+1])**2)
        R_mass.append(R)
        ax.scatter(A[i][j],A[i][j+1])
        plt.text(A[i][j]+0.2,A[i][j+1], f'{i}',fontsize = 12)

    ax.scatter(B[j],B[j+1])
    plt.text(B[j]+0.2,B[j+1], 'B', fontsize = 12)
    plt.show()
    print('Наиболее близкой точкой, является точка под номером: ' ,R_mass.index(min(R_mass)))

def N132():

    fig = plt.figure()
    ax = fig.add_subplot()
    N = random.randint(2, 10)
    A = [[random.randint(-10,10) for i in range(2)] for i in range(N)]
    B = [0,0]
    print(A,N)
    j = 0
    R_mass = []
    point = []
    for i in range(len(A)):
        if A[i][j] < 0 and A[i][j+1] > 0:
            R = sqrt((B[j] - A[i][j])**2 + (B[j+1] - A[i][j+1])**2)
            R_mass.append(R)
            point.append(i)
        ax.scatter(A[i][j],A[i][j+1])
        plt.text(A[i][j]+0.2,A[i][j+1], f'{i}',fontsize = 12)

    ax.scatter(B[j],B[j+1])
    ax.grid()
    plt.text(B[j]+0.2,B[j+1]+0.2, 'B', fontsize = 12)
    ax.vlines(0,-10,10, 'black', linewidth = 1.5)
    ax.hlines(0, -10, 10,'black',  linewidth = 1.5)
    plt.show()

    if R_mass:
        index = R_mass.index(max(R_mass))
        print('Наиболее удаленной точкой из 2 четверти, является точка под номером: ' , point[index])
    else:
        print('Вторая четверть пуста')

def N133():

    fig = plt.figure()
    ax = fig.add_subplot()
    N = random.randint(2, 10)
    A = [[random.randint(-10,10) for i in range(2)] for i in range(N)]
    B = [0,0]
    print(A,N)
    j = 0
    R_mass = []
    point = []
    card = []
    for i in range(len(A)):
        if (A[i][j] > 0 and A[i][j+1] > 0) or (A[i][j] < 0 and A[i][j+1] < 0):
            R = sqrt((B[j] - A[i][j])**2 + (B[j+1] - A[i][j+1])**2)
            R_mass.append(R)
            point.append(i)
            if (A[i][j] > 0 and A[i][j+1] > 0):
                card.append('1')
            else:
                card.append('3')

        ax.scatter(A[i][j],A[i][j+1])
        plt.text(A[i][j]+0.2,A[i][j+1], f'{i}',fontsize = 12)

    ax.scatter(B[j],B[j+1])
    ax.grid()
    plt.text(B[j]+0.2,B[j+1]+0.2, 'B', fontsize = 12)
    ax.vlines(0,-10,10, 'black', linewidth = 1.5)
    ax.hlines(0, -10, 10,'black',  linewidth = 1.5)
    plt.show()

    if R_mass:
        index = R_mass.index(min(R_mass))
        print(f'Наиболее близкой точкой из {card[index]} четверти, является точка под номером: ' , point[index])
    else:
        print('Первая и третья четверти пусты')


def N134():

    fig = plt.figure()
    ax = fig.add_subplot()
    N = random.randint(2, 10)
    A = [[random.randint(-10,10) for i in range(2)] for i in range(N)]
    print(A,N)
    j = 0
    R_mass = []
    left = []
    right = []
    for i in range(len(A)):
        for k in range(i, len(A)-1):
            R = sqrt((A[i][j] - A[k+1][j])**2 + (A[i][j+1] - A[k+1][j+1])**2)
            R_mass.append(R)
            left.append(i)
            right.append(k+1)
        ax.scatter(A[i][j],A[i][j+1])
        plt.text(A[i][j]+0.2,A[i][j+1], f'{i}',fontsize = 12)


    ax.grid()
    ax.vlines(0,-10,10, 'black', linewidth = 1.5)
    ax.hlines(0, -10, 10,'black',  linewidth = 1.5)
    plt.show()

    index = R_mass.index(max(R_mass))
    print(f'Наиболее удалены друг от друга точки под номером {left[index]} и {right[index]} на расстояние - ', max(R_mass))

def N135():

    fig = plt.figure()
    ax = fig.add_subplot()
    N1 = random.randint(2, 10)
    N2 = random.randint(2, 10)
    A = [[random.randint(-10,10) for i in range(2)] for i in range(N1)]
    B = [[random.randint(-10,10) for i in range(2)] for i in range(N2)]
    print(A, N1, B, N2)
    j = 0
    R_mass = []
    left = []
    right = []
    for i in range(len(A)):
        for k in range(len(B)):
            R = sqrt((A[i][j] - B[k][j])**2 + (A[i][j+1] - B[k][j+1])**2)
            R_mass.append(R)
            left.append(i)
            right.append(k)

        ax.scatter(A[i][j],A[i][j+1])
        plt.text(A[i][j]+0.2,A[i][j+1], f'A{i}',fontsize = 12)



    for i in range(len(B)):
        ax.scatter(B[i][j],B[i][j+1])
        plt.text(B[i][j]+0.2,B[i][j+1], f'B{i}',fontsize = 12)

    ax.grid()
    ax.vlines(0,-10,10, 'black', linewidth = 1.5)
    ax.hlines(0, -10, 10,'black',  linewidth = 1.5)
    plt.show()

    index = R_mass.index(min(R_mass))
    print(f'Наименее удалены друг от друга точки под номером A{left[index]} и B{right[index]} на расстояние - ', min(R_mass))

def N136():

    fig = plt.figure()
    ax = fig.add_subplot()
    N1 = random.randint(3, 10)
    A = [[random.randint(-10,10) for i in range(2)] for i in range(N1)]
    print(A, N1)
    j = 0
    R_mass = []


    for i in range(len(A)):
        R = 0
        for k in range(len(A)):
            R += sqrt((A[i][j] - A[k][j])**2 + (A[i][j+1] - A[k][j+1])**2)

        R_mass.append(R)
        ax.scatter(A[i][j],A[i][j+1])
        plt.text(A[i][j]+0.2,A[i][j+1]+0.2, f'{i}',fontsize = 12)


    ax.grid()
    ax.vlines(0,-10,10, 'black', linewidth = 1.5)
    ax.hlines(0, -10, 10,'black',  linewidth = 1.5)
    plt.show()

    index = R_mass.index(min(R_mass))
    print(f'Точка - {index}, сумма растояниий которой минимальна - ', min(R_mass))


def N137():
    fig = plt.figure()
    ax = fig.add_subplot()
    N1 = random.randint(3, 10)
    A = [[random.randint(-10,10) for i in range(2)] for i in range(N1)]
    print(A, N1)
    j = 0
    P_mass = []
    Triangl = []



    for i in range(len(A)):
        for k in range(i+1, len(A)):
            for t in range(k+1, len(A)):
                tri = []
                P = 0
                R_1 = sqrt((A[i][j] - A[k][j])**2 + (A[i][j+1] - A[k][j+1])**2)
                R_2 = sqrt((A[i][j] - A[t][j])**2 + (A[i][j+1] - A[t][j+1])**2)
                R_3 = sqrt((A[t][j] - A[k][j])**2 + (A[t][j+1] - A[k][j+1])**2)
                P += R_1 + R_2 + R_3
                P_mass.append(P)
                tri.append(i)
                tri.append(k)
                tri.append(t)
                Triangl.append(tri)



        ax.scatter(A[i][j],A[i][j+1])
        plt.text(A[i][j]+0.2,A[i][j+1]+0.2, f'{i}',fontsize = 12)

    ax.grid()
    ax.vlines(0,-10,10, 'black', linewidth = 1.5)
    ax.hlines(0, -10, 10,'black',  linewidth = 1.5)
    plt.show()
    index_max = P_mass.index(max(P_mass))
    index_min = P_mass.index(min(P_mass))
    print(f'Периметр треугольника с точками: {Triangl[index_max]}, максимален - ', max(P_mass))
    print('Задача, номер - N138')
    print(f'Периметр треугольника с точками: {Triangl[index_min]}, минимален - ', min(P_mass))


def N139():
    fig = plt.figure()
    ax = fig.add_subplot()
    N1 = random.randint(3, 10)
    A = [[random.randint(-10,10) for i in range(2)] for i in range(N1)]

    print(A, N1)
    j = 0
    for k in range(len(A)):
        for i in range(len(A)-k-1):
            if (A[i][j] > A[i+1][j]) or (A[i][j] == A[i+1][j] and A[i][j+1] > A[i+1][j+1]):
                A[i], A[i+1] = A[i+1], A[i]

    for i in range(len(A)):
        ax.scatter(A[i][j],A[i][j+1])
        plt.text(A[i][j]+0.2,A[i][j+1]+0.2, f'{i}',fontsize = 12)
    print(A)
    ax.grid()
    ax.vlines(0,-10,10, 'black', linewidth = 1.5)
    ax.hlines(0, -10, 10,'black',  linewidth = 1.5)
    plt.show()


def N140():
    fig = plt.figure()
    ax = fig.add_subplot()
    N1 = random.randint(3, 10)
    A = [[random.randint(-10,10) for i in range(2)] for i in range(N1)]

    print(A, N1)
    j = 0
    for k in range(len(A)):
        for i in range(len(A)-k-1):
            if ((A[i][j] + A[i][j+1]) < (A[i+1][j] + A[i+1][j+1])) or (((A[i][j] + A[i][j+1]) == (A[i+1][j] + A[i+1][j+1])) and (A[i][j] < A[i+1][j]))  :
                A[i], A[i+1] = A[i+1], A[i]

    for i in range(len(A)):
        ax.scatter(A[i][j],A[i][j+1])
        plt.text(A[i][j]+0.2,A[i][j+1]+0.2, f'{i}',fontsize = 12)
    print(A)
    ax.grid()
    ax.vlines(0,-10,10, 'black', linewidth = 1.5)
    ax.hlines(0, -10, 10,'black',  linewidth = 1.5)
    plt.show()

N140()










