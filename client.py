import socket
import sys
import time
from subprocess import Popen,PIPE
from operator import eq

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('ec2-13-209-68-158.ap-northeast-2.compute.amazonaws.com',5000 ))
# 아마존 서버와 소켓통신을 연결하기 위한 주소

while True:
        #my_input = input("종료하고싶으면 0 입력 :: ")
        sbuff=sock.recv(65535)          # 소켓 포트넘버
        data=str(sbuff, encoding='utf-8')       # 통신 버퍼 읽기/쓰기       
        print("data 값 : ",data)         
        time.sleep(1)                   
        if eq(data,'uploade_complete'): # 서버로 사진 전송되었을때 알림
            print("조회 프로그램을 실행합니다.")
            p = Popen(['python',"recog.py"],stdout = PIPE, stderr = PIPE)
            stdout,stderr = p.communicate()
            data ='false'
        if eq(data,'close'):
                  print("======= 서버를 종료합니다. ========")
                  sock.close()
                  sys.exit()  
