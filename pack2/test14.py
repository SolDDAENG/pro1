kor = 100


def abc():
    print('난 모듈의 멤버인 함수')


class My:
    kor = 90

    def abc(self):
        print('메소드')

    def show(self):
        kor = 77  # 메소드 내에서 kor을 호출하면 클래스 내에서 먼저 찾고 없으면 위에서 찾음. kor = 77을 없애면 위의 kk = 100을 가져온다
        print(kor)
        print(self.kor)
        self.abc()
        abc()


m = My()
m.show()

print('\n----------------')
class Our:
    a = 1

o1 = Our()
print(o1.a)
o1.a = 2
print(o1.a)

print()
o2 = Our()
print(o2.a)
o2.b = 10
print(o2.b)

# print(o1.b)     # err
print(Our.a)
# print(Our.b)    # ree

print(type(o1))     # Our 클래스 type.  # 클래스 : 나만의 새로운 타입을 만드는것.

print('\n---클래스는 새로운 type을 생성--------')
class Singer:
    titleSong = '겁쟁이'

    def sing(self):
        msg = '노래는'
        print(msg, self.titleSong, '겁쟁이이잉')

buzz = Singer()
buzz.sing()

print()
redvelvet = Singer()
redvelvet.sing()
redvelvet.titleSong = '빨간맛'
redvelvet.sing()
redvelvet.co = "SM"
print('레드벨벳 소속사 : ', redvelvet.co)
print()
buzz.sing()
# print('버즈 소속사 : ', buzz.co)     # err