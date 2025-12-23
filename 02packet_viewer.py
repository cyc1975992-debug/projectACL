# 간단한 네트워크 패킷 스니퍼
#from Tools.scripts.dutree import store
#from Tools.scripts.fixnotice import process
from scapy.all import sniff, IP, TCP, ICMP

#import lib.mymodule
#import lib.mymodule2

# 패킷이 캡쳐될때마다 호출되는 함수
# 여기서 패킷의 헤더정보를 꺼내봄
def process_packet(packet):

    if ICMP in packet:
        print(f"Ping이 감지되었습니다!!")

    # 1. ip레이어가 있는지 확인
    # 네트워크에는 ip가없는 패킷도 존재할수 잇슴 - 주의요망!
    if packet.haslayer(IP):

        # ip헤더에서 출발지/도착지 ip 주소호출(프로토콜 번호함께)
        ip_scr = packet[IP].src
        ip_dst = packet[IP].dst
        proto_num = packet[IP].proto #tcp : 6 , udp: 17

        #print(ip_scr, ip_scr, proto_num)

        # 2. tcp레이어가 있는지확인
        if packet.haslayer(TCP):
            # tcp헤더에서 출발지/도착지 포트번호 호출
            port_src = packet[TCP].sport
            port_dst = packet[TCP].dport

            #print(port_src, port_dst, proto_num)
            print(f"==========================")
            print(f"[TCP 패킷감시 !!]")
            print(f"누가 :{ip_scr}:{port_src}")
            print(f"어디로 :{ip_dst}:{port_dst}")
            print(f"==========================\n")
        else:
            # ip패킷이지만 tcp가아닌 경우 (udp,icmp등) 출력
            print(f"[기타 IP패킷] {ip_scr} -> {ip_dst} ({proto_num})")



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
