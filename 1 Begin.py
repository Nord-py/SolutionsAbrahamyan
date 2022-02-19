1#
#a=int(input('Введите сторону квадрата: '))
#P=4*a
#print("Периметр квадрата P = ", P)


3#
#a=int(input('Введите сторону прямоугольника: '))
#b=int(input('Введите сторону прямоугольника: '))
#S=a*b
#P=(a+b)*2
#print("Площадь = ",S)
#print("Периметр = ",P)


4#
#import math
#d=int(input("Введите диаметр: "))
#L= math.pi*d
#print("Длинна окрожности = ", L)


10#
#import random
#a = random.randrange(1,15)
#b = random.randrange(1,15)
#print(a, b)
#a1=a**2
#b1=b**2
#print(a1+b1)
#print(a1-b1)
#print(a1*b1)
#print(a1/b1)


13#
#import random
#import math
#R1=random.randrange(1,10)
#R2=random.randrange(1,R1)
#S1=math.pi*R1**2
#S2=math.pi*R2**2
#S3=S1-S2
#print(S1,S2,S3)


16#
#import random
#x1=random.randrange(-10,10)
#x2=random.randrange(-10,10)
#x3=abs(x2-x1)
#print(x1,x2)
#print(x3)

17#
#import random
#A,B,C = sorted(random.sample(range(-10, 10), 3))
#print(A,B,C)
#print(abs(A-C))
#print(abs(B-C))
#print(abs(A-C)+abs(B-C))


18#
#import random
#A,C,B = sorted(random.sample(range(-10, 10), 3))
#print(A,C,B)
#print(abs(A-C))
#print(abs(A-B))
#print(abs(A-C)*(abs(A-B)))



19#
#import random
#x1,x2= random.sample(range(-10,10),2)
#y1,y2= random.sample(range(-10,10),2)

#print("(x1,y1): ({0},{1})".format(x1,y1))
#print("(x2,y2): ({0},{1})".format(x2,y2))
#str1=abs(x1-x2)
#str2=abs(y1-y2)
#P=2*(str1*+str2)
#S=str1*str2
#print(str1,str2,P,S)



20#
#import random
#import math
#x1,x2=random.sample(range(-10,10),2)
#y1,y2=random.sample(range(-10,10),2)
#print("Точка 1 = (x1,y1) : ({0},{1})".format(x1,y1))
#print("Точка 2 = (x2,y2) : ({0},{1})".format(x2,y2))
#Rastoynie=math.sqrt((x2-x1)**2+(y2-y1)**2)
#print(Rastoynie)



21#
#import random
#import math
#def Rastoynie(A,B):
#     return math.sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2)

#x1,x2,x3=sorted(random.sample(range(-10,10),3))
#y1,y2,y3=sorted(random.sample(range(-10,10),3))

#print("Точка 1 = (x1,y1) : ({0},{1})".format(x1,y1))
#print("Точка 2 = (x2,y2) : ({0},{1})".format(x2,y2))
#print("Точка 3 = (x3,y3) : ({0},{1})".format(x3,y3))


#d1=Rastoynie([x1,y1],[x2,y2])
#print(d1)

#d2=Rastoynie([x1,y1],[x3,y3])
#print(d2)

#d3=Rastoynie([x2,y2],[x3,y3])
#print(d3)

#p=(d1+d2+d3)/2
#print(p)

#S=math.sqrt(p*(p-d1)*(p-d2)*(p-d3))
#print(S)




22#
#import random
#A=random.randrange(-10,10)
#B=random.randrange(-10,10)
#print(A,B)
#C=None
#if A!=B:
#    C=A
 #   A=B
  #  B=C
   # print(A,B)
#else:
 #   print("A=B")



#A,B = B,A
#print("A = {0}, B = {1}".format(A,B))




23#
#import random
#A,B,C=random.sample(range(-10,10),3)
#print(A,B,C)
#D=None

#D=C
#C=B
#B=A
#A=D
#print(A,B,C)


25#
#import random
#x=random.randrange(0,10)
#print(x)
#y=3*x**6-6*x**2-7
#print(y)


27#
#import random
#x=random.randrange(2,10)
#print(x)
#x=x*x
#print("x^2 = ",x)
#x=x*x
#print("x^4 = ",x)
#x=x*x
#print("x^8 = ",x)




28#
#import random

#A = random.randrange(0, 10)
#print("A = ",A)
#x = A*A
#print("A^2 = ",x)
#A = x*A
#print("A^3 = ",A)
#A = x*A
#print("A^5 = ",A)
#x = A*A
#print("A^10 = ",x)
#A = x*A
#print("A^15 = ",A)



33#
#import random
#x,y=sorted(random.sample(range(1,10),2))
#print(x,y)
#A=random.randrange(1000,10000)
#print(A)
#K=A/x
#y=K*y
#print(" 1 килограмм = ",K)
#print(" y килограмм = ",y)





34#
#import random
#x,y=sorted(random.sample(range(1,15),2))
#print(x,y)
#A=random.randrange(3000,5000)
#B=random.randrange(1000,2000)
#print(A,B)
#K2=B/y#ириски
#K1=A/x#шоколдные
#print(K1,K2)
#print("Шоколаадные дороже ирисок в = ", K1/K2)





35#
#import random
#V=random.randrange(20,100)#Скорость лодки
#U=random.randrange(1,10)#Скорость реки
#T1=random.randrange(1,5)#Время движения по озеру
#T2=random.randrange(1,5)#Время движения по реке (против течения)
#S1=V*T1#Путь по озеру
#S2=(V-U)*T2#Путь по реке
#print(V,U,T1,T2,S1,S2)


38#
#import random
#A,B=random.sample(range(-100,100),2)
#if A!=0:
#    x=-B/A
#    print(A,B)
#    print(x)
#else:
#    print('Нет решний')



39#
#import random
#mport math
#A,B,C=sorted(random.sample(range(-10,10),3))
#print("A = ", A)
#print("B = ", B)
#print("C = ", C)
#D=B**2-4*A*C
#print("D =",D)
#if A!=0 and D>0:
#    x1=(-B+math.sqrt(D))/(2*A)
#    x2=(-B-math.sqrt(D))/(2*A)
#    print("x1 =", x1)
#    print("x2 =", x2)
#    print(x1<x2)
#    if x1<x2:
#        a=x1
#    else:
#        a=x2
#    print(a)
#else:
#    print("A=0 or D<0 ; Нет решений")





40#
import random
A1,B1,C1,A2,B2,C2=random.sample(range(-10,10),6)
print("A1 = ",A1)
print("B1 = ",B1)
print("C1 = ",C1)
print("A2 = ",A2)
print("B2 = ",B2)
print("C2 = ",C2)
D=A1*B2-A2*B1
print("D=",D)
x=(C1*B2-C2*B1)/D
x=round(x,30)#Тут я увеличивал точность после запятой, те ошибки, что возникают, это проблемы с округлением
y=(A1*C2-A2*C1)/D
y=round(y,30)
print("x=",x)
print("y=",y)
print(A1*x+B1*y)
print(A2*x+B2*y)
if A1*x+B1*y==C1 and A2*x+B2*y==C2:
    print("x и y решения системы линейных уравнений" )
else:
    print("x и у не подходят системе")
