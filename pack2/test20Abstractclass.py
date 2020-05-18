# 추상 클래스 (Abstract Class)
from abc import *   # abc : abstract base class

class AbstractClass(metaclass=ABCMeta):  # 추상 클래스 : 추상 메소드를 가지고 있는 클래스

    @abstractclassmethod    # 추상 메소드 장식자
    def abcMethod(self):    # 추상 메소드
        pass

    def normalMethod(self):
        print('AbstractClass 클래스의 일반 메소드')

# abs = AbstractClass()   # TypeError : Can't instantiate abstract class
# abs.normalMethod()    # 추상 메소드가 있으면 실행할 수 없다.

class Child1(AbstractClass):    # 추상 클래스를 상속받았기 때문에 오버라이딩을 반드시 해야한다.
    name = '난 Child1'

    def abcMethod(self):
        print('추상 메소드를 오버라이딩')

c1 = Child1()   # 추상 클래스를 상속받았기 때문에 오버라이딩을 반드시 해야한다.
print(c1.name)
c1.abcMethod()
c1.normalMethod()

print()
class Child2(AbstractClass):    # 추상 클래스를 상속받았기 때문에 오버라이딩을 반드시 해야한다.
    name = '난 Child2'

    def abcMethod(self):    # 오버라이딩 강요 - 추상 메소드
        print('추상 메소드를 오버라이딩 하였다.')

    def normalMethod(self): # 오버라이딩 선택 - 일반 메소드
        print('normalMethod도 오버라이딩 하였디.')

c2 = Child2()
print(c2.name)
c2.abcMethod()
c2.normalMethod()

print()
parent = AbstractClass  # 부모타입의 주소를 가지고 자식클래스를 사용할 수 있다.
print(type(parent))
parent = c1
print(type(parent))
print(parent.name)

parent = c2
print(parent.name)

print()
imsi = c1   # 꼭 부모자식간의 관계가 필요하지 않다. 아무 변수에게나 줄 수 있다. 다형성 최고...
print(imsi.name)
imsi = c2
print(imsi.name)