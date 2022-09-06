import streamlit as st

from add_pages import pages
app = pagess()
#import app_2
#import app_3
st.title('프로젝트1')


app.add_page('선텍하세요',db/app_1/app_0.app)
#app.add_page('개발환경 설정',db/app_1/app_1.app )
#app.add_page('자료표출',db/app_1/app_2.app)
#app.add_page('시계열자료',db/app_1/app_3.app)


app.run()





