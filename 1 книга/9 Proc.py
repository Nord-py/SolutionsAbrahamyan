1,2,3,4,5,6,7,8,9#
'''
def PowerA3(A):
    return A*A*A

for i in range(1,11):
    x = PowerA3(i)
    print(x)
'''

'''
def PowerA234(A):
    B = A * A
    C = B * A
    D = C * A
    return B,C,D

for i in range(1,11):
    x = PowerA234(i)
    print(i,':',x)
'''
'''
def Mean(X,Y):
    AMean = (X + Y) / 2
    GMean = (X * Y) ** (1 / 2)
    return AMean,GMean

import random
A,B,C,D = random.sample(range(0,100),4)
print(A,B,C,D)

print(Mean(A,B))
print(Mean(A,C))
print(Mean(A,D))
'''
'''
def TrianglePS(a):
    P = 3 * a
    S = (a**2 * 3**(1/2)) / 4
    return f"P = {P} ; S = {S}"


for i in range(1,11):
    x = TrianglePS(i)
    print(i,':',x)
'''


'''
def RectPC(x1,y1,x2,y2):
    s1 = abs(x1 - x2)
    s2 = abs(y1 - y2)
    P = 2*s1 + 2*s2
    S = s1 * s2
    return f'Периметр равен = {P} \nПлощадь равна = {S} '


import random
x1,y1,x2,y2 = random.sample(range(-10,10),4)
print('x1 = ',x1,'; y1 =',y1)
print('x2 = ',x2,'; y2 =',y2)


print(RectPC(x1,y1,x2,y2))

'''

'''
def DigitCountSum(C):
    S = str(C)
    d = len(S)
    Sum = 0
    for i in range(d):
        Sum += int(S[i])

    return f'Количество цифр в числе: {d} \nСумма этих цифр: {Sum} '


for i in range(1,6):
    x = random.randint(1,1000)
    print('x =',x)
    print()
    print(DigitCountSum(x))
    print()
'''
'''
import random

def InvertDigits(K):
    S = str(K)
    f = S[::-1]
    K = int(f)
    return f'Измененное число: {K}'


for i in range(1,6):
    x = random.randint(1,1000)
    print('x =',x)
    print()
    print(InvertDigits(x))
    print()

'''

'''
def AddRightDigit(D,K):
    K = str(K)
    D = str(D)
    N = K + D

    return  N

import random
K = random.randint(1,10000)
D = 0
print('K = ',K)
print()

for i in range(1,6):
    D = random.randint(1,9)
    print('D = ',D)
    print(AddRightDigit(D,K))
    K = AddRightDigit(D,K)

'''




10,11,12,13,14,15#
'''
def Swap(X,Y):
    X,Y = Y,X
    return f'Измененные Х и У: {X} ; {Y}'

import random
A,B,C,D = random.sample(range(-10,10),4)
print('A = ',A)
print('B = ',B)
print('C = ',C)
print('D = ',D)
print()
print('A : B')
print(Swap(A,B))
print('C : D')
print(Swap(C,D))
print('B : C')
print(Swap(B,C))
'''


'''
def Minmax(X,Y):
    if X < Y:
        return f'Минимальное: {X}; Максимальное: {Y}'
    else:
        return f'Минимальное: {Y}; Максимальное: {X}'


import random
for i in range(1,6):
    X,Y = random.sample(range(-10,10),2)
    print(X,Y)
    print(Minmax(X,Y))

'''

'''
def SortInc3(A,B,C):
    S = []
    S.append(A)
    S.append(B)
    S.append(C)
    S.sort()
    return f'Упорядоченный по возрастанию список: {S}'

def SortDec3(A, B, C):
    S = []
    S.append(A)
    S.append(B)
    S.append(C)
    S.sort(reverse = True)
    return f'Упорядоченный по убыванию список: {S}'




import random
for i in range(1,4):
    A,B,C = random.sample(range(-10,10),3)
    print(A,B,C)
    print(SortInc3(A,B,C))

for i in range(1,4):
    A,B,C = random.sample(range(-10,10),3)
    print(A,B,C)
    print(SortDec3(A,B,C))

'''
'''
def ShiftRight3(A, B, C):
    D = C
    C = B
    B = A
    A = D

    return A,B,C

import random
for i in range(1,4):
    A,B,C = random.sample(range(-10,10),3)
    print(A,B,C)
    print(ShiftRight3(A,B,C))

'''



16,17,18#
'''
import random

def Sign(x):
    if x < 0:
        return -1
    elif x == 0:
        return 0
    else:
        return 1


A,B = random.sample(range(-10,10),2)
print(A,B)

print(Sign(A) + Sign(B))
'''
'''
import random

def RootsCount(A, B, C):
    D = B ** 2 - 4 * A * C
    if D > 0 :
        return 'Уравнение имеет 2 корня'
    elif D == 0:
        return 'Уравнение имеет 1 корень'
    else:
        return 'В вещественных числах уравнение не имеет корней'


A = B = C = 0
while A == 0:
    A,B,C = random.sample(range(-10,10),3)

print(A,B,C)
D = B ** 2 - 4 * A * C
print(D)
print(RootsCount(A,B,C))
'''

