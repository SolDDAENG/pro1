# 모듈의 멤버로 클래스
aa = 10

def aa():
    pass

print(aa)
print()
class TestClass:
    kk = 1      # 멤버변수(클래스 내에서 전역변수) (접근 지정자 없음: 무조건 public)

    def __init__(self):     # 생성자. 소멸자에 쓸 내용이 없다면 안써도 된다.
        print('생성자')

    def __del__(self):      # 소멸자. -> 없어도 된다.
        print('소멸자')

    def printMsg(self):     # 메소드(public)
        name = '한국인'    # 지역변수
        print(name)
        print(self.kk)

test = TestClass()  # 생성자 호출. instance
print(test.kk)
print(TestClass.kk)     # prototype(원형) 클래스의 멤버 직접 호출

print()
test.printMsg()     # Bound Method Call = 인스턴스 객체에 bind 된 함수를 호출
                    # self를 붙인 쪽을 bound, 안 붙인 쪽은 unbound 메소드
# TestClass.printMsg()   # 인스턴스를 하지 않 # TypeError: printMsg() missing 1 required positional argument: 'self'
TestClass.printMsg(test)    # Unbound Method Call
print()
print(type(1))
print(type(test))   # <class '__main__.TestClass'>
print(id(test))
print(id(TestClass))

# del test      # 객체 지우기
# test.printMsg()