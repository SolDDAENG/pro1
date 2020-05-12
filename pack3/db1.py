# 개인용 DB - MiriaDB와 연동

import MySQLdb

# conn = MySQLdb.connect(host = '127.0.0.1', user = 'root', password='123', database='test')
# print(conn)
# conn.close

config = {  # dict타입
    'host': '127.0.0.1',
    'user': 'root',
    'password': '123',
    'database': 'test',
    'port': 3306,
    'charset': 'utf8',
    'use_unicode': True
}

try:
    conn = MySQLdb.connect(**config)  # config가 dict타입이기 때문에 **를 써서 **config로 받아야한다.
    # print(conn)
    cursor = conn.cursor()  # SQL문 수행을 위한 cursor 객체 생성

    # 부분 자료 읽기
    code = 3
    #     sql = "select * from sangdata where code=%s"
    #     cursor.execute(sql, (code, ))
    sql = "select * from sangdata where code='{0}'".format(code)
    cursor.execute(sql)

    for data in cursor.fetchall():  # tuple type
        # fetchall() 메서드는 모든 데이타를 한꺼번에 클라이언트로 가져올 때 사용
        print(data)

    print('-----')
    # select all : 전체 자료 읽기
    sql = "select * from sangdata"
    cursor.execute(sql)

    # 출력1
    for data in cursor.fetchall():  # tuple type
        # print(data)
        print('%s %s %s %s' % data)

    print('-----')
    # 출력2
    for r in cursor:
        # print(r)
        print(r[0], r[1], r[2], r[3])

    print('-----')
    # 출력3
    for (code, sang, su, dan) in cursor:    # 여기서 code, sang, su, dan 는 칼럼명이 아닌 변수명이다.
        print(code, sang, su, dan)

    print('-----')
    # 출력4
    for (a, b, c, 단가) in cursor:
        print(a, b, c, 단가)

except Exception as e:
    print('err : ', e)
finally:
    cursor.close()
    conn.close()
