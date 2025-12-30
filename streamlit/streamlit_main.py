import subprocess
import sys


def run_streamlit(appName):
    subprocess.run([sys.executable,
                    '-m', 'streamlit', 'run',str(appName)])



# 실행진입점
# 위치는 파일 맨 아래
if __name__ == "__main__":
    # 직접호출하면 무제한반복문제발생 -자기자신을 계속호출
    # run_streamlit('13streamlit_multi_pages.py')
    # run_streamlit('14streamlit_multi_pages.py')
    run_streamlit('15streamlit_query_params.py')
