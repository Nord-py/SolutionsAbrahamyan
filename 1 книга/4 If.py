
1#
#import random
#x=random.randint(-10,10)
#print('x=',x)

#if x>0:
#    x=x+1
#else:
#    x

#print('x=',x)






4,5#
#import random
#x,y,z=[random.randrange(-5,5) for i in  range(0,3)]
#print('x=',x)
#print('y=',y)
#print('z=',z)
#S = 0
#S_=0
#if x > 0:
#    S += 1
#elif x<0:
##    S_ +=1

#if y > 0:
#    S += 1
#elif y<0:
#    S_ +=1
#if z > 0:
#    S += 1
#elif z<0:
#    S_ +=1

#print("Количество положительных чисел: ", S)
#print("Количество отрицательных чисел: ", S_)






6.7#
#import random
#x,y=[random.randrange(-5,5) for i in  range(0,2)]
#print('x=',x)
#print('y=',y)
#if x>y:
#    a=x
#    min_=2
#else:
#    a=y
#   min_=1
#print("Большее число=", a)
#print('Номер меньшего числа=', min_)







9#
#import random
#A=random.uniform(1,10)
#B=random.uniform(1,10)
#print('A=',A)
#print('B=',B)
#C=0
#if A>B:
    #A,B=B,A
#    C=A
 #   A=B
  #  B=C
   # print('A было больше В')
   # print('A=',A)
#    print('B=',B)
#else:
#    print('A было меньше В')
#    print('A=',A)
 #   print('B=',B)






11#
#import random
#x=random.randint(-10,10)
#y=random.randint(-10,10)
#print('x=',x)
#print('y=',y)
#if x!=y:
#    x=y=max(x,y)
#else:
#    x=y=0

#print('x=',x)
#print('y=',y)




12,13,14,15#
#import random
#A,B,C=[random.randint(1,10) for i in range(0,3)]
#print('A=',A)
#print('B=',B)
#print('C=',C)

#if A<B and A<C:
 #   print('Наименьшее число:',A)
#elif B<A and B<C:
#    print('Наименьшее число:',B)
#else:
#    print('Наименьшее число:',C)

#if (A>=B and A<=C) or (A>=C and A<=B):
#    print('Среднее число:',A)
#elif (B>=A and B<=C) or (B<=A and B>=C):
#    print('Среднее число:',B)
#else:
#    print('Среднее число:',C)


#if A<B and A<C:
 #   m=A
  #  print('Наименьшее число:',A)
#elif B<A and B<C:
 #   m=B
  #  print('Наименьшее число:',B)
#else:
 #   m=C
  #  print('Наименьшее число:',C)
#
#print("Наименьшее:",m)
##
#if A>B and A>C:
 #   n=A
  #  print('Наибольшее число:',A)
#elif B>A and B>C:
 #   n=B
  #  print('Наибольшее число:',B)
#else:
 #   n=C
  #  print('Наибольшее число:',C)
#
#print(m,n)


#if A>B and A>C:
 #   n=A
  #  print('Наибольшее число:', A)
#elif B>A and B>C:
 #   n=B
  #  print('Наибольшее число:',B)
#else:
 #   n=C
  #  print('Наибольшее число:',C)


#if (A>=B and A<=C) or (A>=C and A<=B):
 #   m=A
  #  print('Среднее число:',A)
#elif (B>=A and B<=C) or (B<=A and B>=C):
 #   m=B
 #   print('Среднее число:',B)
#else:
  #  m=C
   # print('Среднее число:',C)


#print('Сумма двух наибольших чисел, равна=',m+n)






16#
#import random
#A,B,C=[random.uniform(-10,10) for i in range(0,3)]
#print('A=',A)
#print('B=',B)
#print('C=',C)
#if A<B and A<C and B>A and B<C and C>A and C>B:
#    print('Ряд упорядочен по возростанию, удвоим его:')
#    A=2*A
#   B=2*B
#    C=2*C
#    print(A,B,C)
#else:
##    A=-A
 #   B=-B
 #   C=-C
 #   print(A,B,C)




18#
#import random
#A,B,C=[random.randint(0,3) for i in range(0,3)]
#A=B=C=1
#print('A=',A)
#print('B=',B)
#print('C=',C)

#if A==B and A!=C:
#    print('C')
#elif A==C and A!=B:
#    print('B')
#elif B==C and B!=A:
#    print('A')
#else:
#    print('Не удовлетворяет условию задачи')






20#
#import random
#A,B,C=[random.randint(-10,10) for i in range(0,3)]
#print('A=',A)
#print('B=',B)
#print('C=',C)
#l1=abs(A-B)
#l2=abs(A-C)
#if l1<l2:
 #   print('Точка В ближе к точке А')
  #  print('B=',B)
   # print('Расстояние до точки:',l1)
#elif l2<l1:
 #   print('Точка C ближе к точке А')
  #  print('C=',C)
   # print('Расстояние до точки:',l2)
#lse:
 #   print('Точки находятся на одинаковом растоянии')
  #  print(l1)




21#
#import random
#x,y=[random.randint(-10,10) for i in range(0,2)]
#print('(x;y)=({0};{1})'.format(x,y))

#if x==0 and y==0:
#    print(0)
#elif x==0:
#    print(1)
#elif y==0:
#    print(2)
#else:
#    print(3)




23#СЛОЖНО!!!
#import random
##x,y,x1=[random.randint(-10,10) for i in range(0,3)]
#print('A=',A)
#print('B=',B)
#print('C=',C)



24,27#
#import random
#import math
#x=random.uniform(-1,10)
#print('x=',x)
#if x>0:
 #   x1=2*math.sin(x)
  #  print("f(x)=",x1)
#else:
 #   x2=6-x
  #  print("f(x)=",x2)
#x_floor = math.floor(x)#округление вниз
#if x<0:
#    print(0)
#elif x_floor%2==0:
#    print(1)
#else:
#    print(-1)





28#
#import random
#year=random.randint(1,3000)
#year=2200
#print(year)

#if year%4==0 and (year%100!=0 or year%400==0):
#    print('Високосный=', year)
#else:
#    print("Не високосный")







29#
import random
x=random.randint(-10,10)
print('x=',x)
if x<0 and x%2!=0:
    print('Отрицательное нечетное число:', x)
elif x<0 and x%2==0:
    print('Отрицательное четное чиcло:', x)
elif x==0:
    print('Нулевое:', x)
elif x>0 and x%2==0:
    print('Положительное четное число:', x)
else:
    print('Положительное нечетное число:', x)













