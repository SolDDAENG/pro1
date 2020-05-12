# 집합 자료형 : String, List, Tuple, Set, Dict

# String : 문자열 취급 (순서형), 변경 불가
print('\n---------String : 문자열 취급 (순서형), 변경 불가--------------------------')
s = 'sequence'
print(len(s))
print(s.count('e'))
print(s.find('e'), ' ', s.find('e', 3), s.rfind('e'))
print(s.startswith('s')) # s로 시작하면 true, 아니면 false

ss = 'mbc'
print('mbc', id(ss))
    # ss가 mbc의 주소를 가지고 있었지만 abc의 주소를 가지게 되면서 mbc가 사라진다. 
ss = 'abc'
print('abc', id(ss))

# 슬라이싱
print(s[0], ' ', s[2:4], ' ', s[:3], ' ', s[3:]) # 0번째, 2~4번째, 처음부터 3까지 출력, 3이후부터 출력
print(s[-1], ' ', s[-4:-1], ' ', s[-4:], ' ', s[::2]) # -를 붙이면 뒤에서부터, ::2 하나걸러 하나씩 출력
# s[0] = 'k' # Error : String은 변결할 수 없다. 

ss = 'kbs mbc'
ss2 = ss.split(sep=' ') # 공백을 기준으로 자르기
print(ss2)
print(','.join(ss2)) # ,를 기준으로 합친다.

# List : 배열과 유사, 순서 있음, 변경가능, 여러 종류의 자료 허용.
print('\n---------List : 배열과 유사, 순서 있음, 변경가능, 여러 종류의 자료 허용--------------------------')
a = [1, 2, 3] # 객체변수
b = [10, a, 12.3, True, 'kbs'] # 객체변수를 호출 할 때는 대괄호[]를 둘려준다.
print(a, ' ', id(a))
print(b, ' ', id(b))

print(b[0], ' ', b[1], ' ', b[1][:2]) # List는 중첩도 가능하다. 결과 : 10   [1, 2, 3]   [1, 2] 
b[0] = 'mbc' # List형이라 수정 가능. -> 삭제도 가능하다.
print(b[0]) # mbc 
b.remove('kbs') # .remove : 값에 의한 삭제
print(b)
del b[3]    # del : 순서에 의한 삭제
print(b)
print()
family = ['엄마', '아빠', '나']
family.append('동생') # List의 값 추가 - 맨 뒤로 들어감
family.remove('나')  # List의 값 삭제
family.insert(0,'할아버지') # 임의의 지점에 값 추가 - 0번째 지정
family.extend(['삼촌', '고모', '이모']) # extend : 다중 값 추가
family += ['아주머니', '아저씨'] # += 사용해서 다중 값 추가
print(family, len(family), family[0])
print()
li = [[0,1,2],[3,4,5]]
print(li[0])
print(li[0][0])
print()
name = ['tom', 'james', 'oscar']
name2 = name # 주소 치환해서 같은 값의 주소를 가지고 있다. name의 값이 바뀌면 name2도 바뀐다. 
print(name, ' ', name2)
name[0] = 'sujan'
name2[1] = 'jhon'
print(name, ' ', name2)

import copy
name3 = copy.deepcopy(name) # 새로운 객체의 주소를 기억. 주소가 다르다.
print(name, ' ', name3)
name[0] = '길동'
print(name, ' ', name3)

print('\nstack과 queue------------------------') 
sbs = [1,2,3]
sbs.append(4)
print(sbs)
sbs.pop() # FILO : 마지막에 들어온것을 꺼낸다.
print(sbs)
sbs.pop()
print(sbs)
print()
sbs = [1,2,3]
sbs.append(4)
print(sbs)
sbs.pop(0) # 처음에 들어온것을 꺼낸다. FIFO(First In First Out)
print(sbs)
sbs.pop(0)
print(sbs)
print()




















