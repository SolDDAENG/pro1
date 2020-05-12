# 정규표현식
import re # 정규표현식 import

ss = '1234 abc 가나다ABC_555_6 a b'
print(ss)
print(re.findall(r'123', ss)) # pattern을 입력할 때 r을 절대 빼먹지 말자
print(re.findall(r'[0-9]', ss)) # 0~9까지 
print(re.findall(r'\d', ss)) # 위와 같다

print(re.findall(r'[0-9]+', ss)) # + : 1회 이상, ? : 0또는 1, * : 0회 이상
print(re.findall(r'[0-9]{2}', ss)) # 0~9까지 숫자중 2개씩
print(re.findall(r'\d{2}', ss)) # 위와 같다
print(re.findall(r'[0-9]{2,3}', ss)) # 0~9까지 숫자중 3개씩 2개만 출력

print('---'*10)
print(re.findall(r'.bc', ss)) # 앞에 한글자가 뭐가오던 상관없이 bc인것
print(re.findall(r'^1+', ss)) # 첫 글자가 1으로 시작
print(re.findall(r'[^1]+', ss)) # 1을 제외 - 범위 안에 ^는 부정
print(re.findall(r'[^0-9]+', ss)) # 숫자열 있는것을 제외 - 범위 안에 ^는 부정
print(re.findall(r'nbc$', ss)) # 이건 뭔지 모르겠다.

a = re.match(r'123', ss)
print(a)
print(a.group())

