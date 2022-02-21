1#
#import random
#N=random.randint(1,1000)
#K=random.randint(-1000,1000)
#print(N,K)
#for i in range(0,N):
#    print(i+1," : ",K)


2,3#
#import random
#A,B=sorted(random.sample(range(-10,10),2))
#print(A,B)
#print('Список i:')

#for i in range(A,B+1):
#   print(i)

#print('Количество этих чисел:', B-A+1)

#for i in range(A+1,B):
 #   print(i)

#print('Количество этих чисел:', B-A-1)




4,5,6#
#import random

#def frange(start,stop,step):
#    i=start
#    while i<=stop:
##        yield i# для float
  #      i+=step

#x=round(random.uniform(100,180),2)# round-Округление числа
#print('x=',x)

#for i in range(1,11):
#    print(i,':',x*i)

#for i in frange(1.2, 2.0, 0.2):
 #   print(round(i,1),':',round(x*i,2))






7,8,9#
#import random
#A,B=sorted(random.sample(range(-10,10),2))
#print('A=',A)
#print('\v''B=',B)
#print('\v''All i:')
##S=0
#P=1
#S2=0

#for i in range(A,B+1):
#    print('\v''i=',i)
 #   S+=i
  #  P*=i
   # S2+=i*i
#print('Sum all i=',S)
#print('Произведение all i=',P)
#print('Сумма квадратов all i:',S2)




10,11,12,13,14#
#import random
#N=random.randint(1,10)
#print('N=',N)
#S=0.0
#for i in range(1,N+1):
#    print(round(1/i,3))
#    S+=1/i

#print('Сумма ряда=',round(S,2))

#for i in range(N,2*N+1):
 #   print(i**2)
  #  S += i**2

#print("Sum = ",S)

#P = 1.0
#for i in range(1,N+1):
 #   print(1 + i*0.1)
  #  P *= 1 + i*0.1

#print("Product = ",P)

#for i in range(1,N+1):
 #   print(1+i*0.1)
  #  x=1+i*0.1
   # S+=x*(-1)**(i+1)
#print(round(S,2))

#for i in range(1,N+1):
  #  x=2*i-1
   # S+=x
    #print(i)

#print(S)




15,16,17,18,19,20,21#
#import random
#import math
#N=random.randint(1,10)
#A=random.uniform(1,10)
#print('N=',N)
#print('A=',round(A,2))
#S=1#Иногда S=1, т.к. ряд фактариалов начинается с 1
#P=1

#for i in range(1,N+1):
 #   P*=A
  #  print(i," : ",round(P,2))

#print(round(P,2))


#for i in range(1,N+1):
 #   x=A**i
  #  print(x)

#for i in range(1,N+1):
 #   S+=A**i
  #  print(A**i,':',S)


#for i in range(0,N+1):
 #   S+=((-1)**i)*A**i
  #  print((-A)**i,':',S)

#for i in range(1,N+1):
 #   P*=i
  #  print(P)

#for i in range(1,N+1):
 #   P*=i
  #  S+=P
   # print(P,':',S)

#for i in range(1,N+1):
 #   P*=1/i
  #  S+=P
   # print(i,':',P)
#print(S)#Полученное выражение является приближенным значением экспоненты e = exp(1).
#print("e = ",math.exp(1))






'''

22,23,24#

import random
import math
X=random.uniform(-10,10)
print('X=',X)
N=random.randint(1,10)
print('N=',N)
S=1
P=1.0
K=2

for i in range(1,N+1):
    P*=i
    S+=(X**i)/P
    print(i,':',P,':',S)
print(S)#Приближенное значение 'е' в точке Х

print("e:")
print(math.exp(X))


for i in range(1,N+1):
    P*=i*K
    S+=(-1)**i * X**(2*i+1)/P
    K+=4
    print(i, ':', P, ':', S)
print(S)
print(math.sin(X))



for i in range(1,N+1):
    P*=i*K
    S+=(-1)**i * X**(2*i)/P
    K+=4
    print(i, ':', P, ':', S)
print(S)
print(math.cos(X))

'''



25,26,27#
#import random
#import math
#X=random.uniform(-1,1)
#N=random.randint(1,10)
#print('X=',X)
#print('N=',N)
#S=X

#for i in range(1,N+1):
#    S+=X**i/i*(-1)**(i-1)
#    print(i,':',S)
#print(S)
#print(math.log(1+X))


#for i in range(0,N+1):
#    S+=(-1)**i * X**(2*i+1) / (2*i+1)
#    print(i, ':', S)
#print(S)
#print(math.atan(X))


#Z=1
#for i in range(1,N+1):
#    Z=((2*i) * (2*i+1))
#    S+=((2*i-1) * X**(2*i+1)) / Z
#    print(i, ':', S, ':', Z)

#print(S)
#print(math.asin(X))




29#
#import random
#import math
#N=random.randint(2,15)
##A=random.uniform(0,10)
#B=random.uniform(0,10)
#A=2.0
#B=12.0
#N=5
#while A>B:
##    A=random.uniform(0,10)
 #   continue
#print('A=',A)
#print('B=',B)
#print('N=',N)#

#S=B-A
#H=S/N
#print('S=',S)
#print('H=',H)

#x=A
#for i in range(0,N):
#    print(x,end=', ')
#    x+=H
#print(x)


#x=A
#for i in range(0,N+1):
##    y=1-math.sin(x)
 #   print("{0:.2f} : {1:.4f}".format(x,y))
 #   x += H














#30,31,32,33,34,35 - были сделанны, но программа слетела....

















36,37,38#
#import random
#N,K=random.sample(range(1,10),2)
#N=10
#S=0.0
#K=K+S

#print('N=',N)
#print('K=',K)

#for i in range(1,N+1):
#    S+=i**K
#    print(i, ':', S)
#print(S)


#for i in range(1,N+1):
#    S+=i**i
#    print(i, ':', S)
#print(S)


#for i in range(1,N+1):
#    S+=i**(N+1-i)
#    print(i, ':', S)
#print(S)





39,40#
import random
A,B=sorted(random.sample(range(1,10),2))
print('A=',A)
print('B=',B)

#for i in range(A,B+1):
#    for j in range(0,i):
#        print(i,end=" ")


k=1
for i in range(A,B+1):
    for j in range(0,k):
        print(i,end=" ")
    print()
    k+=1





























