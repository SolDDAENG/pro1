# 제어문
# if
print('\n---------if--------------------------')
var = 10
if var >= 3:
    print('크구나')
    print('참일 때')
    if var > 5:
        print('5 초과')
else:
    print('거짓')
    
print('계속 1')

jumsu = 80
# 키보드로 값 받기
# jumsu = int(input('점수 : ')) # input은 문자형이기 때문에 casting해줘야한다.

if jumsu >= 90:
    print('우수')
elif jumsu >= 70:
    print('보통')
else:
    print('부족')
    
if 90 <= jumsu <= 100:
    res = 'a'
elif 70 <= jumsu < 90:
    res = 'b'
else:
    res = 'c'
print(res)

names = ['홍길동', '신기해', '이기자']
if '홍길동' in names:
    print('친구 이름')
else:
    print('누구야')

a = 'kbs'
b = 9 if a == 'kbs' else 11 # a가 kbs면 b = 9, 아니면 b = 11을 준다.
print(b)
a = 11
b = 'mbc' if a == 9 else 'kbs'
print(b)

print()
a = 6
re = a * 2 if a > 5 else a + 2
print(re)

a = 3
print((a + 2, a * 2)[a > 5]) # 결과가 참이면 1, 거짓이면 0. 거짓이기 때문에 3 + 2 = 5가 실행된다.


# while
print('\n---------while--------------------------')
a = 1
while a <= 5:
    print(a, end = ' ')
    a += 1
print()

colors = ['r','g','b']
a = 0
while a < len(colors):
    print(colors[a], end = ' ')
    a += 1
print()

while colors:
    print(colors.pop(), end= ' ') # pop에 0을 넣으면 r g b 로 출력된다.
print()


# 잘 되지만 키보드로 일일히 입력하기 귀찬다.
# import time   
# sw = input('폭탄 스위치를 누를까요?(y/n)')
# if sw == 'Y' or sw == 'y':
#     count = 5
#     while 1 <= count:
#         print('%d초 남았습니다.'%count)
#         time.sleep(1) # 1초동안 재운다.
#         count -= 1
#     print('폭발!!!!')
# elif sw == 'N' or sw == 'n':
#     print('작업 취소')
# else:
#     print('y 또는 n을 누르시오')

a = 0
while a < 10:
    a += 1
    if a == 5:continue
#     if a == 7:break    # 반복문이 break로 빠져나올 시 else문은 필요없다. 
    print(a)
else:
    print('while 수행')


# 난수 발생
import random
num = random.randint(1, 10) # 1~10 사이의 난수를 발생시킨다.
# print(num) 
# while True:    #무한루프에 빠트림
while 1:     #무한루프에 빠트림. 숫자 0 이외의 모든 양수값은 true. 음수는 false
    print('1~10 사이의 컴이 가진 숫자를 입력하시오')
    guess = input() # 문자열로 입력
    su = int(guess) # 숫자로 변환
    if su == num:   #난수값과 내가 입력한 숫자가 같으면 성공, 틀리면 실패
        print('성공~~'*5)
        break
    elif su < num:
        print('더 큰 수 입력')
    elif su > num:
        print('더 작은 수를 입력')
        