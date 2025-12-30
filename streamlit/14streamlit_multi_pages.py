# naviagtion.py
import streamlit as st

# st.navigation : 여러 페이지를 탭이나 메뉴처럼 관리할 수 있게 해주는 기능
# 리스트안에 네비게이션 메뉴를 구성할 페이지를 정의
# st.Page : st.navigation에 사용할 페이지를 정의할때 사용하는 객체

pages = {
    '🏠 Home': [st.Page('14streamlit_home.py', title='🏠 Home')],
    '📞 Contact us':[
        st.Page('14streamlit_message.py', title=' Message'),
        st.Page('14streamlit_adress.py', title=' Adress'),
    ],
}

pg = st.navigation(pages)
pg.run()



