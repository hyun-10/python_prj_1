# -*- coding: utf-8 -*-
import streamlit as st

def app():
	st.write('''\
\
    Windows 64-bit packages of scikit-learn can be accelerated using scikit-learn-intelex.\
    More details are available here: https://intel.github.io/scikit-learn-intelex\
\
    For example:\
\
        $ conda install scikit-learn-intelex\
        $ python -m sklearnex my_application.py\
\
\
done\
#\
# To activate this environment, use\
#\
#     $ conda activate test1\
#\
# To deactivate an active environment, use\
#\
#     $ conda deactivate'''\
    )
