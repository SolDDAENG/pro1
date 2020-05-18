# 다중 상속
class Tiger:
    data = '호랑이 세계'

    def Cry(self):
        print('호랑이 어흥')

    def Eat(self):
        print('맹수는 고기를 좋아함')

class Lion:

    def Cry(self):  # 나중에 상속되어서 인식할 수 없다.
        print('사자 으르렁')

    def Hobby(self):
        print('백수의 왕은 낮잠을 즐겨함')

class Liger1(Tiger, Lion):   # 다중 상속 : 중복된 메소드가 있을 경우 먼저 상속한 Tiger의 것만 상속받는다.
    pass

aa = Liger1()
aa.Cry()    # Tiger.Cry()를 취한다. 우선순위에 의해 먼저 상속받은 쪽을 실행한다.
aa.Eat()
aa.Hobby()
print(aa.data)

print()
class Liger2(Lion, Tiger):
    data = '라이거 만세'

    def Play(self):
        self.Cry()
        super().Cry()
        print(self.data)
        print(super().data)

    def Hobby(self):
        print('라이거는 낮잠을 좋아함')

bb = Liger2()
bb.Play()
bb.Hobby()