# naviagtion.py
import streamlit as st

# st.navigation : 여러 페이지를 탭이나 메뉴처럼 관리할 수 있게 해주는 기능
# 리스트안에 네비게이션 메뉴를 구성할 페이지를 정의
# st.Page : st.navigation에 사용할 페이지를 정의할때 사용하는 객체

# pages = {
#     '🏠 Home': [st.Page('15streamlit_query_params.py', title='🏠 Home')],
#     '📞 Contact us':[
#         st.Page('14streamlit_message.py', title=' Message'),
#         st.Page('14streamlit_adress.py', title=' Adress'),
#     ],
# }
#
# pg = st.navigation(pages)
# pg.run()

# naviagtion3.py
import streamlit as st
import Home
import Contact

# 스트림잇의 페이지 전환을  py파일이 아닌
# if 조건문을 이용해서 url 매개변수 기반으로 구현함
# 즉, 특정 페이지를 직접 보여주는 것이 아니고
# 조건에 따라 어떤 페이지를 보여줄지 결정함
# dP) ?page=home, ?page=contact

# 현재 페이지 확인
current_page = st.query_params.get('page', ['home'])

# 페이지에 따라 올바른 콘텐츠 표시
if current_page == 'home':
    #st.title('Home Page')
    Home.run()
elif current_page == 'contact':
    Contact.run()

# 하위 URL 간 이동을 위한 링크 추가
# 버튼 클릭시 지정한 페이지를 출력하기 위해 rerun() 호출
st.sidebar.title('Pages')
if st.sidebar.button('Home'):
    st.query_params['page'] = 'home'
    st.rerun()
if st.sidebar.button('Contact'):
    st.query_params['page'] = 'contact'
    st.rerun()

