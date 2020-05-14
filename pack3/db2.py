import MySQLdb
import sys

config = {  # dict type
    'host': '127.0.0.1',
    'user': 'root',
    'password': '123',
    'database': 'test',
    'port': 3306,
    'charset': 'utf8',
    'use_unicode': True
}

try:
    conn = MySQLdb.connect(**config)    # dict타입의 자료는 **를 사용해서 받는다.
    # print(conn)     # 연결 확인
    cursor = conn.cursor()  # SQL문 수행을 위한 객체 생성

    # 부서 번호 별 sql문
    buserNum = input('부서 번호 입력 : ')
    # sql = 'select jikwon_no, jikwon_name, buser_num, jikwon_jik from jikwon where buser_num=%s'
    # cursor.execute(sql, (buserNum, ))

    sql = '''
        select jikwon_no, jikwon_name, buser_num, jikwon_jik
        from jikwon
        where buser_num={0}
    '''.format(buserNum)

    cursor.execute(sql)

    datas = cursor.fetchall()

    if len(datas) == 0:
        print(buserNum + '번 부서는 없어요')
        sys.exit()

    # 부서 번호 별 출력
    print('\n 출력 방법 1----------')
    print('사번\t이름\t부서번호\t직급')
    for data in datas:  # tuple type
        # print(data)
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3])
        # print('인원 수 : ', str(len(datas))) # 여기에 입력하면 사원 정보마다 밑에 인원 수가 출력된다.
    print('인원 수 : ', str(len(datas)))

except Exception as e:
    print('err : ', e)

finally:
    cursor.close()
    conn.close()