1#
'''
import random
N = random.randint(1,10)
print('N=',N)
S = [random.randint(-10,10) for i in range(0,N)]
print('S=',S)
print('min(S)=',min(S))
print('max(S)=',max(S))
'''

2,3#
'''
import random
N = random.randint(1,10)
print('N=',N)
S = 1
s = []
for i in range(0,N):
    a = random.randint(1,20)
    b = random.randint(1,20)
    print(a,';',b)
    S = a * b
    s.append(S)

print(s)
print('min(s)=',min(s))
print('max(s)=',max(s))

ИЛИ

import random

N = random.randrange(1,10)
s = []
for x in range(0, N):
    a = random.randrange(1,10)
    b = random.randrange(1,10)
    s.append({'a':a,'b':b})
print(s)

print("Количество прямоугольников: ", N)
i = 1
min_square = s[0]['a']*s[0]['b']
for x in s:
    y = x['a']*x['b']
    print('Прямоугольник №', i, ' со сторонами a = ', x['a'],'; b = ', x['b'], '; Площадь S = ', y)
    if min_square > y:
        min_square = y
    i += 1
print('Минимальная из площадей: ', min_square)
'''

4#
'''
import random
N = random.randint(1,10)
print('N=',N)
S = [random.randint(-10,10) for i in range(0,N)]
print('S=',S)
Min = 100
k = 0
n = 0
for i in S:
    k+=1
    if i < Min:
        Min = i
        n = k
print('Номер наименьшего элемента в списке:',n)
'''

5#
'''
import random
N = random.randint(1,10)
print('N=',N)
P = 1
k = 1
s = []
Max = 1
index = 0
m = 0
for i in range(0,N):
    M = random.randint(1,1000)
    V = random.randint(1,10)
    print(k,':','M=',M,';','V=',V)
    P = M / V
    s.append(P)
    k+=1

for j in s:
    m+=1
    if j > Max:
        Max = j
        index = m

print('Плотность детали:',Max, 'Номер:',index)

ИЛИ

import random

N = random.randrange(1,15)
print("N = ",N)
L = [(random.randint(100, 1000), random.randint(1, 100)) for k in range(N)]
P = [L[i][0]/L[i][1] for i in range(N)]
print("L: ")
print(L)
print(P)
max_density = max(P)
print("Максимальная плотность: ", max_density)
print("Индекс детали с макс. плотностью: ", P.index(max_density))
'''

6#
'''
import random
N = random.randint(1,20)
print('N=',N)
Min = 1000
Max = -1000
k = 0
index1 = 0
index2 = 0
S = [random.randint(1,10) for i in range(N)]
print(S)
for i in S:
    k+=1
    if i >= Max:
        Max = i
        index1 = k
    elif i < Min:
        Min = i
        index2 = k
print(index2,':',Min)
print(index1,':',Max)

ИЛИ

import random

N = random.randrange(1,15)
print("N = ",N)
L = [random.randint(1, 8) for i in range(N)]
print("L: ")
print(L)

_max = max(L)
_min = min(L)
print("Минимум: ", _min)
print("Максимум: ", _max)

for i in range(N):
    if L[i] == _min:
        break
print("Индекс первого минимума: ", i)

for i in range(N,0,-1):
    if L[i-1] == _max:
        break
print("Индекс последнего максимума: ", i-1)
'''

8#
'''
import random
N = random.randint(1,20)
print('N=',N)
Min = 1000
k = 0
index1 = 0
index2 = 0


S = [random.randint(1,10) for i in range(N)]
print(S)

for i in S:
    k +=1
    if i < Min:
        Min = i
        index1 = k
    elif i <= Min:
        Min = i
        index2 = k

print('Номер первого минимального элемента:',index1)
print('Номер последнего минимального элемента:',index2)
'''


10#
'''
import random
N = random.randint(1,20)
print('N=',N)

Min = 1000
Max = -1000
k = 0
index1 = 0
index2 = 0

S = [random.randint(1,10) for i in range(N)]
print(S)

for i in S:
    k +=1
    if i > Max:
        Max = i
        index1 = k
    if i < Min:
        Min = i
        index2 = k

if index1 < index2:
    l = index1
else:
    l = index2

print('Номер экстремума:',l)
'''

12#
'''
import random
N = random.randint(1,10)
print('N=',N)
Min = 1000

S = [random.randint(-10,10) for i in range(N)]
print(S)

for i in S:
    if i < Min and i > 0:
        Min = i

if Min!=1000:
    print('Минимальное положительное число в списке:',Min)
else:
    print('Нет положительных чисел в списке:',0)
'''

13#
'''
import random
N = random.randint(1,10)
print('N=',N)
k = 0
Max = -1000
index = 0

S = [random.randint(-10,10) for i in range(N)]
print(S)

for i in S:
    k+=1
    if i > Max and i%2 != 0:
        Max = i
        index = k
if Max != -1000:
    print('Номер первого максимального нечетного числа в списке:',index)
else:
    print('Нечетных в списке нет:',0)
'''