'''
import random,math

def CircleS(R):
    S = math.pi * R ** 2
    return S

R = random.randint(0,10)
print(R)
print(CircleS(R))
'''


21#
'''
import random

def SumRange(A,B):
    if A > B:
        return f'A больше В: {0}'
    else:
        S = 0
        for i in range(A,B+1):
            print(i)
            S += i

    return f'Cумма от А до В: {S}'


A,B,C = random.sample(range(-10,10),3)
print(A,B,C)
print(SumRange(A,B))
print(SumRange(B,C))
'''



22#
'''
import random

def Calc(A,B,Op):
    if Op == 1:
       return  A - B
    elif Op == 2:
        return A * B
    elif Op == 3:
        return A / B
    else:
        return A + B

A,B = random.sample(range(-10,10),2)
Op = random.randint(1,4)
print(A,B)
print(Op)
if B == 0:
    B = random.randint(-10,10)
    print(B)

print(Calc(A,B,Op))
'''


23#
'''
import random

def Quarter(x,y):
    if x > 0 and y > 0:
        return '1 четверть'
    elif x > 0 and y < 0:
        return '4 четверть'
    elif x < 0 and y < 0:
        return '3 четверть'
    elif x < 0 and y > 0:
        return '2 четверть'
    else:
        return 'Ось'


x,y = random.sample(range(-10,10),2)
print(x,y)
print(Quarter(x,y))
'''


26#
'''
import random
import math

def IsPower5(K):
    x = int(math.log(K,5))
    if K == 5**x:
        return True
    return False

s = 0
L = [5**random.randrange(1,10)+random.randrange(0,2) for i in range(0,10)]
for i in range(0,len(L)):
    x = L[i]
    print(x,end="; ")
    s += int(IsPower5(x))

print("\nAmount of IsPower5:",s)


'''

27#
'''
import random
import math

def IsPower(K,N):
    x = int(math.log(K,N))
    if K == N ** x:
        return True
    return False



for i in range(2,11):
    K = random.randint(2,100)
    N = random.randint(2,10)
    print(K,N)
    print(IsPower(K,N))


'''

28#
'''
import random

def IsPrime(N):
    if N == 2  or N == 3 or N == 5 or N == 7:
        return True
    for i in range(2,10):
        if N % i == 0:
            return False
    else:
        return True


for i in range (0,10):
    x = random.randint(2,100)
    print(x,':',IsPrime(x))
'''


29#
'''
import random

def DigitCount(K):
    i = 0
    while K != 0:
        K /= 10
        i += 1
        K = int(K)
    return i

for i in range(0,5):
    K = random.randint(1,1000)
    print(K,':',DigitCount(K))

'''

31#
'''
import random

def Palindrom(K):
    return int(str(K) + str(K)[::-1])

def IsPalindrom(K):
    result = False
    num = str(K)
    try:
        #val = int(num)
        if num == str(num)[::-1]:
            result = True
    except ValueError:
        print("That's not a valid number, Try Again !")
    return result

def IsPalindrom2(n):
    temp=n
    rev=0
    while(n>0):
        dig=n%10
        rev=rev*10+dig
        n=n//10
    if(temp==rev):
        result = True
    else:
        result = False
    return result


for i in range(0,10):
    x = random.randrange(1,10000)
    #x = Palindrom(x)
    #print(x,":",IsPalindrom(x))
    #print(x,":",IsPalindrom2(x))
    print(x,':',Palindrom(x))
'''


34#
'''
import random

def Fact(N):
    if N == 1:
        return 1
    else:
        return N * Fact(N - 1)

for i in range(1,6):
    x = random.randint(1,10)
    print(x,':',Fact(x))
'''


35#
'''
import random

def Fact(N):
    if N == 1:
        return 1
    else:
        return N * Fact(N - 1)

for i in range(1,6):
    x = random.randint(1,4)
    y = Fact(x)
    print(x,':',y)
    print(x,':',Fact(y))
'''



36#
'''
import random

def Fib(N):
    F1 = 1
    F2 = 1
    if N <= 2:
        return 1
    while N > 2:
        F3 = F1 + F2
        F1 = F2
        F2 = F3
        N -= 1
    return F3

for i in range(1,10):
    x = random.randint(1,30)
    print(x,':',Fib(x))

'''



37,38,39#
'''
import random,math

def Power1(A,B):
    if A <= 0:
        return 0
    else:
        K = math.exp(B * math.log(A))
        K1 = A ** B
        return K,K1

for i in range(0,5):
    A = random.randint(-10,10)
    B = random.randint(-10,10)
    print('A =',A,'B =',B)
    print(i+1,':',Power1(A,B))


def Power2(A,N):
    K = 1
    if N == 0:
        return 1
    elif N > 0:
        for i in range(0,N):
            K *= A
        return K
    else:
        for i in range(0,abs(N)):
            K *= 1 / A
        return K

for i in range(0,5):
    A = random.randint(1,10)
    B = random.randint(-10,10)
    print('A =',A,'B =',B)
    print(i+1,':',Power2(A,B),':',A**B)



def Power3(A,B):
    if B % 1 == 0:
        return print(Power2(A,B))
    else:
        return print(Power1(A,round(B)))


for i in range(0,5):
    A = random.uniform(0,10)
    B = random.uniform(0,5)
    print('A =',A,'B =',B)
    print(i+1,':',Power3(A,B))
'''




