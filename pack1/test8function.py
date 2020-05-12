# 함수 계속
# 인수 키워드 매핑

def ShowGugu(start, end = 5):
    for dan in range(start, end + 1):
        print(str(dan) + '단 출력')
        
ShowGugu(2, 3)
print()
ShowGugu(3) # end에 값을 주지 않으면 초기값 5 유지
print()
ShowGugu(start=2, end=4) # argument의 이름에 값을 직접 줄 수 있다.
print()
ShowGugu(end=4, start=3) # argument 이름에 매핑하기 때문에 순서가 바뀌어도 인식한다.
print()

print('\n------------가번 인수--------------')
def func1(*ar): # argument가 tuple타입으로 얼마든지 받아들인다. 인수의 개수가 부정확 할 때 *을 입력한다.
    print(ar) # Tuple형이기 때문에 순서가 있다.
    for i in ar:
        print('음식 : ' + i)
    
func1('비빕밥','공기밥','주먹밥') 

print()
def func2(a, *ar): # argument가 tuple타입으로 얼마든지 받아들인다. 인수의 개수가 부정확 할 때 *을 입력한다.
    print(a) # 가장 첫 번째 값인 비빔밥을 제외하고 *ar에 값이 들어간다.
    print(ar)
    for i in ar:
        print('음식 : ' + i)
    
func2('비빕밥','공기밥','주먹밥') 

print()
def func3(a, b, *v1, **v2): # *v1 : tuple, **v2 : dict
    print(a, b) # 가장 첫 번째 값인 비빔밥을 제외하고 *ar에 값이 들어간다.
    print(v1)
    print(v2)
    
func3(1, 2) 
print()
func3(1, 2, 3, 4, 5) # 1과 2는 a, b가 받고 나머지는 *v1인 tuple이 받는다.  
print()
func3(1, 2, 3, 4, 5, m=6, n=7) # 1과 2는 a, b가 받고 나머지는 *v1인 tuple이 받는다. 그리고 key:value값은 **v2가 dict타입으로 받는다.
print()

print('-------closure(클로저) x ---------------------------------')
# closure (클로저) x
def out():
    count = 0
    def inn():
        nonlocal count
        count += 1
        return count
    print(inn())

out()
out()

print('-------closure(클로저) o ---------------------------------')
# closure (클로저) o
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner # 함수의 주소를 리턴. 이것이 클로저

add1 = outer() # add1은 inner func의 주소를 가지고 있다. outer 함수 밖에서 참조 가능. 클로저를 이용해서 OOP의 흉내를 낼 수 있다.
print(add1())
print(add1())
print(add1())

# add1와 add2객체의 타입은 같지만 다른 객체다. 그래서 같은 주소의 inner함수를 가지고 있어도 새로 시작한다.
add2 = outer()
print(add2())
print(add2())

print('수량 * 단가 * 세금 결과 출력 -----------------')
def outer2(tax):
    def inner2(su, dan):
        amount = su * dan * tax
        return amount
    return inner2 # 클로저 : 내부함수의 주소를 리턴. 함수 밖에서 함수 내부의 주소를 참조해서 사용하기 위함. 클로저는 함수 하나로 사용할 수 없다. 두개 이상의 함수가 필요. 

a1 = outer2(0.1)
# print(id(a1))
result1 = a1(5, 1000)
print(result1)
result2 = a1(10, 35000)
print(result2)

print()
a2 = outer2(0.05) # tax = 0.05
result3 = a2(5, 1000)
print(result3)

print('=======일급함수(함수 안에 함수, 인자로 함수 전달, 반환값이 함수)======================')
def fun1(a, b):
    return a + b
fun2 = fun1 # 함수의 주소를 전달
print(fun2(3, 4))

print()
def fun3(func):
    def fun4(): # 함수안에 함수
        print('난 내부함수 fun4~~~~~')
    fun4()
    return func # 반환값이 함수
mbc = fun3(fun1) # 인자로 함수 전달 - 일급함수 만족
print(mbc(3,4)) # 결과적으로 fun1을 실행함.

print('\n------------lambda 함수 : 함수의 길이를 줄이는데 혁신적인 역활을 함------------------')
def Hap(x, y):
    return x + y

print(Hap(1, 2))

print((lambda x, y : x + y)(1, 2)) # 함수 Hap의 해당하는 내용을 lambda로 줄여쓴 것이다. js의 -> 랑 비슷하다.

aa = lambda x, y : x + y # lambda : 이름이 없는 함수. 결과값 a + b 리턴
print(aa(1, 2))
print(aa(3, 4))

kbs = lambda a, su = 10: a + su
print(kbs(5))
print(kbs(5, 6))

sbs = lambda a, *tu, **di:print(a, tu, di)
sbs(1,2,3, m=4, n=5)

li = [lambda a, b: a + b, lambda a, b: a * b] # list의 argument로 lambda함수를 줄 수 있다.
print(li[0](3, 4)) # 3 + 4 = 7
print(li[1](3, 4)) # 3 * 4 = 12

# 다른 함수에서 람다 사용
print(list(filter(lambda a:a<5, range(10)))) # filter라는 내장함수에서 lambda 사용. filter : true일때만 실행. 
print(list(filter(lambda a:a % 2, range(10)))) # filter : true일때만 실행. 나머지가 0이면 false, 1이면 true : 홀수만 찍힘.

# decorator : 함수 장식자
print('\n----함수 장식자(decorator)-----------------') 
def make2(fn):  #argument로 함수를 가지고 람다를 리턴
    return lambda:'안녕 ' + fn()   # 함수 fn()에 람다 '안녕'을 붙여서 리턴. 여기서 fn()은 make1

def make1(fn):  #argument로 함수를 가지고 람다를 리턴. 여기서 fn()은 hello
    return lambda:'반가워 ' + fn() 

def hello():
    return '홍길동'

hi = make2(make1(hello))
print(hi()) # 안녕 반가워 홍길동

print()
# 함수 장식자(decorator) 사용
@make2
@make1
def hello2():
    return '신기해'
print(hello2()) # h1()랑 똑같다.

print('\n-----------')
hi2 = hello2() # hello2의 실행 결과를 넘김
print(hi2)
hi3 = hello2 # hello2의 주소를 넘김
print(hi3()) # 함수의 주소를 가졌기 때문에 함수로 실행을 해야한다.

print('----재귀 함수(함수 자신을 호출 : 반복처리 효과적)----------------')
def CountDown(n):
    if n == 0:
        print('완료')
    else:
        print(n, end = ' ')
        CountDown(n -1) # <===

CountDown(5)

print()
def tot(n):
    if n == 1:
        print('1일때 탈출')
        return 1
    return n + tot(n - 1)
result = tot(10)
print('합 : '+str(result))

print() # 5!을 구해보자
def fact(a):
    if a == 1: return 1
    print(a)
    return a * fact(a - 1)

result2 = fact(5)
print('5! : ' + str(result2))
print(5 * 4 * 3 * 2 * 1)






