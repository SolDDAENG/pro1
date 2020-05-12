'''
여러 줄
주
석
'''
# 한줄 주석
from builtins import isinstance
# from sqlalchemy.sql.expression import true
var1 = '안녕'
print(var1)
var1 = 5; print(var1);
var1 = '변수 선언시 type은 저장되는 자료에 의해 결정됨'
print(var1)

a = 10
b = 20.1
c = b
print(a,b,c)
print('주소 출력 : ', id(a), id(10), id(b), id(20.1), id(c)) # 참조형이기 때문에 주소가 같다.
print(a is b, a == b) # is : 주소 비교, == : 값 비교
print(b is c, b == c)

print()
A = 1; a = 2
print(A, ' ' , a)

print()
import keyword
print('예약어 : ',keyword.kwlist) # 변수명으로 사용 할 수 없는 용어들

print('\n진법')
print(10, oct(10), hex(10), bin(10)) # 10(10진수) 0o12(8진수) 0xa(16진수) 0b1010(2진수)
print(10, 0o12, 0xa, 0b1010) # 10 10 10 10

print('\n자료형')
print(7, type(7)) # int
print(7.1, type(7.1)) # float
print(7 + 3j, type(7 + 3j)) # complex
print(True, type(True)) # bool
print('kbs', type('kbs')) # string

print((1,), type((1,))) # tuple
print([1], type([1])) # list
print({1}, type({1})) # set
print({'k':1}, type({'k':1})) # dict ( json )

a = 1
print(isinstance(a, int))
print(isinstance(a, float))


print('\n---------연산자----------------')
v1 = 2
v1 = v2 = v3 = 5
print(v1, v2, v3)
v1 = 1, 2, 3, # tuple type으로 들어간다.
print(v1) # (1, 2, 3)
v2, v3 = 10, 20
print(v2, v3) # 10 20

v1, v2 = 10, 20
v2, v1 = v1, v2 # 값 교환도 가능하다.
print(v1, v2) # 20 10

print('\n----------packing------------')
# v1, *v2 = [1, 2, 3, 4, 5] # *을 가진애는 대량을(집합형), *이 없으면 한 개 가져간다.
*v1, v2 = 1, 2, 3, 4, 5 # *을 가진애는 대량을(집합형), *이 없으면 한 개 가져간다.
print(v1)
print(v2)
*v1, v2, v3 = 1, 2, 3, 4, 5
print(v1)
print(v2)
print(v3)


print('\n------------연산자--------------')
print(5 + 3, 5 - 3, 5 * 3)
print(5 / 3, 5 // 3, 5 % 3, 5 ** 3) # 나누기, 몫, 나머지, 거듭제곱(5의 3승)
print(divmod(5, 3)) # 몫과 나머지를 tuple type으로 담는다.
print()
print(3 + 4 * 5, (3+4)*5) # 연산자 우선순위

print('\n관계연산 : ', end = ' ') # end를 만나면 라인스킵이 없다.
print(5 > 3, 5 == 3, 5 != 3)

print('\n논리연산 : ', end = '===> ') # end를 만나면 라인스킵이 없다.
print(5 > 3 and 4 <= 3, not(5 >= 3))

print('\n문자열 더하기 : ', end = ' ')
print('한' + '국' + '만세')
print('한국'*20)

print('\n누적')
a = 10
a = a + 1
a += 1 # ++    --  X 증감연산자 불가
print(a)
print(a * -1, -a, --a) # -12 -12 12(음수의 음수는 양수)

print('\nbool 처리 : ',bool(0), bool(1), bool(True), bool(False))
print('bool 처리 : ',bool(100), bool(-10), bool(None), bool(''), bool([]), bool({})) # 0이외의 숫자는 전부 true, 0이거나 값이 없으면 false

print()
print('kbs\tbs') # kbs    bs
print('kbs\nbs') # kbs \n bs
print(r'kbs\tbs') # r을 붙이면 이스케이프 문자를 무시한다. 일반 문자열 처리. kbs\tbs
print(r'kbs\nbs') # r을 붙이면 이스케이프 문자를 무시한다. 일반 문자열 처리. kbs\nbs


print('\n\n2020-05-07----------------------------------------')
print('*'* 20)
print(format(1.2345,'10.3f'))
print('나이가 %d입니다.'%22) # %d 숫자열
print('나이가 %s입니다.'%'스물') # %s 문자형
print('나이가 %d입니다.%s'%(22,'스물')) # 집합형
print('나이가 %s입니다.%s %f'%(22,'스물',22.5)) # 집합형

print('이름은 {} 나이는 {}'.format('하하',33))  # 0번째와 1번째가 생략되어있다. 안적어주면 순서대로 출력한다.
print('이름은 {0} 나이는 {1}'.format('하하',33)) # 이름은 하하 나이는 33
print('이름은 {1} 나이는 {0}'.format('하하',33)) # 이름은 33 나이는 하하
print('이름은 {1} 나이는 {0} {1} {1}'.format('하하',33)) # 여러번 출력할 수 있다.
