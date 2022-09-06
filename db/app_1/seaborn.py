# -*- coding: utf-8 -*-
import streamlit as st
def app():
	st.write("Collecting streamlit_forum\
  Downloading streamlit_forum-0.0.1-py3-none-any.whl (8.0 kB)\
Requirement already satisfied: streamlit>=1.0.0 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from streamlit_forum) (1.9.2)\
Requirement already satisfied: requests>=2.20.0 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from streamlit_forum) (2.27.1)\
Requirement already satisfied: idna<4,>=2.5 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from requests>=2.20.0->streamlit_forum) (3.3)\
Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from requests>=2.20.0->streamlit_forum) (1.26.9)\
Requirement already satisfied: certifi>=2017.4.17 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from requests>=2.20.0->streamlit_forum) (2022.5.18.1)\
Requirement already satisfied: charset-normalizer~=2.0.0 in c\\users\82103\.conda\envs\test1\lib\site-packages (from requests>=2.20.0->streamlit_forum) (2.0.4)\
Requirement already satisfied: numpy in c:\\users\82103\.conda\envs\test1\lib\site-packages (from streamlit>=1.0.0->streamlit_forum) (1.21.5)\
Requirement already satisfied: pandas>=0.21.0 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from streamlit>=1.0.0->streamlit_forum) (1.3.5)\
Requirement already satisfied: watchdog in c:\\users\82103\.conda\envs\test1\lib\site-packages (from streamlit>=1.0.0->streamlit_forum) (2.1.8)\
Requirement already satisfied: gitpython!=3.1.19 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from streamlit>=1.0.0->streamlit_forum) (3.1.27)\
Requirement already satisfied: click<8.1,>=7.0 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from streamlit>=1.0.0->streamlit_forum) (8.0.4)\
Requirement already satisfied: altair>=3.2.0 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from streamlit>=1.0.0->streamlit_forum) (4.2.0)\
Requirement already satisfied: importlib-metadata>=1.4 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from streamlit>=1.0.0->streamlit_forum) (4.11.3)\
Requirement already satisfied: packaging in c:\\users\82103\.conda\envs\test1\lib\site-packages (from streamlit>=1.0.0->streamlit_forum) (21.3)\
Requirement already satisfied: pydeck>=0.1.dev5 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from streamlit>=1.0.0->streamlit_forum) (0.7.1)\
Requirement already satisfied: typing-extensions in c:\\users\82103\.conda\envs\test1\lib\site-packages (from streamlit>=1.0.0->streamlit_forum) (4.1.1)\
Requirement already satisfied: pympler>=0.9 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from streamlit>=1.0.0->streamlit_forum) (1.0.1)\
Requirement already satisfied: attrs in c:\\users\82103\.conda\envs\test1\lib\site-packages (from streamlit>=1.0.0->streamlit_forum) (21.4.0)\
Requirement already satisfied: pyarrow in c:\\users\82103\.conda\envs\test1\lib\site-packages (from streamlit>=1.0.0->streamlit_forum) (8.0.0)\
Requirement already satisfied: blinker in c:\\users\82103\.conda\envs\test1\lib\site-packages (from streamlit>=1.0.0->streamlit_forum) (1.4)\
Requirement already satisfied: semver in c:\\users\82103\.conda\envs\test1\lib\site-packages (from streamlit>=1.0.0->streamlit_forum) (2.13.0)\
Requirement already satisfied: python-dateutil in c:\\users\82103\.conda\envs\test1\lib\site-packages (from streamlit>=1.0.0->streamlit_forum) (2.8.2)\
Requirement already satisfied: tornado>=5.0 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from streamlit>=1.0.0->streamlit_forum) (6.1)\
Requirement already satisfied: tzlocal in c:\\users\82103\.conda\envs\test1\lib\site-packages (from streamlit>=1.0.0->streamlit_forum) (4.2)\
Requirement already satisfied: cachetools>=4.0 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from streamlit>=1.0.0->streamlit_forum) (4.2.2)\
Requirement already satisfied: validators in c:\\users\82103\.conda\envs\test1\lib\site-packages (from streamlit>=1.0.0->streamlit_forum) (0.19.0)\
Requirement already satisfied: toml in c:\\users\82103\.conda\envs\test1\lib\site-packages (from streamlit>=1.0.0->streamlit_forum) (0.10.2)\
Requirement already satisfied: pillow>=6.2.0 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from streamlit>=1.0.0->streamlit_forum) (9.0.1)\
Requirement already satisfied: jinja2 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from altair>=3.2.0->streamlit>=1.0.0->streamlit_forum) (3.1.2)\
Requirement already satisfied: entrypoints in c:\\users\82103\.conda\envs\test1\lib\site-packages (from altair>=3.2.0->streamlit>=1.0.0->streamlit_forum) (0.4)\
Requirement already satisfied: toolz in c:\\users\82103\.conda\envs\test1\lib\site-packages (from altair>=3.2.0->streamlit>=1.0.0->streamlit_forum) (0.11.2)\
Requirement already satisfied: jsonschema>=3.0 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from altair>=3.2.0->streamlit>=1.0.0->streamlit_forum) (4.6.0)\
Requirement already satisfied: colorama in c:\\users\82103\.conda\envs\test1\lib\site-packages (from click<8.1,>=7.0->streamlit>=1.0.0->streamlit_forum) (0.4.4)\
Requirement already satisfied: gitdb<5,>=4.0.1 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from gitpython!=3.1.19->streamlit>=1.0.0->streamlit_forum) (4.0.9)\
Requirement already satisfied: smmap<6,>=3.0.1 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19->streamlit>=1.0.0->streamlit_forum) (5.0.0)\
Requirement already satisfied: zipp>=0.5 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from importlib-metadata>=1.4->streamlit>=1.0.0->streamlit_forum) (3.8.0)\
Requirement already satisfied: importlib-resources>=1.4.0 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from jsonschema>=3.0->altair>=3.2.0->streamlit>=1.0.0->streamlit_forum) (5.7.1)\
Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from jsonschema>=3.0->altair>=3.2.0->streamlit>=1.0.0->streamlit_forum) (0.18.1)\
Requirement already satisfied: pytz>=2017.3 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from pandas>=0.21.0->streamlit>=1.0.0->streamlit_forum) (2021.3)\
Requirement already satisfied: traitlets>=4.3.2 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from pydeck>=0.1.dev5->streamlit>=1.0.0->streamlit_forum) (5.2.2.post1)\
Requirement already satisfied: ipywidgets>=7.0.0 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from pydeck>=0.1.dev5->streamlit>=1.0.0->streamlit_forum) (7.7.0)\
Requirement already satisfied: ipykernel>=5.1.2 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from pydeck>=0.1.dev5->streamlit>=1.0.0->streamlit_forum) (6.13.0)\
Requirement already satisfied: debugpy>=1.0 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit>=1.0.0->streamlit_forum) (1.6.0)\
Requirement already satisfied: matplotlib-inline>=0.1 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit>=1.0.0->streamlit_forum) (0.1.2)\
Requirement already satisfied: psutil in c:\\users\82103\.conda\envs\test1\lib\site-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit>=1.0.0->streamlit_forum) (5.9.1)\
Requirement already satisfied: ipython>=7.23.1 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit>=1.0.0->streamlit_forum) (7.31.1)\
Requirement already satisfied: jupyter-client>=6.1.12 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit>=1.0.0->streamlit_forum) (7.3.1)\
Requirement already satisfied: nest-asyncio in c:\\users\82103\.conda\envs\test1\lib\site-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit>=1.0.0->streamlit_forum) (1.5.5)\
Requirement already satisfied: setuptools>=18.5 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from ipython>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit>=1.0.0->streamlit_forum) (61.2.0)\
Requirement already satisfied: backcall in c:\\users\82103\.conda\envs\test1\lib\site-packages (from ipython>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit>=1.0.0->streamlit_forum) (0.2.0)\
Requirement already satisfied: prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from ipython>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit>=1.0.0->streamlit_forum) (3.0.20)\
Requirement already satisfied: jedi>=0.16 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from ipython>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit>=1.0.0->streamlit_forum) (0.18.1)\
Requirement already satisfied: decorator in c:\\users\82103\.conda\envs\test1\lib\site-packages (from ipython>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit>=1.0.0->streamlit_forum) (5.1.1)\
Requirement already satisfied: pickleshare in c:\\users\82103\.conda\envs\test1\lib\site-packages (from ipython>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit>=1.0.0->streamlit_forum) (0.7.5)\
Requirement already satisfied: pygments in c:\\users\82103\.conda\envs\test1\lib\site-packages (from ipython>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit>=1.0.0->streamlit_forum) (2.11.2)\
Requirement already satisfied: nbformat>=4.2.0 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit>=1.0.0->streamlit_forum) (5.4.0)\
Requirement already satisfied: ipython-genutils~=0.2.0 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit>=1.0.0->streamlit_forum) (0.2.0)\
Requirement already satisfied: jupyterlab-widgets>=1.0.0 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit>=1.0.0->streamlit_forum) (1.1.0)\
Requirement already satisfied: widgetsnbextension~=3.6.0 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit>=1.0.0->streamlit_forum) (3.6.0)\
Requirement already satisfied: parso<0.9.0,>=0.8.0 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from jedi>=0.16->ipython>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit>=1.0.0->streamlit_forum) (0.8.3)\
Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from jinja2->altair>=3.2.0->streamlit>=1.0.0->streamlit_forum) (2.1.1)\
Requirement already satisfied: jupyter-core>=4.9.2 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from jupyter-client>=6.1.12->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit>=1.0.0->streamlit_forum) (4.10.0)\
Requirement already satisfied: pyzmq>=22.3 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from jupyter-client>=6.1.12->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit>=1.0.0->streamlit_forum) (23.0.0)\
Requirement already satisfied: pywin32>=1.0 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from jupyter-core>=4.9.2->jupyter-client>=6.1.12->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit>=1.0.0->streamlit_forum) (304)\
Requirement already satisfied: fastjsonschema in c:\\users\82103\.conda\envs\test1\lib\site-packages (from nbformat>=4.2.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit>=1.0.0->streamlit_forum) (2.15.3)\
Requirement already satisfied: wcwidth in c:\\users\82103\.conda\envs\test1\lib\site-packages (from prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0->ipython>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit>=1.0.0->streamlit_forum) (0.2.5)\
Requirement already satisfied: six>=1.5 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from python-dateutil->streamlit>=1.0.0->streamlit_forum) (1.16.0)\
Requirement already satisfied: notebook>=4.4.1 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from widgetsnbextension~=3.6.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit>=1.0.0->streamlit_forum) (6.4.11)\
Requirement already satisfied: argon2-cffi in c:\\users\\82103\.conda\envs\test1\lib\site-packages (from notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit>=1.0.0->streamlit_forum) (21.3.0)\
Requirement already satisfied: Send2Trash>=1.8.0 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit>=1.0.0->streamlit_forum) (1.8.0)\
Requirement already satisfied: prometheus-client in c:\\users\82103\.conda\envs\test1\lib\site-packages (from notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit>=1.0.0->streamlit_forum) (0.14.1)\
Requirement already satisfied: terminado>=0.8.3 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit>=1.0.0->streamlit_forum) (0.15.0)\
Requirement already satisfied: nbconvert>=5 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit>=1.0.0->streamlit_forum) (6.5.0)\
Requirement already satisfied: defusedxml in c:\\users\82103\.conda\envs\test1\lib\site-packages (from nbconvert>=5->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit>=1.0.0->streamlit_forum) (0.7.1)\
Requirement already satisfied: pandocfilters>=1.4.1 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from nbconvert>=5->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit>=1.0.0->streamlit_forum) (1.5.0)\
Requirement already satisfied: nbclient>=0.5.0 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from nbconvert>=5->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit>=1.0.0->streamlit_forum) (0.6.4)\
Requirement already satisfied: bleach in c:\\users\82103\.conda\envs\test1\lib\site-packages (from nbconvert>=5->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit>=1.0.0->streamlit_forum) (5.0.0)\
Requirement already satisfied: beautifulsoup4 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from nbconvert>=5->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit>=1.0.0->streamlit_forum) (4.11.1)\
Requirement already satisfied: tinycss2 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from nbconvert>=5->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit>=1.0.0->streamlit_forum) (1.1.1)\
Requirement already satisfied: mistune<2,>=0.8.1 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from nbconvert>=5->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit>=1.0.0->streamlit_forum) (0.8.4)\
Requirement already satisfied: jupyterlab-pygments in c:\\users\82103\.conda\envs\test1\lib\site-packages (from nbconvert>=5->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit>=1.0.0->streamlit_forum) (0.2.2)\
Requirement already satisfied: pywinpty>=1.1.0 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from terminado>=0.8.3->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit>=1.0.0->streamlit_forum) (2.0.5)\
Requirement already satisfied: argon2-cffi-bindings in c:\\users\82103\.conda\envs\test1\lib\site-packages (from argon2-cffi->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit>=1.0.0->streamlit_forum) (21.2.0)\
Requirement already satisfied: cffi>=1.0.1 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from argon2-cffi-bindings->argon2-cffi->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit>=1.0.0->streamlit_forum) (1.15.0)\
Requirement already satisfied: pycparser in c:\\users\82103\.conda\envs\test1\lib\site-packages (from cffi>=1.0.1->argon2-cffi-bindings->argon2-cffi->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit>=1.0.0->streamlit_forum) (2.21)\
Requirement already satisfied: soupsieve>1.2 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from beautifulsoup4->nbconvert>=5->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit>=1.0.0->streamlit_forum) (2.3.2.post1)\
Requirement already satisfied: webencodings in c:\\users\82103\.conda\envs\test1\lib\site-packages (from bleach->nbconvert>=5->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit>=1.0.0->streamlit_forum) (0.5.1)\
Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from packaging->streamlit>=1.0.0->streamlit_forum) (3.0.4)\
Requirement already satisfied: pytz-deprecation-shim in c:\\users\82103\.conda\envs\test1\lib\site-packages (from tzlocal->streamlit>=1.0.0->streamlit_forum) (0.1.0.post0)\
Requirement already satisfied: backports.zoneinfo in c:\\users\82103\.conda\envs\test1\lib\site-packages (from tzlocal->streamlit>=1.0.0->streamlit_forum) (0.2.1)\
Requirement already satisfied: tzdata in c:\\users\82103\.conda\envs\test1\lib\site-packages (from tzlocal->streamlit>=1.0.0->streamlit_forum) (2022.1)\
Installing collected packages: streamlit-forum\
Successfully installed streamlit-forum-0.0.1\
(test1) PS C:\\Users\82103> pip install seaborn\
Requirement already satisfied: seaborn in c:\\users\82103\.conda\envs\test1\lib\site-packages (0.11.2)\
Requirement already satisfied: matplotlib>=2.2 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from seaborn) (3.5.1)\
Requirement already satisfied: scipy>=1.0 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from seaborn) (1.7.3)\
Requirement already satisfied: pandas>=0.23 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from seaborn) (1.3.5)\
Requirement already satisfied: numpy>=1.15 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from seaborn) (1.21.5)\
Requirement already satisfied: kiwisolver>=1.0.1 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from matplotlib>=2.2->seaborn) (1.4.2)\
Requirement already satisfied: cycler>=0.10 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from matplotlib>=2.2->seaborn) (0.11.0)\
Requirement already satisfied: pyparsing>=2.2.1 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from matplotlib>=2.2->seaborn) (3.0.4)\
Requirement already satisfied: python-dateutil>=2.7 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from matplotlib>=2.2->seaborn) (2.8.2)\
Requirement already satisfied: packaging>=20.0 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from matplotlib>=2.2->seaborn) (21.3)\
Requirement already satisfied: fonttools>=4.22.0 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from matplotlib>=2.2->seaborn) (4.25.0)\
Requirement already satisfied: pillow>=6.2.0 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from matplotlib>=2.2->seaborn) (9.0.1)\
Requirement already satisfied: typing-extensions in c:\\users\82103\.conda\envs\test1\lib\site-packages (from kiwisolver>=1.0.1->matplotlib>=2.2->seaborn) (4.1.1)\
Requirement already satisfied: pytz>=2017.3 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from pandas>=0.23->seaborn) (2021.3)\
Requirement already satisfied: six>=1.5 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from python-dateutil>=2.7->matplotlib>=2.2->seaborn) (1.16.0)"
    )
 