# Tuple : 리스트와 유사. 읽기 전용.
print('\n---------Tuple(순서o, 중복o, 수정 불가)--------------------------')
# t = ('a','b','c','a')
t = 'a','b','c','a' # 소괄호가 없어도 Tuple형이다.
print(t, ' ', t.count('a'), ' ', t.index('b')) # 순서가 있음. a = 2개 , b는 1번째에 있다.
print(t[0])
# t[0] = 'm' # 읽기 전용이기 때문에 수정 불가
q = list(t) # List형으로 형변환
q[0] = 'm' # 값 수정
t = tuple(q) # 다시 Tuple로 변환
print(t)
t1 = (1, 2)
print(t1)
a, b = t1
b, a = a, b # 순서 바꾸기
t1 = a, b
print(t1)
kk = (1) # 값이 하나일 때 이렇게 쓰면 tuple이 아니다. -> int형
kk2 = (1,) # 값이 하나일 때 ,를 사용하면 tuple형이 된다. -> tuple형
print(kk, type(kk), kk2, type(kk2)) # 1 <class 'int'> (1,) <class 'tuple'>


# Set : 순서x, 중복x, 수정가능
print('\n---------Set(순서x, 중복x)--------------------------')
a = {1,2,3,1}
print(a)
b = {3, 4}
print(a.union(b)) # 합집합
print(a.intersection(b)) # 교집합
print(a - b, a | b, a & b) # 차집합, 합집합, 교집합
# print(a[0])
b.add(5)
print(b)
b.update({6, 7})
b.update({8, 9})
b.update({10, 11})
print(b)

b.discard(7) # 값에 의한 삭제. 해당 값이 없으면 통과
b.remove(6) # 값에 의한 삭제. 해당 값이 없으면 에러
b.discard(7) # 값에 의한 삭제. 해당 값이 없으면 통과
# b.remove(6) # 값에 의한 삭제. 해당 값이 없으면 에러
print(b)
b.clear()
print(b)

# 중복제거 방법 -> set형태로 casting 후 다시 원래 형태로 casting하면 된다.
li = [1,2,1,2]
s = set(li)
li = list(s)
print(li)


# Dict : {key:value} 형태의 값을 가지고 있다.
print('\n---------Dict {key:value}--------------------------')
mydic = dict(k1=1, k2='mbc', k3=1.2)
print(mydic)
dic = {'파이썬':'뱀','자바':'커피','스프링':'용수철'}
print(dic, ' ', len(dic))
print(dic['자바']) # key를 이용한 검색 가능
# print(dic[0]) # Error : 순서를 이용한 검색 불가. 순서가 없음.

dic['오라클'] = '예언자' # 값 추가
print(dic)
del dic['오라클'] # 값 삭제
print(dic)
dic['자바'] = 'Programing Language'
print(dic)
print(dic['자바']) # 자바의 value 값 출력
print(dic.keys()) # Dict 형태의 key 값을 출력
print(dic.values()) # Dict 형태의 value 값을 출력
print(dic.get('자바')) # key '자바'의 value값 출력



