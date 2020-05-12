# for target in object: ~

print('\n---------for--------------------------')
for i in [1,2,3,4,5]:
    print(i, end = ' ')

print()
# colors = {'r','g','b'} # List형이건 Tuple형이건 Set형이건 상관없다. 다만 set형태일 경우 순서가 없기 때문에 다르게 나올 수 있다.
colors = ('r','g','b') # 순서가 있다.
for c in colors:
    print(c, end = ' ')

print()
soft = {'java':'웹용언어','python':'접착언어','c':'시스템 개발용'}
for i in soft.items():
    #print(i) # dict 타입
    print(i[0], ' ', i[1])

print()
for k, v in soft.items(): # key와 value를 따로 찍을 수 도 있다.
    print(k, ' ', v)

print()
for k in soft.keys(): # key와 value를 따로 찍을 수 도 있다.
    print(k)
    
print()
for v in soft.values(): # key와 value를 따로 찍을 수 도 있다.
    print(v)
    
print()
for n in [2,3]:
    print('--{}단'.format(n))
    for i in [1,2,3,4,5,6,7,8,9]:
        print('{0}*{1}={2}'.format(n, i, n*i))
        
print()
li = ['a', 'b', 'c']
for index, data in enumerate(li): # 내장함수 - index값도 얻을 수 있다.
    print(index, ' ', data)

print()
datas = [1,2,3,4,5]
for i in datas:
    if i == 3:
        continue
        #break
    print(i, end = ' ')
else:
    print('정상 종료일 때 처리 - break만나지 않음')
    
print('\n---------문자열 검색 후 단어 수 출력--------------------------')
import re
ss = '''
생활 속 거리 두기 첫날인 6일 신종 코로나바이러스 감염증(코로나19) 확진 환자가 4명 늘어 총 1만810명이 됐다. 
최근 3일간 없었던 지역사회 감염 환자가 나흘 만에 나왔다.
질병관리본부 중앙방역대책본부(방대본)는 7일 오전 0시 기준 국내 코로나19 누적 확진자가 1만810명이라고 밝혔다. 
확진자 가운데 사망자는 1명 늘어 총 256명, 격리 해제된 완치자는 86명 증가한 총 9419명이다.
확진자 가운데 확진자 가운데 확진자 생활 속 생활 속 생활 속 생활 속 
''' # '''는 주석이 될 수도 있고 문자열이 될 수도 있다.    

print(ss)
ss2 = re.sub(r'[^가-힣\s]', '', ss)   # 한글을 제외한 나머지 것은 공백처리한다.
print(ss2)
ss3 = ss2.split(' ') # 공백을 기준으로 자름
print(ss3)    
print(len(ss3)) # 아직 중복 있음. 
setdata = set(ss3)
print(len(setdata)) # 중복이 제거됨.

cou = {}    # 단어의 발생 횟수를 dict type으로 저장
for i in ss3:
    if i in cou:
        cou[i] += 1
    else:
        cou[i] = 1
print(cou)        

print('\n----dict 자료로 과일값 출력 ----')
price = {'사과':500, '수박':12000, '참외':600}
my = {'사과':2, '수박':1}
bill = sum(price[f] * my[f] for f in my)    # price에 해당하는 개수를 my에서 뽑아낸다. 
print('총 구매 가격 : {}'.format(bill))

print()
datas = [1,2,'a',True, 3]
li = [i * i for i in datas if type(i) == int]   # type이 int인 애들만 수행
print(li) 

datas = {1,1,2,2,3} # set형태라 자동으로 중복제거 되어서 {1, 2, 3} 만 남는다.
se = {i * i for i in datas}
print(se)

id_name = {1:'tom', 2:'james'}
name_id = {val:key for key,val in id_name.items()}
print(name_id)

print()
temp = [1,2,3]
for i in temp:
    print(i, end = ' ')
print()
print([i for i in temp])
print({i for i in temp})
# print((i for i in temp))

temp2 = list()
for i in temp:
    temp2.append(i)
print(temp2)

temp3 = [i + 10 for i in temp]
print(temp3)

print()
aa = [(1,2),(3,4),(5,6)]
for a, b in aa:
    print(a + b)

print('--------------------')
print(list(range(1, 6))) # 1부터 6이전까지 list형 수열 
print(tuple(range(1,6))) # 1부터 6이전까지 tuple형 수열
print(set(range(1,6)))   # 1부터 6이전까지 set형 수열

for i in range(6):
    print(i, end = ' ') # 0부터 6이전까지의 수열

print()
for i in range(2, 10):
    for j in range(1, 10):
        print('{}*{}={}'.format(i, j, i*j), end = ' ')
    print()

print()