40#
'''
import random,math

def Fact(x):
     if x == 1:
         return 1
     else:
         return x * Fact(x-1)


def Exp1(x,e):
    S = 1
    if e <= 0:
        return print('Эпсилон должен быть больше нуля!')
    else:
        for i in  range(1,1000):
            k = x ** i / Fact(i)
            if k > e:
                S += k
        return S


x = random.randint(1,10)
x = 1
for i in range(0,6):
    print()
    e = random.uniform(0,0.01)
    print('X=',x , ';', 'E=',e)
    print('Приблеженный расчет функции = ',Exp1(x,e),';', f'e^{x} = ', math.exp(x))
'''

46,47#
'''

def Nod2(A,B):
    if B != 0:
        while B != 0:
            A,B=B,A%B
        return A
    else:
        return A


A,B,C,D = random.sample(range(0,100),4)
print(A,B,C,D)
print(Nod2(A,B))
print(Nod2(A,C))
print(Nod2(A,D))



import random

def Frac1(a,b,p,q):
    L = []
    Numerator = a*q + b*p
    Denominator = b*q
    Divisor = Nod2(Numerator, Denominator)
    L.append(int(round(Numerator / Divisor)))
    L.append(int(round(Denominator / Divisor)))
    return L

for i in range(0,4):
    A = random.randrange(1,1000)
    B = random.randrange(1,1000)
    C = random.randrange(1,1000)
    D = random.randrange(1,1000)
    #A = 1
    #B = 2
    #C = 1
    #D = 3
    print(A,";",B,";",C,";",D,";",Frac1(A,B,C,D))

'''


48#
'''
import random

def Nod2(A,B):
    if B != 0:
        while B != 0:
            A,B=B,A%B
        return A
    else:
        return A



def Nok2(A,B):
    N = A * B / Nod2(A,B)
    return N


A,B,C,D = random.sample(range(1,100),4)
print(A,B,C,D)
print(Nok2(A,B))
print(Nok2(A,C))
print(Nok2(A,D))
'''




49#
'''
import random

def Nod2(A,B):
    if B != 0:
        while B != 0:
            A,B=B,A%B
        return A
    else:
        return A


def Nod3(A,B,C):
    A1 = Nod2(A,B)
    B1 = Nod2(A1,C)
    return B1

Или по другому:
    return NOD2(NOD2(A,B),C)
    Это равносильно

A,B,C,D = random.sample(range(1,1000),4)
print(A,B,C,D)
print(Nod3(A,B,C))
print(Nod3(A,C,D))
print(Nod3(B,C,D))
'''


50#
'''
import random

def TimeToHMS(T):
    H = 0
    M = 0
    S = 0
    while T > 3600 :
        T -= 3600
        H += 1
    while T > 60:
        T -= 60
        M += 1

    S = T
    return ('Hours=' , H, 'Minutes:' , M, 'Seconds:', S)


for i in range(0,5):
    x = random.randint(0,10000)
    print('x=',x)
    print(TimeToHMS(x))

'''


52#
'''
L = [2016,300,1300,1900,1200,2000]

def IsLeapYear(Y):
    result = False
    if (Y%4 == 0) and not(Y%100 == 0 and Y%400 != 0):
        result = True
    return result

for i in L:
    s = "не високосный"
    y = IsLeapYear(i)
    if IsLeapYear(i):
        s = "високосный"

    print(i," : ",s)

'''


56,57#
'''
import random,math

def Leng(x1, y1, x2, y2):
    AB = math.sqrt((x1-x2)**2+(y1-y2)**2)
    return AB


for i in range(0,5):
    A_x = random.randint(-10,10)
    A_y = random.randint(-10,10)
    B_x = random.randint(-10,10)
    B_y = random.randint(-10,10)
    print('A_x=', A_x,'; B_x=',B_x,'; A_y=',A_y,'; B_y=',B_y)
    print(Leng(A_x,A_y,B_x,B_y))




def Perim(x_a,   y_a,   x_b,  y_b,  x_c,  y_c):
    AB = Leng(x_a,   y_a,   x_b,   y_b)
    BC = Leng(x_b,   y_b,   x_c,   y_c)
    CA = Leng(x_c,   y_c,   x_a,   y_a)
    P = AB + BC + CA
    return P


for i in range(0,5):
    x_a = random.randint(-10,10)
    y_a = random.randint(-10,10)
    x_b = random.randint(-10,10)
    y_b = random.randint(-10,10)
    x_c = random.randint(-10,10)
    y_c = random.randint(-10,10)
    print('A:',x_a,'и',y_a, ';B:',x_b,'и',y_b, ';C:',x_c,'и',y_c)
    print(Perim(x_a,   y_a,   x_b,  y_b,  x_c,  y_c))
'''

























