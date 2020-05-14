# 사용자 정의 모듈
gvar = 123  #gvar = 전역변수

def ListHap(*ar):
    print(ar)
    # if __name__ = '__main__':
    # print('최상위 메인모듈')   # 최상위 모듈이 아니기 때문에 if가 False를 만나 출력 X

def Kbs():
    print('채널9')

def Mbc():
    print('문화방송')