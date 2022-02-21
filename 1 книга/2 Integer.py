6,7,8#
#import random
#x=random.randrange(10,100)
#print("x = ",x)
#a=int(x/10)
#b=x%10
#print(a,b)
#print("Суума цифр числа х = ", a+b)
#print("Произведение цифр числа х = ", a*b)
#x_2=b*10+a
#print(x_2)




9,10,11,12,13#
#import random
#x=random.randrange(100,1000)
#print("x=",x)
#a=int(x/100)# 1 цифра
#print(a)
#b1=int(x/10)
#b2=int(b1%10)# 2 цифра
#print(b2)
#c=int(x%10)
#print(c)# 3 цифра
#print("Summa=",a+b2+c)
#rint("Proizvedenie=",a*b2*c)
#print("Obratnoe chislo=",c*100+b2*10+a)
#print("Levoe chislo - spravo =", b2*100+c*10+a)






17#
#import random
#x=random.randrange(1000,10000000)
#print(x)
#a=int(x%1000)# получается сотня
#print(a)
#b=int(a/100)# получается цифра нужного разряда
#rint(b)




19,21#
#import random
#sec=random.randrange(0,86401)
#sec=245
#print(sec)
#in_=int(sec/60)
#print(min_)
#chas=int(min_/60)
#print(chas)
#min_pol=(sec%60)
#print(min_pol)



24#
#import random
#k=random.randrange(1,366)
#print(k)
#print('1 января - Понедельник')

#if k%7==0:
 #   print("Воскресенье")
#elif k%7==1:
#    print('Понедельник')
#elif k%7==2:
#    print('Вторник')
#elif k%7==3:
#print('Среда')
#elif k%7==4:
#    print('Четверг')
#elif k%7==5:
#    print('Пятница')
#elif k%7==6:
#    print('Суббота')
#else:
#    print('Ошибка')




26#
#import random
#k=random.randrange(1,366)
#print(k)
#print('1 января - Вторник')

#if (k+1)%7==0:
#    print("Воскресенье")
#elif (k+1)%7==1:
#    print('Понедельник')
#elif (k+1)%7==2:
#    print('Вторник')
#elif (k+1)%7==3:
#    print('Среда')
#elif (k+1)%7==4:
#    print('Четверг')
#elif (k+1)%7==5:
    #print('Пятница')
#elif (k+1)%7==6:
#    print('Суббота')
#else:
#    print('Ошибка')





29#
#import random
#A,B,C=random.sample(range(1,10),3)
#a=print(A,B,C)
#print(a)
#if A<B or B<C:
#    while A<B or B<C:
#        A,B,C=random.sample(range(1,10),3)
#        if A<B or B<C:
#                continue



##print(A,B,C)
#S1=A*B
#print('Площадь прямоугольника:',S1)
#Z=int(S1/C)
#print("Квадратов влазиет в прямоугольник:",Z)
#S2=Z*C
#print('Квадрат со сторой С на их количество Z:',S2)
#S3=S1-S2
#print('Площадь пустго пространства:',S3)







30#
import random
n=random.randint(1,2020)
print('Год:',n)

s=int((n-1)/100)+1
print("Cтолетие:",s)

