14#
'''
import random
N=10
S = [random.randint(-10,10) for i in range(N)]
print(S)
S = sorted(S)
print(S)
L = []


B = random.randint(1,10)
print('B=',B)

k = 0
index = 0
Min = 1000


for i in S:
    if i > B:
        L.append(i)

print(L)
if L != []:
    Min = min(L)
    print('Наименьшее значение больше В:',Min)
else:
    print('Нет чисел больших В',0 0)
 '''

15#
'''
import random
N=10
S = [random.randint(0,30) for i in range(N)]
L = []
print(S)
B = random.randint(1,10)
C = random.randint(10,20)
print('B=',B, 'C=',C)

for i in S:
    if i > B and i < C:
        L.append(i)

if L == []:
    print('В списке нет элементов меньше С и больше В')
else:
    print(L)
    x = max(L)
    index = S.index(x)
    print('Максимальный элемент из списка S:',x)
    print('Номер максимального элемента:',index+1)
'''


16#
'''
import random
N = random.randint(5,10)
S = [random.randint(0,10) for i in range(N)]
print(S)
m=0
x = min(S)
index = S.index(x)
print(index,':',x)
print(S[index::-1])
k = S[index::-1]
for i in k:
    m+=1
print('Первый минимум:', index)
print('Элементов до минимума:',m-1)# Много способов решеня
'''



18#
'''
import random
N = random.randint(10,20)
S = [random.randint(0,10) for i in range(N)]
L = []
print(N)
print(S)
Max1 = -1000
Max2 = -1000
k1 = 0
k2 = 0
k3 = 0
l = 0
for i in S:
    k1+=1
    k2+=1
    if i > Max1:
        Max1 = i
        index1 = k1
    if i >= Max2:
        Max2 = i
        index2 = k2

for i in S:
    l+=1
    if l > index1 and l < index2:
        L.append(i)

if index1 == index2:
    print('Максимум всего один;',0)
else:
    print(L)
    for i in L:
        k3+=1

    print(['Количество элементов между максимумами:',k3])
'''


19#
'''
import random
N = random.randint(10,20)
S = [random.randint(0,10) for i in range(N)]
print(N)
print(S)
k = 0

x = min(S)
print(x)

for i in S:
    if i == x:
        k+=1

print('Количество минимальных элементов в списке:',k)
'''


21#
'''
import random
N = random.randint(2,10)
S = [random.randint(0,10) for i in range(N)]
print(N)
print(S)
s=0

Min = min(S)
Max = max(S)

for i in S:
    if i!=Min and i!=Max:
        s+=i

medium = s/N
print(medium)
'''


22#
'''
import random
N = random.randint(2,10)
S = [random.randint(0,10) for i in range(N)]
print(N)
print(S)

Min1 = min(S)
S.remove(Min1)
Min2 = min(S)
print(Min1,Min2)
'''



23#
'''
import random
N = random.randint(3,10)
S = [random.randint(0,10) for i in range(N)]
print(N)
print(S)

Max1 = max(S)
S.remove(Max1)

Max2 = max(S)
S.remove(Max2)

Max3 = max(S)
S.remove(Max3)


print(Max1,Max2,Max3)
'''


24#
'''
import random
N = random.randint(2,10)
S = [random.randint(0,10) for i in range(N)]
print(N)
print(S)

mx = S[0] + S[1]
for i in range(1,len(S)-1):
    x = S[i] + S[i+1]
    if x > mx:
        mx = x
    print(S[i],S[i+1])
print("\nMaximum of pairs:",mx)
'''


25#
'''
import random
N = random.randint(2,10)
S = [random.randint(0,10) for i in range(N)]
print(N)
print(S)

mx = S[0] * S[1]
mn_idx = 0
for i in range(1,len(S)-1):
    x = S[i] * S[i+1]
    if x < mx:
        mx = x
        mn_idx = i
    print(S[i],S[i+1])
print("\nMinimum of pairs:",mn_idx,mn_idx +1)
'''


26#
'''
import random
N = random.randint(2,10)
S = [random.randint(0,10) for i in range(N)]
print(N)
print(S)

largest = 0
temp_largest = 0

for i in S:
    if i%2==0:
        temp_largest += 1
    else:
        if temp_largest > largest:
            largest = temp_largest
        temp_largest = 0

if temp_largest > largest:
    largest = temp_largest

print("\nLargest Length of Evens:",largest)
'''


'''
27#
import random
N = random.randint(10,20)
S = [random.randint(0,1) for i in range(N)]
print(N)
print(S)

last = 0
present = S[0]
index_Max = 0
indexNow = S.index(last)
indexNext = 0
LengthListNow = 0
LengthListNext = 0
l=0
for i in S:

    if last == present:
        LengthListNow = S.index(present) - indexNow
        last = present
        present = S[l]

    else:
        LengthListNow = S.index(present) - indexNow
        Max_Lenght = max(LengthListNext,LengthListNow)
        if Max_Lenght == LengthListNow:
            index_Max = indexNow
        else:
            index_Max = indexNext
        LengthListNext = LengthListNow
        LengthListNow = 0
        last = present
        present = S[l]
    l+=1
print(index_Max)



27,28,29,30 - Не решил




'''


















