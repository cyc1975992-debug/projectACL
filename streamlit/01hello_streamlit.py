import streamlit as st
from PIL import Image
import datetime
import time
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#기본 텍스트 위젯
st.title("Streamlit Basics")
st.header("This is a header")
st.subheader("This is a subheader")
st.text("This is a simple 용철")
st.write("This is a write dimension") #만능출력함수

# 마크다운을 이용한 출력지원(추천!!)
st.markdown("## 마크다운을 이용한 제목")
st.markdown("[Streamlit](https://www.streamlit.io)")
st.markdown("https://www.streamlit.io")


# 사용자 작성 html 코드도 삽입가능
html_page = """
<div style="background-color:orange; padding:50px">
<p style="color:white; font-size:50px">Enjoy Hell!</p>
</div>
"""
st.markdown(html_page, unsafe_allow_html=True)


# 구분선 위젯
# st.divider()
st.markdown("---")


# 간단한 알림상자 위젯
st.success("Success!")
st.info("Information")
st.warning("This is a warning!")
st.error("This is an error!")





# 테스트2
import streamlit as st
import time

if st.button("축하 버튼을 눌러보세요!"):
    st.balloons() # 풍선 애니메이션
    st.snow()     # 눈 내리는 애니메이션
    st.toast("축하합니다! 작업이 완료되었습니다.")




# 이미지불러오기
from pathlib import Path

BASE_DIR = Path(__file__).parent
img_path = BASE_DIR / "imgs" / "canva.jpg"

img = Image.open(img_path)
st.image(img, width=300, caption="Hello Logo")





#유튜브 url도 포함가능
st.video("https://www.youtube.com/watch?v=hRPMf7_OpzM")


st.markdown("---")




# qjxmstm
st.button("Play1")

if st.button("Play2"): #play2 버튼이 클릭되었다면
    st.text("Hello world!")

if st.checkbox("Checkbox"): #checkbox 버튼을 클릭하면
    st.text("Checkbox selected")

radio_but = st.radio("Your Selection", ["A", "B"])
if radio_but == "A":  # a라디오버튼 클릭하면
    st.info("You selected A")
else:
    st.info("You selected B")

city = st.selectbox("Your City", ["Napoli", "Palermo", "Catania", "평양"])

occupation = st.multiselect("Your Occupation",
                            ["Programmer", "Data Scientist", "IT Consultant", "DBA", "해커"])


st.divider()




Name = st.text_input("Your Name", "Write something…")
st.text(Name)

Age = st.number_input("Input a number")
message = st.text_area("Your Message", "Write something...")
select_val = st.slider("Select a Value", 1, 10)



st.divider()



if st.button("Balloons"):
    st.balloons()

if st.button("눈 내리기"):
    st.snow()


st.divider()



#날짜/시간
today = st.date_input("Today is",datetime.datetime.now())
hour = st.time_input("The time is",datetime.time(12,30))

# json 데이터를 돌리는위젯
data = {"name":"John","surname":"Wick"}
st.json(data)
st.code("import pandas as pd")


st.divider()



my_bar = st.progress(0)

for value in range(10):
    time.sleep(0.01)
    my_bar.progress(value+1)
#스피너위젯
with st.spinner("Please wait..."):
    time.sleep(2)

st.success("Done!")


st.divider()


csv_path = BASE_DIR / "auto.csv"

st.header("Dataframes and Tables")
df = pd.read_csv(csv_path)
st.dataframe(df.head(30)) #가변적인 데이터출력

st.table(df.head(30)) #정적인 데이터출력


st.divider()

# 차트위젯
st.area_chart(df[["mpg","cylinders"]])
st.bar_chart(df[["mpg","cylinders"]].head(20))
st.line_chart(df[["mpg","cylinders"]].head(20))


st.divider()

#matplotlib, seaborn 위젯
fig, ax = plt.subplots()
corr_plot = sns.heatmap(df[["mpg","cylinders", "displacement"]].corr(), annot= True)
st.pyplot(fig)


