import streamlit as st

from add_pages import pages
from addpages import page1 as p1
app = pages()




app.add_page('개발환경 설정',p1.app )


app.run()

