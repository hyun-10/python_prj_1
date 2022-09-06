import streamlit as st

from multiple.multi_pages import multipage
import app_0
import app_1
#import app_2
#import app_3
st.title('프로젝트1')

app = multipage()
app.add_page('선텍하세요',app_0.app)
app.add_page('개발환경 설정',app_1.app )
#app.add_page('자료표출',app_2.app)
#app.add_page('시계열자료',app_3.app)


app.run()





