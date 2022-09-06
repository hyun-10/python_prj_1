import streamlit as st


def app():




    

    app = multipage()


    app.add_page('선택하세요', db/app_1/ch.app)
    app.add_page('명령어', db/app_1/rd.app)
    app.add_page('conda create -n test1 python=3.7.4 ipython numpy matplotlib pands scipy scikit-learn tensorflow keras ', db/app_1/crte.app)
    app.add_page('proceed',db/app_1/preed.app)
    app.add_page('conda activate test1', db/app_1/act.app)
    app.add_page('pip install streamlit', db/app_1/stre.app)
    app.add_page('pip install seaborn', db/app_1/seab.app)
    app.add_page('pip install pandas', db/app_1/pd.app)
    app.add_page('pip install streamlit_forum', db/app_1/stfor.app)
    app.add_page('pip install imageio_ffmpeg', db/app_1/imff.app)

    app.add_page('pip freeze', db/app_1/frez.app)
    app.add_page('more', db/app_1/mo.app)


    app.run()
