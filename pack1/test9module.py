# module : 코드의 재사용을 가능하게 하며, 하나의 이름 공간으로 별도 관리가 가능하다.
# module은 package 내에서 작성해야 한다.
print('뭔가를 하다가...')
a = 10
print(a)
def aa():
    pass

import sys  # 표준 모듈 읽기
print(sys.path)
# sys.exit() # 프로그램의 강제 종료. 이후를 실행하지 않음.
print('종료') # sys.exit()이 실행될때 만나지 않음.

import math
print(math.pi)
print(math.sin(math.radians(30)))

print()
import calendar
calendar.prmonth(2020, 5)

print('\n-----난수 출력-------------')
import random # 모듈 전체 호출
print(random.random()) # random모듈에서 random이라는 함수를 호출 한 것이다.
print(random.randrange(1, 10)) # random모듈에서 randrange() 함수 호출한 것.

# 전체 import가 아닌 일부 멤버만 호출해서 사용하는 방법
from random import random, randrange # from 모듈명 import 멤버명 : random 모듈로부터  random 멤버와 randrange 멤버를 호출
print(random()) # import를 하지 않고 하나의 멤버만 마치 현재 모듈러의 멤버인 것처럼 호출해서 사용 할 수 있다.
print(randrange(1, 10))

from random import *    # random모듈의 모든 멤버를 사용하겠다고 선언. 하지만 별로 좋지는 않음. java.lang.* 랑 같은 맥락

from turtle import *
p = Pen() # 클래스의 생성자를 호출
p.color('red', 'yellow')
p.begin_fill()
while True:
    p.forward(200)
    p.left(170)
    if abs(p.pos()) < 1:
        break
p.end_fill()
done()