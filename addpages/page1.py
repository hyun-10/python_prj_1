import streamlit as st

from multiple.multi_pages import multipage
from pages import create as crte
from pages import proceed as preed
from pages import activate as act
from pages import streamlit as stre
from pages import seaborn as seab
from pages import pandas as pd
from pages import streamlit_forum as stfor
from pages import imageio_ffmpeg as imff
from pages import freeze as frez
from pages import more as mo
from pages import rd
from pages import ch



st.title('프로젝트 1')

app = multipage()


app.add_page('선택하세요', ch.app)
app.add_page('명령어', rd.ap)
app.add_page('conda create -n test1 python=3.7.4 ipython numpy matplotlib pands scipy scikit-learn tensorflow keras ', crte.ap)
app.add_page('proceed',preed.app)
app.add_page('conda activate test1', act.app)
app.add_page('pip install streamlit', stre.app)
app.add_page('pip install seaborn', seab.app)
app.add_page('pip install pandas', pd.app)
app.add_page('pip install streamlit_forum', stfor.app)
app.add_page('pip install imageio_ffmpeg', imff.app)

app.add_page('pip freeze', frez.app)
app.add_page('more', mo.app)


app.run()
