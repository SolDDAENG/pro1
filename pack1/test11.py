# 사용자 정의 모듈 연습
print('이런 저런 작업을 하다가...')

import pack1.mymod1
print(dir(pack1.mymod1))

list1 = [1, 2]
list2 = [3, 4, 5]
pack1.mymod1.ListHap(list1, list2)

# 여러 모듈 중 응용프로그램의 시작 모듈을 명시적으로 표시하기
# test11이 메인모튤. mymod는 메인모듈이 아니다.
if __name__ == '__main__':
    print('최상위 메인모듈')

pack1.mymod1.Kbs()

from pack1 import mymod1
mymod1.Kbs()

from pack1.mymod1 import Kbs, Mbc, gvar
Kbs()
Mbc()
print(gvar)

print('--------')
from etc.mymod2 import *
print(Hap(5, 3))
print(Cha(5, 3))

print('--------')
import mymod3
print(mymod3.Gop(4, 3))
from mymod3 import Nanugi
print(Nanugi(4, 3))