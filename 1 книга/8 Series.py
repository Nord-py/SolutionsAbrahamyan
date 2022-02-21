
1,2,3#
'''
import random
N = 10
s = 0

for i in range(10):
    x = random.uniform(1,10)
    print(x)
    s +=x
print()
print(s)

s = 1
for i in range(10):
    x = random.uniform(1,10)
    print(x)
    s *=x
print()
print(s)

for i in range(N):
    x = random.uniform(1,10)
    print(x)
    s +=x
print()
print(s)
s = s / N
print()
print(s)
'''



4,5,6,7,8,10#
'''
import random
N = random.randint(1,10)
S = 0
P = 1
k = 1
n = 0
print('N = ',N)

for i in range(N):
    x = random.uniform(0,N)
    print(k,':',x)
    k += 1
    S += x
    P *= x
print()
print(S)
print(P)

for i in range(N):
    x = random.uniform(0,N)
    print(k,':',x, ':', int(x))
    k += 1
    S += int(x)
print()
print(S)


for i in range(N):
    x = random.uniform(1,N)
    print(k,':',x, ':', x - int(x))
    k += 1
    P *= x - int(x)
print()
print(P)


for i in range(N):
    x = random.uniform(0,N)
    print(k,':',x, ':', round(x,0))
    S += round(x,0)
print()
print(S)


H = []
for i in range(N):
    x = random.randint(0,N)
    print(k,':',x)
    k += 1
    if x % 2 == 0 and x != 0:
        H.append(x)
        n += 1
print('Все четные числа:', H)
print('Количество четных чисел:',n)



for i in range(N):
    x = random.randint(-10,10)
    print(k,':',x)
    k += 1
    r = (x > 0)
    if x > 0:
        print(x,':',True)
        break
    else:
        print(x,':',False)

print('В ряду есть положительное число:',r)

'''


11#
'''
import random
K,N = random.sample(range(1,20),2)
print('N = ',N)
print('K = ',K)
k = 0
r = 0

for i in range(N):
    x = random.randint(0,20)
    k += 1
    print(k , ':' , x)

    if x < K:
        r +=1
print()
if r > 0:
    print('Есть числа меньше K? ', True)
else:
    print('Есть числа меньше K? ' ,False)
'''


12,13#
'''
import random
N = random.randint(0,100)
s = 0
S = []
S.append(N)
while N != 0:
    N = random.randint(-10,10)
    S.append(N)
print(S)
#print('Всего элементов в списке:',len(S)-1)

for i in S:
    if i > 0 and i % 2 == 0:
        s += i
print()
print(s)
'''


14,15,16#
'''
import random
K = random.randint(1,15)
print('K = ',K)
print()

x = random.randint(-10,20)
S = []
S.append(x)

while x != 0:
    x = random.randint(-10,20)
    S.append(x)

del S[-1]
#S = list(reversed(S)) # or S = S[::-1]
print(S)


n = 0

for i in S:
    if i < K:
        n +=1

print('Количество чисел меньше К:', n)

r = 0
for i in S:
    r += 1
    if i > K:
        print('Номер элемента большего К:',r)
        break

if K > i:
    print(0)


N = 0
r = 0
for i in S:
    r += 1
    if i > K:
        N = r

print(N)
'''


17#
'''
import random
B = random.uniform(0,10)
N = random.randint(0,10)
print('B = ',B)
print('N = ',N)


S = []
k = 0

while k < N:
    k += 1
    x = random.uniform(0,10)
    S.append(x)


S = list(sorted(S))
print(S)
print()

for i in S:
    if i <= B and B <= i+1:
        print(B)

'''


18#
'''
import random
N = random.randint(0,10)
print('N = ',N)


S = []
k = 0

while k < N:
    k += 1
    x = random.randint(0,10)
    S.append(x)

print(S)
print()

y = sorted(set(S), key=lambda d: S.index(d))# Сортировка по индексу, а set сортирует только уникальные элементы, т.е. по одному в списке
print(y)
'''


19#
'''
import random
N = random.randint(1,10)
print('N = ',N)

x = random.randrange(1,10)
print(x,end="; ")
x_prev = x
k = 0
for i in range(1,N):
    x = random.randrange(1,10)
    if  x < x_prev:
        k +=1
        print("*{0}".format(x),end="; ")
    else:
        print(x,end="; ")
    x_prev = x
print()
print("K = ",k)
'''



