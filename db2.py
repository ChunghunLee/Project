import pymysql
import MySQLdb

def DBconnect(result,user,password,db,host='13.209.68.158',port=3306):
    conn = pymysql.connect(host="13.209.68.158"    # 접속 할 주소
                     ,port=3306,user=user,         # 포트넘버 / 로그인 ID/PW
                     password=password,  
                     db=db,charset='utf8')         # DB 이름과 한글 인식을 위해 utf8 설정

    try:
           with conn.cursor() as cursor:
             sql = 'SELECT * FROM User WHERE car_num=%s'    # 차량 번호가 기본키이므로 조회값
             cursor.execute(sql,(result))                   # sql문 날림
             dbinfo = str(cursor.fetchall())                # 일치하는 DB 모두 검색
             test="C:/Users/any/Desktop/python/test.txt"    # 이 경로에 검색 결과를 작성
             f = open(test, 'a+')
            
             f.write(dbinfo)
             f.write("\n")
             print(dbinfo)
             f.close()
                
    finally:
           conn.close()

