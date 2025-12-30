import streamlit as st
from PIL import Image
from pathlib import Path

# favicon설정
# 웹사이트를 대표하는 작은 아이콘 - 브랜드 인식을 위해 사용

BASE_DIR = Path(__file__).parent
icofile = BASE_DIR / 'favicon.ico'
icon = Image.open(icofile)

# 페이지 구성
st.set_page_config(
    page_title='Hello World',
    page_icon=icon,
    layout='centered',
    initial_sidebar_state='auto',
    menu_items={
        'Get Help': 'https://streamlit.io/',
        'Report a bug': 'https://github.com',
        'About': 'About your application: **Hello World**'
    }
)

# 제목 설정
title = 'Hello World'
st.sidebar.title(title)
st.title(title)

# 헤더와 푸터를 숨기기 위한 사용자 정의 CSS
hide_streamlit_style = """
    <style>
    /* 스트림릿 헤더 숨기기 */
    header {
        visibility: hidden;
    }
    /* 스트림릿 푸터 숨기기 */
    footer {
        visibility: hidden;
    }
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)



# 사이드바에 사용자 정의 푸터 추가
custom_footer_style = """
    <div class="markdown-text-container stText" style="width: 698px;">
        <footer>
            <p></p>
        </footer>
        <div style="font-size: 14px;">Hello world v 0.1</div>
        <div style="font-size: 12px;">Hello world LLC.</div>
    </div>
    """
st.sidebar.markdown(custom_footer_style, unsafe_allow_html=True)