20#
'''
import random

N = random.randrange(2,20)
print("N = ",N)

x = random.randrange(1,10)
x_prev = x
k = 0
for i in range(1,N):
    x = random.randrange(1,10)
    if x_prev < x:
        k += 1
        print("*{0}".format(x_prev),end="; ")
    else:
        print(x_prev,end="; ")
    x_prev = x
print(x)

print("K = ",k)

'''

21#
'''
import random
N = random.randint(1,10)
print('N = ',N)

x = random.randint(1,10)
Left = x
print(Left)

Flag =True

for i in range(1,N):
    x = random.randint(1,10)
    if Left <= x:
        print(x)
        Flag
    else:
        print(x)
        Flag = False

    Left = x

print(Flag)
'''



22#
'''
import random
N = random.randint(1,10)
print('N = ',N)



x = random.randint(1,10)
Left = x
print(Left)
k = 1
Flag = 0

for i in range(1,N):
    x = random.randint(1,10)
    k += 1
    if Left >= x:
        print(x)
        Flag
    else:
        print(x)
        k
        break

    Left = x

print()
print(Flag)
print(k)

'''



23# НЕ СДЕЛАЛ
'''
import random
N = random.randint(3,10)
print('N = ',N)

x = random.randint(0,10)
Left = x
print(Left)

x = random.randint(0,10)
Mid = x
print(Mid)

k = 2
for i in range(1,N):
    x = random.randint(0,10)
    k +=1
    if (Left < Mid and Mid > x) or (Left > Mid and  Mid < x):
        print(x)
        Flag = 0
    else:
        Flag = k
        break
print()
print(Flag)

'''


24#
'''
import random

N = random.randrange(5,15)
Z = random.randrange(2,6)

L1 = [random.randrange(1,5) for i in range(0,N)]
L2 = [0 for i in range(0,Z)]
L = L1 + L2

print(L1)
print(L2)
random.shuffle(L)
print(L)

s = 0
for x in L:
    if x == 0:
        s_last = s
        s = 0
    else:
        s += x

print("Sum = ",s_last)
'''

25#
'''
N = random.randrange(5,15)
Z = random.randrange(2,6)

L1 = [random.randrange(1,5) for i in range(0,N)]
L2 = [0 for i in range(0,Z)]
L = L1 + L2

print(L1)
print(L2)
random.shuffle(L)
print(L)

s = 0
Sum = 0
flag = True
for x in L:
    if x == 0:
        if flag:
            flag = False
        else:
            Sum += s
        s = 0
    else:
        s += x

print("Sum = ",Sum)
print(s)

'''


26#
'''
import random
N = random.randint(0,10)
K = random.randint(0,10)

print('N = ',N)
print('K = ',K)



for i in range(0,N):
    x = random.randint(-10,10)
    A = 1
    for j in range(0,K):
        A *= x
    print("{0}. {1}^{2} = {3}".format(i+1,x,K,A))

'''

27,28#
'''
import random
N = random.randint(1,10)
print('N = ',N)


for i in range(0,N):
    x = random.randint(-10,10)
    K = i + 1
    k = 1
    for j in range(0,K):
        k *= x
    print(f'{i+1}: {x}^{K} = {k}')


for i in range(N): #for i in range(N,0,-1): (Можно еще запусть цикл в обратную сторону, как в этом примере)
    x = random.randint(-10,10)
    K = N - i
    k = 1
    for j in range(K):
        k *= x
    print(f'{i+1}: {x}^{K} = {k}')
'''


29,30,31,32,33,34#
'''
import random
N = random.randint(0,10)
K = random.randint(0,10)
print('N = ',N)
print('K = ',K)
S = 0
s = 0

for i in range(K):
    for j in range(N):
        x = random.randint(-10,10)
        print(x,end="; ")
        s += x


print()
print(s)

for i in range(K):
    S =0
    for j in range(N):
        x = random.randint(-10,10)
        print(x,end='; ')
        S += x
    print()
    print('Сумма каждой группы К:',S)

k = 0
for i in range(K):
    print()
    for j in range(N):
        x = random.randint(-10,10)
        print(x,end='; ')
        if x == 2:
            k += 1
            break
    print()

print()
print('Всего наборов К содержащих 2:',k)

z = 0
for i in range(K):
    k = 0
    print()
    flag = True
    for j in range(N):
        x = random.randint(0,10)
        print(x,end='; ')
        k += 1
        if x == 2 and flag:
            flag = False
            z = j
    print()
    if flag == True:
        print(0)
    else:
        print('Номер элемента:',z)
    print()

z = 0
for i in range(K):
    k = 0
    print()
    flag = True
    for j in range(N):
        x = random.randint(0,10)
        print(x,end='; ')
        k += 1
        if x == 2:
            flag = False
            z = j
    print()
    if flag == True:
        print(0)
    else:
        print('Номер элемента:',z)
    print()



for i in range(K):
    print()
    S = 0
    flag = True
    for j in range(N):
        x = random.randint(0,10)
        print(x,end='; ')
        S += x
        if x == 2:
            flag = False

    print()
    if flag == False:
        print(S)
    else:
        print(0)
    print()
'''


