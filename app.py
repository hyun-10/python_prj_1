import streamlit as st

from add_pages import pages
from addpages import page1 as p1
from addpages import page2 as p2
from addpages import page3 as p3

app = pages()




app.add_page('개발환경 설정',p1.app )
app.add_page('자료표출',p2.app)
app.add_page('시계열자료',p3.app)

app.run()

