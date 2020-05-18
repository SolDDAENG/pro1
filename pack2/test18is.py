# 클래스 상속 (is)
class Person:
    say = '난 사람이야~~~'
    nai = 20
    __kbs = '공용방송'  # __변수명 : private

    def __init__(self, nai):
        print('Person 생성자')
        self.nai = nai

    def PrintInfo(self):
        print('나이 : {}, 이야기 : {}'.format(self.nai, self.say))

    def Hello(self):
        print('안녕')
        print(self.__kbs)

    @staticmethod  # 장식자(decoating)
    # staticmethod 는 아래와 같이 @staticmethod 라는 데코레이터를 사용하여 정의할 수 있다. 인스턴스메소드와 달리 self라는 인자를 가지고있지 않다.
    def sbs(tel):
        print('tel : ', tel)
        # print(self.say)   # static 메소드의 argument는 안된다.


print(Person.say, ' ', Person.nai)
print()

p = Person('22')  # 생성자 호출. 객체 생성
print(p.nai)
p.PrintInfo()  # 나이 : 22, 이야기 : 난 사람이야~~~
p.Hello()

print('---' * 20)
class Employee(Person):
    say = '일하는 동물'
    subject = '근로자'

    def __init__(self):
        print('Employee 생성자')

    def PrintInfo(self):
        print('Employee의 PrintInfo')

    def EprintInfo(self):
        print(self.say, ' ', super().say)
        super().PrintInfo()
        self.PrintInfo()
        self.Hello()
        # print(self.__kbs)     # err : private 멤버이므로

e = Employee()
print(e.say, ' ', e.nai, ' ', e.subject)    # 일하는 동물   20   근로자
e.EprintInfo()

print('\n------------')
class Worker(Person):
    def __init__(self, nai):
        print('Worker 생성자')
        super().__init__(nai)   # Bound Method Call

    def PrintInfo(self):
        print('Worker의 PrintInfo')

    def WprintInfo(self):
        self.PrintInfo()    # 위의 PrintInfo가 없으면 부모클래스의 PrintInfo가 출력된다.
        super().PrintInfo()

w = Worker('33')
print(w.say, ' ', w.nai)
w.WprintInfo()
w.PrintInfo()

print('\n-------------------')
class Programmer(Worker):
    def __init__(self, nai):
        print('Programmer 생성자')
        # super().__init__(nai)
        Worker.__init__(self, nai)  # UnBound Method Call : 클래스를 통해 함수를 호출하며, 인스턴스 객체를 parameter 로 전달.

    def WprintInfo(self):
        print('Programmer에서 오버라이딩')

pr = Programmer('44')
print(pr.say, ' ', pr.nai)
pr.WprintInfo()
pr.PrintInfo()

print('\n------------------')
print(type(12.3))   # type : float
print(type(pr))     # type : Programmer
print(type(w))      # type : Worker
print(Person.__bases__)     # object
print(Programmer.__bases__) # Worker
print()
pr.sbs('123-4567')  # 권장하지 않음. Person의 자식 어느 누구나 가능하지만 이 방벙은 권장하지 않음.
Person.sbs('234-3333')  # 이 방법을 권장