35,36,37,38#
'''
import random
K = random.randint(0,10)
print('K =',K)
S = []
L = []


for i in range(K):
    print()
    S = []
    x = random.randint(-10,10)
    print(x,end='; ')
    S.append(x)
    while x != 0:
        x = random.randint(-10,10)
        print(x,end='; ')
        S.append(x)
    print()
    print('Длина этого списка:',len(S) - 1)
    L.extend(S)
    print()

print()
print('Длина всех списков вместе:',len(L) - K)

k = 0
d = 0
for i in range(K):
    print()
    x_pred = random.randint(-10,10)
    print(x_pred,end='; ')
    x = random.randint(-10,10)
    print(x,end='; ')
    if x_pred < x:
        flag = True
    else:
        flag = False
    while True:
        x_pred = x
        x = random.randint(-10,10)
        print(x,end='; ')
        if x == 0:
            break
        if not (flag and x > x_pred):
            flag = False

    print()
    if flag:
        d +=1
print()
print('Всего наборов с возрастающими членами:',d)


k = 0
d = 0
for i in range(K):
    print()
    x_pred = random.randint(-10,10)
    print(x_pred,end='; ')
    x = random.randint(-10,10)
    print(x,end='; ')
    if x_pred < x:
        flag_v = True
    else:
        flag_v = False
    if x_pred > x:
        flag_u = True
    else:
        flag_u = False

    while True:
        x_pred = x
        x = random.randint(-10,10)
        print(x,end='; ')
        if x == 0:
            break
        if not (flag_v and x > x_pred) :
            flag_v = False
        if not (flag_u and x_pred > x):
            flag_u = False

    print()
    if flag_v:
        d += 1
    if flag_u:
        k += 1
print()
print('Всего наборов с возрастающими членами:',d)
print('Всего наборов с убывающими членами:',k)
print('Наборов в общем:',d+k)


k = 0
d = 0
for i in range(K):
    print()
    x_pred = random.randint(-10,10)
    print(x_pred,end='; ')
    x = random.randint(-10,10)
    print(x,end='; ')
    if x_pred < x:
        flag_v = True
    else:
        flag_v = False
    if x_pred > x:
        flag_u = True
    else:
        flag_u = False

    while True:
        x_pred = x
        x = random.randint(-10,10)
        print(x,end='; ')
        if x == 0:
            break
        if not (flag_v and x > x_pred) :
            flag_v = False
        if not (flag_u and x_pred > x):
            flag_u = False

    print()
    if flag_v:
        d = 1
        print('Набор с возрастающими членами:',d)
    elif flag_u:
        k = -1
        print('Набор с убывающими членами:',k)
    else:
        z = 0
        print('Невозрастающий и неубывающий набор:',z)

'''




39,40#
'''
import random
K = random.randint(0,10)
print('K = ',K)
k = 0
n = 0
z = 0

for i in range(K):
    print()
    n += 1
    print(n)
    left = random.randint(-1,1)
    print(left,end='; ')
    mid = random.randint(-1,1)
    print(mid,end='; ')
    right = random.randint(-1,1)
    print(right,end='; ')

    if left < mid < right:
        flag = True

    else:
        flag = False

    while True:
        left = mid
        mid = right
        right = random.randint(-1,1)
        print(right,end='; ')
        if right == 0:
            break
        if not (left < mid < right):
            flag = False
    print()
    if flag:
        z = n
        k += 1
print()
print(z,':',k)



for i in range(K):
    m = 0
    print()
    n += 1
    print(n)
    left = random.randint(-1,1)
    print(left,end='; ')
    m += 1

    mid = random.randint(-1,1)
    print(mid,end='; ')
    m += 1

    right = random.randint(-1,1)
    print(right,end='; ')
    m += 1


    if left < mid < right:
        flag = True

    else:
        flag = False

    while True:
        left = mid
        mid = right
        right = random.randint(-1,1)
        print(right,end='; ')
        m += 1
        if right == 0:
            break
        if not (left < mid < right):
            flag = False
    print()
    if flag:
        z = n
        k += 1
        print('Всего элементов в списке:',m)
print()
print(z,':',k)

'''








