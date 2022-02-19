1#
#import random
#x=str(random.randint(1,8))
#print('x=',x)
#week_days={
#'1': 'понедельник',
#'2': 'вторник',
#'3': 'среда',
#'4': 'четверг',
##'5': 'пятница',
#'6': 'суббота',
#'7': 'воскресенье'
#}
#print(week_days[x])







5# Там где есть вычисления, лучше задействовать If and ELSE
#import random
#x=str(random.randint(1,4))
#A,B=[random.randint(-10,10) for i in range(0,2)]

#print("1 — сложение, 2 — вычитание, 3 — умножение, 4 — деление")
#
#print('x=',x)
#print('A=',A)
#print('B=',B)

#if B!=0:
 #   Operation={
  #      '1': A+B,
   #     '2': A-B,
    #    '3': A*B,
     #   '4': A/B
    #}
    #print(Operation[x])
#else:
 #   print('B=0, операция деления невозможна')




6#
#import random
#x=random.randint(1,5)
#AB=random.randint(1,100)
#print("1 — дециметр, 2 — километр, 3 — метр, 4 — миллиметр, 5 — сантиметр")
#print("Номер единицы длины: ", x)

#if x==1:
#    print('Дм:',AB)
#    print('М:',AB/10)
#elif x==2:
#    print('Kм:',AB)
#    print('М:',AB*1000)
#elif x==3:
#    print('М:',AB)
#elif x==4:
#    print('Мм:',AB)
#    print('М:',AB/1000)
#else:
#    print('Cм:',AB)
#    print('М:',AB/100)




8#
#import random
#M = random.randint(1,12)
#month = {
#    1: 31,
 #   2: 28,
  #  3: 31,
   # 4: 30,
    #5: 31,
    #6: 30,
    #7: 31,
    #8: 31,
    #9: 30,
    #10: 31,
    #11: 30,
    #12: 31
#}

#d_max=month[M]
#D=random.randint(1,d_max)
#D=1
#print('Date:')
#print('Month {0}. Day {1}'.format(M,D) )

#if D>1:
#    D=D-1
#else:
#    if  M==1:
 #       M=12
  #  else:
   #     M=M-1
    #D=month[M]
#print('Last date:')
#print('Month {0}. Day {1}'.format(M,D))





10#
#import random
#C=random.randint(1,4)
#print('1-Север, 2-Запад, 3-Юг, 4-Восток')
#N=random.randint(-1,1)
#print('-1 - Поворот направо, 0 - Продолжать движение, 1 - Поворот налево')


#side_of_light={
 #   1:'Cевер',
 #   2:'Запад',
 #   3:'Юг',
 #   4:'Bосток'
#}
#print('Первоначальное напрвление:',side_of_light[C])

#direction_of_movement={
#    -1:'Поворот направо',
#     0:'Продолжать движение',
#     1:'Поворот налево'
#}
#print('Команда:',direction_of_movement[N])





#if C==1 and N==-1:
#    print('Новое направление: Восток')
#elif C==1 and N==0:
#    print('Новое направление: Север')
#elif C==1 and N==1:
#    print('Новое направление: Запад')


##if C==2 and N==-1:
  #  print('Новое направление: Cевер')
#elif C==2 and N==0:
#    print('Новое направление: Запад')
#elif C==2 and N==1:
#    print('Новое направление: Юг')


#if C==3 and N==-1:
#    print('Новое направление: Запад')
#elif C==3 and N==0:
#    print('Новое направление: Юг')
#elif C==3 and N==1:
#    print('Новое направление: Восток')

#if C==4 and N==-1:)
#    print('Новое направление: Юг')
#elif C==4 and N==0:
 #   print('Новое направление: Восток')
#elif C==4 and N==1:
 #   print('Новое направление: Север')







12#
#import random
#import math
#from math import pi
#N=random.randint(1,4)
#S = {1 : "радиус R",
 #    2 : "диаметр D",
  #   3 : "длина L",
   #  4 : "площадь круга S"
#}
#print(S[N])

#if N==1:
#   R=random.randint(1,10)
#   print('R=',R)
#   print('D=',2*R)
#   print('L=',2*pi*R)
#   print('S=',pi*R*R)

#elif N==2:
 #   D=random.randint(1,10)
  #  print('D=',D)
  #  print('R=',D/2)
  # print('L=',2*pi*D/2)
  # print('S=',pi*D*D/4)

#elif N==3:
 #   L=random.randint(1,10)
  #  print('L=',L)
  #  print('R=',L/(2*pi))
 #   print('D=',2*L/(2*pi))
   # print('S=',pi*L/(2*pi)*L/(2*pi))

