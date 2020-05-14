print('txt 파일을 읽어 dict로 저장')
# with open('mydict', 'r') as ff:
with open('mydict.txt', 'r', encoding='utf-8') as ff:
    aa = eval(ff.read())       # 보안 취약
    print(aa)
    print(type(aa))

print()
import ast
with open('mydict.txt', 'r', encoding='utf-8') as ff:
    aa = ff.read()
    print(aa)
    print(type(aa))
    print()
    bb = ast.literal_eval(aa)     # 보안 안정 보장
    print(bb)
    print(type(bb))