# 클래스의 상속   # is = 상속
class Animal:
    def __init__(self):
        print('Animal 생성자')

    def move(self):
        print('움직이는 생물')

class Dog(Animal):  # 클래스 상속(is) : ()를 열고 상속할 클래스를 선택한다. 다형성 가능
    def __init__(self):
        print('Dog 생성자')    # 이 생성자에서 출력이 가능하면 여기서 출력하고 위의 부모클래스의 'Animal 생성자'는 출력되지 않는다

    def my(self):
        print('나는 개')

dog1 = Dog() # 현재 클래스의 생성자가 있으면 부모클래스의 생성자는 수행하지 않는다. 따로 호출해야 출력됨.
dog1.my()
dog1.move()

print('\n---------')
class Cat(Animal):
    pass

cat1 = Cat()
cat1.move

print('\n--overriding------')   # 메소드 오버라이드 : 메소드 재정의  # 파이썬은 오버로딩은 없음.
class Parent:
    def PrintData(self):
        pass

class Child1(Parent):
    def PrintData(self):
        print('Childe1에서 overriding')

class Child2(Parent):
    def PrintData(self):
        print('Child2에서 재정의')

    def abc(self):
            print('Child2 고유 매소드')

# c1 = Child1 이렇게 하면 주소를 넘기는것
c1 = Child1()   # 이렇게 ()를 써야 객체를 만드는 것이다.
c1.PrintData()

c2 = Child2()
c2.PrintData()

print('\n---다형성------')     # 다형성 : 부모 클래스로부터 물려받은 가상 함수를 자식 클래스 내에서 오버라이딩 하여 사용하는 것
# 동일한 코드이지만 동작방법, 결과가 다른 것을 의미한다.
kbs = c1
kbs.PrintData()
kbs = c2
kbs.PrintData()
kbs.abc()

print()
plist = [c1, c2]
for i in plist:
    i.PrintData()
