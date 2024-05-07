# path : common\\dbConnectTemplate.py
# module : common.dbConnectTemplate
# 데이터베이스 연결 관리용 공통 모듈 정의 (변수와 함수로만 정의)

# 1. 사용할 패키지(모듈) 임포트함
import cx_Oracle

# 오라클 연결을 위한 값들을 전역변수로 지정.
dbUrl = 'localhost:1521/xe'
dbUser = 'c##testweb'
dbPass = 'testweb'

# 2. 오라클 드라이브(instantclient) 등록  / 1회 실행
# 방법 1 : 환경변수 path 에 등록 (파이썬 코드로 등록할 수 있음)
# location  ='D:\\instantclient_18_5'
# os.environ['PATH']  = location + ';' + os.environ['PATH']

def oracle_init(): # 어플리케이션에서 한번만 구동시킴
    cx_Oracle.init_oracle_client(lib_dir='D:\\instantclient_18_5')
    # Mac 에서는 필요없음.

def connect():
    try :
        conn = cx_Oracle.connect(dbUser, dbPass, dbUrl)
        # Mac 에서는 아래구문을 사용해야 함.
        # conn = cx_Oracle.connect('c##testweb/testweb@localhost:1521/xe')
        conn.autocommit = False
        return conn
    except Exception as msg :
        print('오라클 연결 에러 : ', msg)

def close(conn) :
    try :
        if conn :       # conn != null 과 같음. (True 이면)
            conn.close()
    except Exception as msg :
        print('오라클 닫기 실패 : ', msg)

def commit(conn) :
    try:
        if conn:  # conn != null 과 같음. (True 이면)
            conn.commit()
    except Exception as msg:
        print('오라클 트랜잭션 커밋 실패 : ', msg)

def rollback(conn) :
    try:
        if conn:  # conn != null 과 같음. (True 이면)
            conn.rollback()
    except Exception as msg:
        print('오라클 트랜잭션 롤백 실패 : ', msg)



