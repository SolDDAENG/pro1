# 클래스의 포함   # has = 포함
# import etc.handle   # 포함 방법 1
from etc.handle import PohamHandle  # 포함 방법 2

class PohamCar:
    turnShow = '정지'

    def __init__(self, ownerName):  # 프로토타입 없고 각각의 ownerName만 있다는것
        self.ownerName = ownerName
        # self.ownerName = etc.handle.PohamHandle()   # 클래스의 포함 or from etc.handle import PohamHandle
        self.handle = PohamHandle()
        # __init__은 파이썬에서 클래스의 생성자를 만들때 항상 동일한 규칙.
        # __init__을 사용하면 클래스명을 쓰고 옆에 바로 인자들을 채워 넣음으로써 그 값들을 지닌 객체를 만들어 낼 수 있다.

    def TurnHandle(self, q):
        if q > 0:
            self.turnShow = self.handle.RightTurn(q)
        elif q < 0:
            self.turnShow = self.handle.LeftTurn(q)
        else:
            self.turnShow = '직진'

if __name__ == '__main__':  # 해당 모듈이 임포트된 경우가 아니라 인터프리터에서 직접 실행된 경우에만, if문 이하의 코드를 돌리라는 명령
    tom = PohamCar('tom')
    tom.TurnHandle(10)
    print(tom.ownerName + '의 회전량은 ' + tom.turnShow + str(tom.handle.quantity))
    tom.TurnHandle(-15)
    print(tom.ownerName + '의 회전량은 ' + tom.turnShow + str(tom.handle.quantity))

    print()
    james = PohamCar('jame')
    james.TurnHandle(0)
    print(james.ownerName + '의 회전량은 ' + james.turnShow + str(james.handle.quantity))
