# 개인용 DB - MariaDb와 연동
# pip install mysqlClient

import MySQLdb

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
    conn = MySQLdb.connect(**config)  # dict타입의 자료는 **을 사용해서 받는다.
    # print(conn)
    cursor = conn.cursor()

    # 자료 추가 방법 1 - 한번만 되기 때문에 주석처리 한다.
    '''
    sql = 'insert into sangdata values(13, "흑우팩", 3, 1000)'
    cursor.execute(sql) # 여기선 추가된 것처럼 보이지만 실제 DB에는 적용되지 않음. commit을 해줘야함. 되돌릴 경우 rollback을 하자
    conn.commit()
    '''

    # 자료 추가 방법2
    '''
    sql = 'insert into sangdata values(%s, %s, %s, %s)'
    #sql_data = ('14', '월정액', 5, 2000)  # tuple형
    sql_data = '14', '월정액', 5, 2000     # tuple형
    cursor.execute(sql, sql_data)
    conn.commit()
    '''

    # 자료 수정
    sql = 'update sangdata set sang=%s, su=%s, dan=%s where code=%s'
    sql_data = ('파이썬', '7', '7000', '14')
    cursor.execute(sql, sql_data)
    conn.commit()

    # 자료 삭제 - commit은 일부러 수행하지 않았다. 원본을 지우지 않기 위해서
    '''
    code = '14'
    # sql = 'delete from sangdata where code=' + code
    # sql = 'delete from sangdata where code="{0}"'.format(code)
    sql = 'delete from sangdata where code=%s'
    # cursor.execute(sql)
    cursor.execute(sql, (code, ))   # tuple type으로 주기 위해서 (code, )라고 입력함.
    conn.commit()
    '''

    # 부분 자료 읽기
    print('\n부분 자료 읽기--------')
    code = 3
    # sql = 'select * from sangdata where code=%s'
    # cursor.execute(sql, (code, ))
    sql = "select * from sangdata where code={0}".format(code)
    cursor.execute(sql)
    for data in cursor.fetchall():  # tuple type
        print(data)

    # 전체 자료 따로 읽기
    print('\n전체 자료 읽기---------')
    sql = 'select * from sangdata'
    cursor.execute(sql)

    # 출력 1 : 전체 출력
    print('출력 방법 1-----------')
    for data in cursor.fetchall():  # tuple type
        # print(data)
        print('%s %s %s %s' % data)

    print()

    # 출력 2 : 하나씩 출력
    print('\n 출력 방법 2-----------')
    for r in cursor:
        # print(r)
        print(r[0], r[1], r[2], r[3])

    # 출력 3 : 펼쳐서 담아온다.
    print('\n 출력 방법 3-----------')
    for (code, sang, su, dan) in cursor:  # code 등은 칼럼명이 아니라 변수명. 가독성을 위해서 해줌. 변수 순서에 의한 매핑이다.
        print(code, sang, su, dan)

    # 출력 4 : 칼럼명이 아닌 변수명. 가독성을 중시했을 뿐
    print('\n 출력 방법 4-----------')
    for (a, b, c, 단가) in cursor:  # code 등은 칼럼명이 아니라 변수명. 가독성을 위해서 해줌. 변수 순서에 의한 매핑이다.
        print(a, b, c, 단가)

except Exception as e:
    print('err : ', e)
finally:
    cursor.close()
    conn.close()
