
1,2#
#import random
#B,A=sorted(random.sample(range(1,15),2))
#print('B=',B)
#print('A=',A)

#C = A - B
#i = 1
#while C >= B:
#    C -= B
#    i += 1

#print('Незанятая длинна отрезка А:',C)
#print('Количество отрезков В, размещенных на А:',i)



3#
#import random
#K,N = sorted(random.sample(range(1,10),2))
##while N%K!=0:
 #   K,N = random.sample(range(1,10),2)
 #   continue

#print('N=',N)
#print('K=',K)

#R = N - K
#i = 1
#while R - K >= 0:
#    R -= K
#    i += 1
#print('Деление нацело равно:',i)
#print('Остаток от деления:',R)




4,5#
#import random
#N=random.randint(1,100)
#N=64
#print('N=',N)
#i=0
#while N>=3:
#    N/=3
#    print(N)
#print(N==1)

#L=math.log(2,N)
#print(L)

#while N>=2:
#    N/=2
#    i+=1
#    print(N)

#if N==1:
 #   print(i)





7#
#import random
#N=random.randint(1,10)
#print('N=',N)
#K=1

#while K*K<=N:
#    K+=1
#    print(K,':',K*K)
#print(K*K,">",N)



9#
#import random
#N=random.randint(2,10)
#print('N=',N)
#K=0
#while 3**K <= N:
#    K+=1
#    print(3**K,':',N)





11,12#
#import random
#N = random.randint(2,10)
#print('N=',N)
#K = 0
#S = 0
#while S < N:
 #   K += 1
  #  S += K
   # print(f"Количество элементов K = {K},\n Сумма S = {S}")

#print("\n K = {0}, S = {1}".format(K,S))


#while S <= N:
#    K += 1
#    S += K
#    print(f"Количество элементов K = {K},\n Сумма S = {S}")

#if S > N:
#    S -= K
#    K -= 1

#print("\n K = {0}, S = {1}".format(K,S))






13#
'''
import random
A = random.randint(2,100)
print(' A = ',A)
K = 1
S = 0
while S <= A:
    X = 1 / K
    S += X
    print(f' Иттерация: {K} \n Часть суммы: {X} \n Сумма данной иттерации: {S} \n')
    K += 1
print('Итоговая сумма:',S)
'''



15#
'''
import random
procent = random.randint(1,25)
print('% = ',procent)
start_sum = 1000
end_sum = 1100
month = 0
while start_sum < end_sum:
    one_procent = start_sum / 100
    procent_in_money = procent * one_procent
    start_sum += procent_in_money
    month += 1
    print(f'Месяцы = {month}, Сумма = {start_sum}')

print(f'\nЗа {month} месяцев вклад превысит {end_sum} \n')
print('Итоговая сумма =', start_sum)
'''

16#
'''
import random
procent = random.randint(1,50)
procent=22
print('% = ',procent)
start_km = 10
sum_km = start_km
end_km = 200
day = 1
while sum_km < end_km:
    one_procent = sum_km / 100
    procent_in_km = procent * one_procent
    sum_km += procent_in_km + start_km
    day += 1
    print(f'Days = {day}, Final_km = {sum_km}')

print(f'\nЗа {day} дней лыжник превысит {end_km} \n')
print('Итоговая сумма =', sum_km)
'''


'''
17,18,19,20,21#
import random
N = random.randint(1,200)
print('N = ',N)

q = N
S = 0
i=0

#while q >= 1:
 #  r = q % 10
  # print(r)
   #q = int(q / 10)

#while q >= 1:
 #   i += 1
  #  r = q % 10
   # S += r
   # print('Цифра :', r , 'Cумма :', S)
   # q = int(q / 10)
#print('Количество цифр:',i ,'Итоговая сумма:',S)



#while q >= 1:
#    r = q % 10
#    print('Цифра :', r )
#    q = int(q / 10)
#    S = S * 10 + r
#print('Инверсионное число:',S)


#while q >= 1:
#    r = q % 10
#    print(r)
#    if r == 2:
#        S = True
 #       break
  #  else:
   #     q = int(q / 10)
    #    S = False


#print(S)



while N >= 1:
    r = N % 10
    print(r)
    if r % 2 == 0:
        S = True
        break
    else:
         N = int(N / 10)
         S = False

print(S)
'''





22#
'''
import random, math
N = random.randint(2,100)
print('N = ',N)
while N > 1:
    if N == 2 or N == 3 or N == 5 or N == 7:
        print(True)
        break
    elif N % 2 == 0 or N % 3 == 0 or  N % 4 == 0 or N % 5 == 0 or N % 6 == 0 or N % 7 == 0 or N % 8 == 0 or N % 9 == 0:
        print(False)
        break
    else:
        print(True)
        break

#Или


N = 100
print("N = ",N)
L = []
for x in range(2,N+1):
    n = math.sqrt(x)
    i = 2
    k = 0
    while i <= n:
        if int(x / i)*i == x:
            k += 1
            break
        i += 1
    if k == 0:
        L.append(x)
print(L)
'''




'''
23#
import random
A,B = random.sample(range(0,1000),2)

print('A = ',A)
print('B = ',B)

if B != 0:
    while B > 0:
        A,B = B,A % B
    print('НОД:',A)
else:
    print('B = 0, Нод отсутствует')

'''
'''
24,25,26#
import random
N = random.randint(2,200)
K = random.randint(2,100)
K = 300
print('N = ',N)
print('K = ',K)
F1 = 1
F2 = 2
Fk = 0
Fb = []

while Fk < K:
    Fk = F1 + F2
    F1 = F2
    F2 = Fk
    print(Fk)
    Fb.append(Fk)



    if N == Fk or N == 1 or N ==2:
        print(True)
        break
    else:
       print(False)


    if Fk > N:
        print('Fk > N:',Fk)
        break


    if N == Fk:
        print('Fk+1:',Fk+F2)
        print('Fk-1:',Fk-F1)

print(Fb)

26,27#Сделать реально, но нужно переделывать код, но я бы смог!
'''


28,29#
'''
import random
E = random.uniform(0,0.00000001)
print('E = ',E)


A1 = 2
print(1,":",A1)
Ak = 2 + 1/A1
i = 2
print(2,":",Ak)

while  abs(Ak - A1) >= E:
    A1 = Ak
    Ak = 2 + 1 / A1
    i += 1
    print(i, ';', Ak)
print(abs(Ak - A1))
print(i,":",A1,":",Ak)


A1 = 1
print(1,":",A1)
A2 = 2
print(2,":",A2)
A3 = (A1 + 2 * A2) / 3
print(3,":",A3)
i = 3

while abs(A3 - A2) >= E:
    A1 = A2
    A2 = A3
    A3 = (A1 + 2 * A2) / 3
    i += 1
    print(i , ';' ,A3)
print()
print(abs(A3 - A2))
print()
print(i,":",A2,":",A3)
'''



30#
import random
A,B,C =sorted(random.sample(range(1,20),3),reverse=True) #Запомнить этот пример с обратной сортировкой.
print('A = ',A)
print('B = ',B)
print('C = ',C)

Sp = A * B
Sk = C * C
print('Площадь прямоугольника:',Sp)
print('Площадь квадрата:',Sk)
k = 0
while Sp - Sk >= 0:
    k += 1
    Sp -= Sk
    print(k, ';', Sp)
print(f'{k} квадратов влезет в прямоугольник')