#else:
 #   S=random.randint(1,10)
 #   print('S=',S)
 #   print('R=',math.sqrt(S/pi))
 #   print('D=',2*math.sqrt(S/pi))
 #   print('L=',2*pi*math.sqrt(S/pi))





15#
#import random
#N=random.randint(6,14)# Достоинство карты
#M=random.randint(1,4)# Масть карты
#print(N,M)
#Mast={
 #   1:'Пик',
  #  2:"Треф",
   # 3:"Бубен",
    #4:"Червей"
#}


#D={
#    6 : 'шестерка',
#    7 : 'семерка',
#    8 : 'восьмерка',
#    9 : 'девятка',
#    10 : 'десятка',
#    11 : 'валет',
#    12 : 'дама',
#    13 : 'король',
#    14 : 'туз'
#}
#print(D[N])
#print(Mast[M])





16#
#import random
#g=random.randint(20,69)
#if g==20 or (g>=25 and g<=30):
#    print('{g} лет'.format(g=g))
#elif (g>=35 and g<=40):
#    print('{g} лет'.format(g=g))
#elif (g>=45 and g<=50):
#    print('{g} лет'.format(g=g))
#elif (g>=55 and g<=60):
#    print('{g} лет'.format(g=g))
#elif (g>=65 and g<=69):
#    print('{g} лет'.format(g=g))
#
#if g==21 or g==31 or g==41 or g==51 or g==61:
#   print('{g} год'.format(g=g))#

#if g>=22 and g<=24:
 #   print('{g} года'.format(g=g))
#elif g>=32 and g<=34:
#    print('{g} года'.format(g=g))
#elif g>=42 and g<=44:
#    print('{g} года'.format(g=g))
#elif g>=52 and g<=54:
#    print('{g} года'.format(g=g))
#elif g>=62 and g<=64:
#    print('{g} года'.format(g=g))




17#
#import random

#dcat = {
 #   11 : 'одиннадцать',
 #   12 : 'двенадцать',
 #   13 : 'тринадцать',
 #  14 : 'четырнадцать',
  #  15 : 'пятнадцать',
  #  16 : 'шестнадцать',
  #  17 : 'семнадцать',
  #  18 : 'восемнадцать',
  #  19 : 'девятнадцать',
#}

#desyatki = {
#    10 : 'десять',
#    20 : 'двадцать',
##    30 : 'тридцать',
  #  40 : 'сорок'
#}

#edinici  = {
#    1 : 'одно учебное задание',
#    2 : 'два учебных задания',
#    3 : 'три учебных задания',
#    4 : 'четыре учебных задания',
#    5 : 'пять учебных заданий',
#    6 : 'шесть учебных заданий',
#    7 : 'семь учебных заданий',
#    8 : 'восемь учебных заданий',
#    9 : 'девять учебных заданий'
#}

#n=random.randint(10,40)
#print("n = ",n)
#if 10 < n and n < 20:
#    print("{0} учебных заданий".format(dcat[n]))
#else:
 #   r = n%10
  #  print("r = ",r)
   # if r == 0:
    #    print("{0} учебных заданий".format(desyatki[n]))
    #else:
    #    q = int(n/10)*10
    #    print("q = ",q)
    #    print("{0} {1}".format(desyatki[q], edinici[r]))







18#
import random

edinici  = {
    1 : 'один',
    2 : 'два',
    3 : 'три',
    4 : 'четыре',
    5 : 'пять',
    6 : 'шесть',
    7 : 'семь',
    8 : 'восемь',
    9 : 'девять'
}

dcat = {
    11 : 'одиннадцать',
    12 : 'двенадцать',
    13 : 'тринадцать',
    14 : 'четырнадцать',
    15 : 'пятнадцать',
    16 : 'шестнадцать',
    17 : 'семнадцать',
    18 : 'восемнадцать',
    19 : 'девятнадцать',
}

desyatki = {
    10 : 'десять',
    20 : 'двадцать',
    30 : 'тридцать',
    40 : 'сорок',
    50 : 'пятьдесят',
    60 : 'шестьдесят',
    70 : 'семьдесят',
    80 : 'восемьдесят',
    90 : 'девяносто',
}

sotni = {
    100 : 'сто',
    200 : 'двести',
    300 : 'триста',
    400 : 'четыреста',
    500 : 'пятьсот',
    600 : 'шестьсот',
    700 : 'семьсот',
    800 : 'восемьсот',
    900 : 'девятьсот',
}
N = random.randrange(100,999)
propis = ''
print("N = ",N)
q = int(N/100)*100
propis += sotni[q]
N -= q
if 10 < N and N < 20:
    propis += ' ' + dcat[N]
else:
    r = N%10
    q = int(N/10)*10
    if q !=0:
        propis += ' ' + desyatki[q]
    if r != 0:
        propis += ' ' + edinici[r]
    print(propis)















