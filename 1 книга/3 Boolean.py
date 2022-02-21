1,4,6,10,14#
#import random
#A=random.randint(-10,10)
#B=random.randint(-10,10)
#C=random.randint(-10,10)
#print('A=',A)
#print('B=',B)
#print('C=',C)
#print('Число А является положительным:', A>0)
#print('Справедливы неравенства:', A>2 and B<=3)
#print('Справедливо двойное неравество:',A<B and B<C)

#x=A%2!=0
#y=B%2!=0
#z=x!=y
#print(' Х нечетноp:',x)
#print(' У нечетно:',y)
#print('Ровно одно из чисел нечетно:', z)

#if A>0 and B>0 and C>0 :
 #   print('Все числа положительные')
#elif A>0 and B>0 :
#    print('А и В положительные')
#elif A>0 and C>0 :
#    print('А и С положительные')
#elif B>0 and C>0:
#    print('В и С положительные')
#elif A<0 and B<0 and C<0:
#    print('Все числа отрицательные')
#else:
#    print('Ровно одно число положительно')






16#
#import random
#A=random.randint(0,100)
#print('A=',A)
#print("Число двузначно и четно?", A>=10 and A<=99 and A%2==0)



18,19#
#import random
#A,B,C=random.sample(range(-10,10),3)
#print(A,B,C)
#print('Среди трех данных целых чисел, есть хотя бы одна пара совпадающиx?', A==B or B==C or A==C)
#print('Среди трех данных целых чисел есть хотя бы одна пара взаимно противоположных?', A==-B or B==-C or A==-C)


20,21,22#
#import random
#A=random.randint(100,999)
#print(A)
#a=int(A/100)#1 цифра
#b=int(int(A/10)%10)#2 цифра
#c=int(A%10)#3 цифра
#print(a,b,c)
#print('Все цифры данного числа различны?', a!=b and b!=c and c!=a)
#print('Цифры данного числа образуют возрастающую последовательность?',a<b and b<c)
#print('Цифры данного числа образуют возрастающую или убывающую последовательность?',(a<b and b<c) or (a>b and b>c))



24#
#import random
#A,B,C=random.sample(range(-10,10),3)
#D=B**2-4*A*C
#print('A=',A)
#print('B=',B)
#print('C=',C)
#print('D=',D)
#x=(D>=0)
#y=(D<0)
#if A!=0 and D>0:
#    print('Уравнение A*x^2+B*x+C=0 имеет вещественные корни:', x)
#else:
#    print('Вещественных корней - нет:',y)





25,27#
#import random
#x,y=random.sample(range(-10,10),2)
#print(x,y)
#A=(x<0 and y>0)
#B=(x<0 and y<0)
#print('Точка с координатами:({x};{y}) лежит во второй координатной четверти?:'.format(x=x,y=y), A)
#print('Точка с координатами ({x};{y}) лежит во второй или третьей координатной четверти?:'.format(x=x,y=y),A or B)





29#
#import random
#x1,x2=sorted(random.sample(range(-10,10),2))
#y2,y1=sorted(random.sample(range(-10,10),2))
#x,y=random.sample(range(-5,5),2)
#print('x=',x)
#print('y=',y)
#print('x1=',x1)
#print('y1=',y1)
#print('x2=',x2)
#rint('y2=',y2)
#if x>x1 and x<x2 and y<y1 and y>y2:
#    print('Точка с координатами ({x};{y}) внутри прямоугольника)'.format(x=x,y=y))
#lif x<x1 or x>x2 or y>y1 or y<y2:
#   print('Точка с координатами ({x};{y}) вне прямоугольника)'.format(x=x,y=y))
#else:
#   print('Точка с координатами ({x};{y}) на границе прямоугольника)'.format(x=x,y=y))




30,31,32,33#Моя программа
#import random
#a,b,c=sorted(random.sample(range(1,10),3))
#print(a,b,c)
#while a>b+c or b>a+c or c>b+a:
#    a,b,c=sorted(random.sample(range(1,10),3))
#    continue#
#
#print(a,b,c)#
#
#if c*c==a*a+b*b:
#    print('Треугольник прямоугольный')
#elif a==b==c:
#    print('Трегольник равносторонний')
#elif a==b or b==c or c==a:
#    print('Треугольник равнобедренный')
#else:
#    print('Треугольник разносторонний')






32#
#import random
#a,b,c=random.sample(range(1,10),3)
#print(a,b,c)
#while a>=b+c or b>=a+c or c>=b+a:
#    a,b,c=random.sample(range(1,10),3)
#    continue#
#
#print(a,b,c)
#x=c*c==a*a+b*b or b*b==c*c+a*a or a*a==c*c+b*b
#print('Треугольник прямоугольный',x)




34,35,#
#import random
#x,y=random.sample(range(1,9),2)
#x1,y1=random.sample(range(1,9),2)
#print('{x}-{y}'.format(x=x,y=y))
#print('{x1}-{y1}'.format(x1=x1,y1=y1))
#print('1-1 -- Черное')
#z=(x+y)%2==0
#z1=(x1+y1)%2==0

#q=(x+y)%2!=0
#q1=(x1+y1)%2!=0
#print('Поля одинакового цвета?', (z==True and z1==True) or (q==True and q1==True))

#print(z)
#print(z1)
#print('Клетка белая?',z)
#print('Клетка белая?',z1)






36,37,38,39,40#
import random
x1,y1,x2,y2=[random.randrange(1,9) for i in range(0,4)]
print("x1: ", x1)
print("y1: ", y1)
print("x2: ", x2)
print("y2: ", y2)
#c= x1==x2 or y1==y2
#print('Ладья может перейти в это поле за один ход? :',c)
#c= (abs(x1-x2)==1 and abs(y1-y2)==1) or (x1==x2 and abs(y1-y2)==1) or (y1==y2 and abs(x1-x2)==1 )
#print('Король за один ход может перейти с одного поля на другое? :', c)
#c= abs(x1-x2) == abs(y1-y2)
#print('Слон за один ход может перейти с одного поля на другое? :', c)
#c=(x1==x2 or y1==y2) or (abs(x1-x2) == abs(y1-y2))
#print('Ферзь за один ход может перейти с одного поля на другое? :',c)
c= (abs(x1-x2)==1 and abs(y1-y2)==2) or (abs(x1-x2)==2 and abs(y1-y2)==1)
print('Конь за один ход может перейти с одного поля на другое? :',c)
















