import streamlit as st
from datetime import datetime
from streamlit_autorefresh import st_autorefresh
import requests
import streamlit as st

st.title('Comtact us')

# 시간 표시를 위한 빈 플레이스홀더 생성
clock = st.empty()

# 시간을 지속적으로 업데이트하기 위한 무한 루프
show_clock = st.checkbox('시간!')

if show_clock:
    # 자동으로 페이지를 일정 간격으로 새로고침하게 해주는 함수
    # 실시간 데이터 표시, 시계,알람,센서 값등 주기적 업데이트가 필요한 경우 유용
    st_autorefresh(interval=500, key='clock_refresh')
    time = datetime.now().strftime('%H:%M:%S')

    # 플레이스홀더에 현재 시간 표시
    clock.info(f'**Current time:** {time}')

    if time > '13:19:00':
        # 알람 조건이 충족되면 시간 표시를 지우고 알람 표시
        clock.empty()
        st.warning('Alarm!!')