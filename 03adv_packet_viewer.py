# 간단한 네트워크 패킷 스니퍼
# 차단하고 싶은 ip 설정(acl 규칙)
# 터미널 글자 색상 지정
from pickle import REDUCE

from scapy.all import sniff, IP, TCP
import sys

#터미널 색상 지정(ansi code)
# 이스케이프 시퀀스로 색상지정 : ESC[코드m
# \33: 8진수 33 -> 10진수 27 -> ESC,제어명령 시작을알림
# 90:빨강, 92,녹색, 0:검정
#  : 색상 SGR 형식(색상,굵기,밑줄,반전)으로 표기
RED       = "\033[91m"
GREEN     = "\033[92m"
Reset     = "\033[0m"

# 차단하고싶은 ip지정(acl)
#BLOCKED_IP = "8.8.8.8"
BLOCKED_IP = "104.18.23.5"

# 패킷이 캡쳐될때마다 호출되는 함수
def process_packet(packet):

    # 1. ip레이어가 있는지 확인
    # 네트워크에는 ip가없는 패킷도 존재할수 잇슴 - 주의요망!
    if packet.haslayer(IP):

        # ip헤더에서 출발지/도착지 ip 주소호출(프로토콜 번호함께)
        ip_scr = packet[IP].src
        ip_dst = packet[IP].dst

        # 출발지 ip가 지정한 ip일때 메세지출력
        if ip_scr == BLOCKED_IP:
            print(f"{RED}" + "="*45)
            print(f"[!!!경고!!!] 차단된 ip가 감지됨!!!!~~~~")

            #TCP 계층도 있다면 포트 정보도 출력
            if packet.haslayer(TCP):
                print(f"포트정보 : {packet[TCP].sport} -> {packet[TCP].dport}")
                print(f"="*45 + f"{Reset}") #색상초기화

        else:
            # 정상패킷은 그대로출력
            if packet.haslayer(TCP):
                print(f"{GREEN} [통과 패킷] {ip_scr} -> {ip_dst} {Reset}")# ip패킷이지만 tcp가아닌 경우 (udp,icmp등) 출력


#메인 실행부분- 프로그램의 시작점(실행진입점)
#현재 파이썬 파일은 직접호출했을때만 실행되게하고
#import 했을때는 자동으로 실행되지 않게 하기위한 코드
if __name__ == "__main__":
    print(">>> 패킷감시를 시작합니다...(중지는 Ctrl+C)")

    #sniff  : 패킷낚는함수
    #filter : 낚을 패킷지정
    #prn    : 패킷을 잡을때마다 호출할 함수 지정
    #store  : 잡은패킷을 메모리에 저장하지 않음(메모리부족방지)
    #sniff(filter="ip", prn=process_packet, store=0)
    sniff(prn=process_packet, store=0)
