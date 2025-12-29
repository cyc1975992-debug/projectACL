import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns

# 프로그램 선택을 위한 사이드바
program = st.sidebar.selectbox('Select program', ['Dataframe Demo', 'Other Demo'])
code = st.sidebar.checkbox('Display code')

# 프로그램 로직
if program == 'Dataframe Demo':
    df = px.data.stocks()
    st.title('DataFrame Demo')

    # 주식 종목 선택을 위한 멀티셀렉트
    stocks = st.multiselect('Select stocks', df.columns[1:], default=df.columns[1:])

    # 주식 데이터를 데이터프레임으로 표시
    st.subheader('Stock value')
    st.write(df[['date'] + stocks].set_index('date'))

    # 플로틀리 선 차트 그리기
    fig = px.line(df, x='date', y=stocks, hover_data={'date': '|%Y %b %d'})
    st.write(fig)

    # 체크박스 선택 시 코드 표시
    if code:
        st.code(
            """
import streamlit as st
import pandas as pd
import plotly.express as px
df = px.data.stocks()
st.title('DataFrame Demo')
program = st.sidebar.selectbox('Select program', ['Dataframe Demo', 'Other Demo'])
code = st.sidebar.checkbox('Display code')
if program == 'Dataframe Demo':
    df = px.data.stocks()
    st.title('DataFrame Demo')
    stocks = st.multiselect('Select stocks', df.columns[1:], default=df.columns[1:])
    st.subheader('Stock value')
    st.write(df[['date'] + stocks].set_index('date'))
    fig = px.line(df, x='date', y=stocks, hover_data={'date': '|%Y %b %d'})
    st.write(fig)
"""
        )
elif program == 'Other Demo':
    st.title('Other Demo')
    BASE_DIR = Path(__file__).parent
    csv_path = BASE_DIR / "auto.csv"

    st.header("Dataframes and Tables")
    df = pd.read_csv(csv_path)

    st.dataframe(df.head(10)) #가변적인 데이터출력

    st.table(df.head(30)) #정적인 데이터출력

    BASE_DIR = Path(__file__).parent
    img_path = BASE_DIR / "imgs" / "canva.jpg"
    img = Image.open(img_path)
    st.image(img, width=300, caption="Hello Logo")