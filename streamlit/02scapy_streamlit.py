import streamlit as st
import pandas as pd

from scapy.all import sniff, IP, ICMP, TCP, send
from datetime import datetime

st.title("Hello, Scapy!!")

# 패킷5개캠챠후 출력
# 패킷캡쳐한것이 streamlit 콘솔에 출력

# sniff(count = 5 , prn=lambda x: print(x))
packets = sniff(count = 5)
for p in packets:
    st.text(p)

st.divider()


# 특정 프로토콜만 캡챠
packets = sniff(filter="tcp",count = 5)
for p in packets:
    st.write(p)

st.divider()

# icmp 패킷 하나 생성하고 전송
packets = IP(dst='8.8.8.8') / ICMP()
for _ in range(1):
    send(packets, verbose=0)
    st.success(" 패킷한놈 날라감!!!")

st.divider()

#패킷구조 확인
st.markdown("### 패킷구조 확인")
st.text(packets.show(dump=True))

st.divider()

# 패킷 캡쳐후 데이터프레임으로 출력
st.markdown("### 패킷 캡쳐후 데이터프레임으로 출력")
packets = sniff(filter="tcp",count = 5)
# for p in packets:
#         st.text(p.time)      #타임스탬프형식
#         st.text(p[0].src)
#         st.text(p[0].dst)
#         st.text(p[0].summary)
data = []
for p in packets:
    # data.append({
    #     "Time": p.time,
    #     "Source": p[0].src if hasattr(p[0], 'src') else "",
    #     "Destination": p[0].dst if hasattr(p[0], 'dst') else ""
    # })
    data.append({
        "Time": datetime.fromtimestamp(p.time).strftime('%Y-%m-%d %H: %M: %S'),
        "Src MAC": p[0].src if hasattr(p[0], 'src') else "",
        "Dest MAC": p[0].dst if hasattr(p[0], 'dst') else "",
        "Src IP": p[IP].src if hasattr(p[IP], 'src') else "",
        "Dest IP": p[IP].dst if hasattr(p[IP], 'dst') else "",
        "Src PORT": p[TCP].sport if hasattr(p[TCP], 'sport') else "",
        "Dest PORT": p[TCP].dport if hasattr(p[TCP], 'dport') else ""
    })


st.text(data)

df = pd.DataFrame(data)
st.dataframe(df)



# 버튼 클릭시 패킷캡쳐 시작
st.markdown("### 버튼클릭시캡쳐시작")

if st.button("캡쳐시작"):
    packets = sniff(count = 5)
    for p in packets:
        st.write(p)