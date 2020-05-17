class Car:
    handle = 0
    speed = 0

    def __init__(self, name, speed):  # 생성자
        self.speed = speed
        self.name = name  # 원형타입의 클래스에 새로운 객체가 만들어진다.

    def showData(self):  # Car클래스 타입의 객체를 여러개 만들것이다. 구별해야함. (ex. 버스, 택시 등)
        km = '킬로미터'  # 지역변수
        msg = '속도 : ' + str(self.speed) + km
        return msg


print(Car.handle)
print(Car.speed)
# print(Car.name)   # AttributeError: type object 'Car' has no attribute 'name'

print('\n----tom의 것--------')
car1 = Car('tom', 10)  # 생성자 호출. car1 => instance
print(type(car1))
print(car1.handle, car1.name, car1.speed)
car1.color = '검정'  # car1에서만 사용 가능한 instance
print('car1.color : ', car1.color)

print('\n---james의 것-------')
car2 = Car('james', 20)
print(car2.handle, car2.name, car2.speed)
# print('car2.color : ', car2.color)    # car2에서 color를 선언하지 않았으니 당연히 에러가 뜬다.

print()
print(id(Car), ' ', id(car1), ' ', id(car2))  # 객체가 3개 만들어진 것이다. 서로 전부 다름

print()
print(car1.showData())
print(car2.showData())
car1.speed = 88
car2.speed = 100
print(car1.showData())
print(car2.showData())

Car.handle = 1  # Car 클래스의 handle을 직접 바꿨기 때문에 car1이랑 car2에도 적용된다.
print(car1.handle)
print(car2.handle)
