# 함수 : 실행단위
# 내장 함수
print('------내장 함수--------------------------')
print(sum([3,5,7]))
print(int(1.7), float(4), str(5) + '오')
print(round(1.2), round(1.6)) # 반올림

import math
print(math.ceil(1.2), math.ceil(1.6)) # 정수 근사치 중 큰 수
print(math.floor(1.2), math.floor(1.6)) # 정수 근사치 중 작은 수

x = [10,20,30]
y = ['a','b']
for i in zip(x, y):
    print(i)

# ....많고 많은 내장함수가 있다.


print('------사용자 정의 함수--------------------------')
# 사용자 정의 함수
def DoFunc1():
    print('DoFunc1')
    
DoFunc1()
print(DoFunc1())
kbs = DoFunc1 # 함수 객체의 주소를 치환. 
kbs()

print()
def DoFunc2(a, b):
    print('DoFunc21')
    result = DoFunc3(a, b)
    return result

def DoFunc3(m, n):
    imsi = m + n # 숫자의 더하기도 문자의 더하기도 된다.
    return imsi

mbc = DoFunc2
print(mbc(5, 6))
print(mbc('대한','민국'))

print('현재 사용 중인 객체 목록 : ', globals()) # 현재 사용중인 객체 전부 출력

print()
def isOdd(arg):
    return arg % 2 == 1 # 홀수 값 처리

myDict = {x:x * x for x in range(11) if isOdd(x)}   # 11이전까지의 숫자중 홀수만 x:x*x 본인 스스로 곱한 값을 출력
print(myDict)


print('\n--------------------전역, 지역 변수------------------------')
# 전역, 지역 변수
player = '전국대표' #전역 변수(global). 모듈의 멤버 

def FuncSoccer():
    name = '홍길동'    # 지역(local) 변수
    player = '지역대표' # 지역(local) 변수
    print(name, player)

FuncSoccer()    # 지역이 우선이기 때문에 지역대표가 출력된다.
print(player)
#print(name) # 지역변수이기 때문에 호출 불가능

print()
a = 10; b = 20; c = 30
print('1) a : ', a, ', b : ', b, ', c : ', c)

def Good(): # 함수의 이름은 소문자로 해도 되고 대문자로 해도 상관없다.
    # pass # 함수에 쓸 내용이 없을 시 그냥 패스할 수 있다.
    a = 40
    b = 50
    print('2) a : ', a, ', b : ', b, ', c : ', c)
    def Nice():
        #c = 60
        global c # 전역 변수가 된다. 이 뒤에 선언되는 c가 전역변수로 쓰인다.
        nonlocal b # 부모함수의 멤버로 선언. 지금은 good함수 내부에서 지역변수로 선언한 것이다.
        print('3) a : ', a, ', b : ', b, ', c : ', c)
        c = 60 # Error: local variable 'c' referenced before assignment. 이 변수는 전역변수에 값을 주는 것이다.
        b = 70
    Nice()
    print('4) a : ', a, ', b : ', b, ', c : ', c)
    
Good()
print('n) a : ', a, ', b : ', b, ', c : ', c)














