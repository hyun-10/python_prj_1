import streamlit as st

from add_pages import pages
from db.app_1 import crte
from db.app_1 import preed
from db.app_1 import act
from db.app_1 import stre
from db.app_1 import seab
from db.app_1 import pd
from db.app_1 import stfor
from db.app_1 import imff
from db.app_1 import frez
from db.app_1 import mo
def app():

    


    

    app = pages()


    app.add_page('선택하세요',ch.app)
    app.add_page('명령어', app_1/rd.py.app)
    app.add_page('conda create -n test1 python=3.7.4 ipython numpy matplotlib pands scipy scikit-learn tensorflow keras ', crte.app)
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
