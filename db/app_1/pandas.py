# -*- coding: utf-8 -*-
import streamlit as st

def app():
	st.write("Collecting streamlit\
  Using cached streamlit-1.9.2-py2.py3-none-any.whl (10.1 MB)\
Requirement already satisfied: click<8.1,>=7.0 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from streamlit) (8.0.4)\
Requirement already satisfied: packaging in c:\\users\82103\.conda\envs\test1\lib\site-packages (from streamlit) (21.3)\
Requirement already satisfied: pandas>=0.21.0 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from streamlit) (1.3.5)\
Requirement already satisfied: typing-extensions in c:\\users\82103\.conda\envs\test1\lib\site-packages (from streamlit) (4.1.1)\
Collecting semver\
  Using cached semver-2.13.0-py2.py3-none-any.whl (12 kB)\
Requirement already satisfied: importlib-metadata>=1.4 in c:\\users\\82103\.conda\envs\test1\lib\site-packages (from streamlit) (4.11.3)\
Requirement already satisfied: blinker in c:\\users\82103\\.conda\envs\test1\lib\site-packages (from streamlit) (1.4)\
Collecting altair>=3.2.0\
  Using cached altair-4.2.0-py3-none-any.whl (812 kB)\
Requirement already satisfied: python-dateutil in c:\\users\82103\.conda\envs\test1\lib\site-packages (from streamlit) (2.8.2)\
Collecting tzlocal\
  Using cached tzlocal-4.2-py3-none-any.whl (19 kB)\
Collecting toml\
  Using cached toml-0.10.2-py2.py3-none-any.whl (16 kB)\
Collecting pympler>=0.9\
  Using cached Pympler-1.0.1\-py3-none-any.whl (164 kB)\
Requirement already satisfied: pillow>=6.2.0 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from streamlit) (9.0.1)\
Requirement already satisfied: tornado>=5.0 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from streamlit) (6.1)\
Collecting pydeck>=0.1.dev5\
  Using cached pydeck-0.7.1-py2.py3-none-any.whl (4.3 MB)\
Requirement already satisfied: cachetools>=4.0 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from streamlit) (4.2.2)\
Requirement already satisfied: protobuf<4,>=3.12 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from streamlit) (3.20.1)\
Requirement already satisfied: requests in c:\\users\82103\.conda\envs\test1\lib\site-packages (from streamlit) (2.27.1)\
Collecting validators\
  Using cached validators-0.19.0-py3-none-any.whl\
Requirement already satisfied: numpy in c:\\users\82103\.conda\envs\test1\lib\site-packages (from streamlit) (1.21.5)\
Collecting watchdog\
  Using cached watchdog-2.1.8-py3-none-win_amd64.whl (77 kB)\
Collecting gitpython!=3.1.19\
  Using cached GitPython-3.1.27-py3-none-any.whl (181 kB)\
Collecting pyarrow\
  Using cached pyarrow-8.0.0-cp37-cp37m-win_amd64.whl (17.8 MB)\
Requirement already satisfied: attrs in c:\\users\82103\.conda\envs\test1\lib\site-packages (from streamlit) (21.4.0)\
Collecting toolz\
  Using cached toolz-0.11.2-py3-none-any.whl (55 kB)\
Collecting jsonschema>=3.0\
  Downloading jsonschema-4.6.0-py3-none-any.whl (80 kB)\
     |████████████████████████████████| 80 kB 2.6 MB/s\
Collecting jinja2\
  Using cached Jinja2-3.1.2-py3-none-any.whl (133 kB)\
Collecting entrypoints\
  Using cached entrypoints-0.4-py3-none-any.whl (5.3 kB)\
Requirement already satisfied: colorama in c:\\users\82103\.conda\envs\test1\lib\site-packages (from click<8.1,>=7.0->streamlit) (0.4.4)\
Collecting gitdb<5,>=4.0.1\
  Using cached gitdb-4.0.9-py3-none-any.whl (63 kB)\
Collecting smmap<6,>=3.0.1\
  Using cached smmap-5.0.0-py3-none-any.whl (24 kB)\
Requirement already satisfied: zipp>=0.5 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from importlib-metadata>=1.4->streamlit) (3.8.0)\
Collecting importlib-resources>=1.4.0\
  Using cached importlib_resources-5.7.1-py3-none-any.whl (28 kB)\
Collecting pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0\
  Using cached pyrsistent-0.18.1-cp37-cp37m-win_amd64.whl (61 kB)\
Requirement already satisfied: pytz>=2017.3 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from pandas>=0.21.0->streamlit) (2021.3)\
Requirement already satisfied: traitlets>=4.3.2 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from pydeck>=0.1.dev5->streamlit) (5.1.1)\
Collecting ipykernel>=5.1.2\
  Using cached ipykernel-6.13.0-py3-none-any.whl (131 kB)\
Collecting ipywidgets>=7.0.0\
  Using cached ipywidgets-7.7.0-py2.py3-none-any.whl (123 kB)\
Collecting jupyter-client>=6.1.12\
  Using cached jupyter_client-7.3.1-py3-none-any.whl (130 kB)\
Collecting psutil\
  Using cached psutil-5.9.1-cp37-cp37m-win_amd64.whl (246 kB)\
Collecting nest-asyncio\
  Using cached nest_asyncio-1.5.5-py3-none-any.whl (5.2 kB)\
Requirement already satisfied: ipython>=7.23.1 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (7.31.1)\
Collecting debugpy>=1.0\
  Using cached debugpy-1.6.0-cp37-cp37m-win_amd64.whl (4.3 MB)\
Requirement already satisfied: matplotlib-inline>=0.1 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.1.2)\
Requirement already satisfied: pygments in c:\\users\82103\.conda\envs\test1\lib\site-packages (from ipython>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (2.11.2)\
Requirement already satisfied: setuptools>=18.5 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from ipython>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (61.2.0)\
Requirement already satisfied: decorator in c:\\users\82103\.conda\envs\test1\lib\site-packages (from ipython>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (5.1.1)\
Requirement already satisfied: jedi>=0.16 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from ipython>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.18.1)\
Requirement already satisfied: backcall in c:\\users\82103\.conda\envs\test1\lib\site-packages (from ipython>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.2.0)\
Requirement already satisfied: prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from ipython>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (3.0.20)\
Requirement already satisfied: pickleshare in c:\\users\82103\.conda\envs\test1\lib\site-packages (from ipython>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.7.5)\
Collecting jupyterlab-widgets>=1.0.0\
  Using cached jupyterlab_widgets-1.1.0-py3-none-any.whl (245 kB)\
Collecting ipython-genutils~=0.2.0\
  Using cached ipython_genutils-0.2.0-py2.py3-none-any.whl (26 kB)\
Collecting widgetsnbextension~=3.6.0\
  Using cached widgetsnbextension-3.6.0-py2.py3-none-any.whl (1.6 MB)\
Collecting nbformat>=4.2.0\
  Using cached nbformat-5.4.0-py3-none-any.whl (73 kB)\
Requirement already satisfied: parso<0.9.0,>=0.8.0 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from jedi>=0.16->ipython>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.8.3)\
Collecting MarkupSafe>=2.0\
  Using cached MarkupSafe-2.1.1-cp37-cp37m-win_amd64.whl (17 kB)\
Collecting jupyter-core>=4.9.2\
  Using cached jupyter_core-4.10.0-py3-none-any.whl (87 kB)\
Collecting pyzmq>=22.3\
  Using cached pyzmq-23.0.0-cp37-cp37m-win_amd64.whl (1.0 MB)\
Collecting pywin32>=1.0\
  Using cached pywin32-304-cp37-cp37m-win_amd64.whl (12.2 MB)\
Collecting fastjsonschema\
  Using cached fastjsonschema-2.15.3-py3-none-any.whl (22 kB)\
Requirement already satisfied: wcwidth in c:\\users\82103\.conda\envs\test1\lib\site-packages (from prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0->ipython>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.2.5)\
Requirement already satisfied: six>=1.5 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from python-dateutil->streamlit) (1.16.0)\
Collecting notebook>=4.4.1\
  Using cached notebook-6.4.11-py3-none-any.whl (9.9 MB)\
Collecting nbconvert>=5\
  Using cached nbconvert-6.5.0-py3-none-any.whl (561 kB)\
Collecting Send2Trash>=1.8.0\
  Using cached Send2Trash-1.8.0-py3-none-any.whl (18 kB)\
Collecting terminado>=0.8.3\
  Using cached terminado-0.15.0-py3-none-any.whl (16 kB)\
Collecting argon2-cffi\
  Using cached argon2_cffi-21.3.0-py3-none-any.whl (14 kB)\
Collecting prometheus-client\
  Using cached prometheus_client-0.14.1-py3-none-any.whl (59 kB)\
Collecting mistune<2,>=0.8.1\
  Using cached mistune-0.8.4-py2.py3-none-any.whl (16 kB)\
Collecting tinycss2\
  Using cached tinycss2-1.1.1-py3-none-any.whl (21 kB)\
Collecting defusedxml\
  Using cached defusedxml-0.7.1-py2.py3-none-any.whl (25 kB)\
Collecting nbclient>=0.5.0\
  Downloading nbclient-0.6.4-py3-none-any.whl (71 kB)\
     |████████████████████████████████| 71 kB 5.1 MB/s\
Collecting beautifulsoup4\
  Using cached beautifulsoup4-4.11.1-py3-none-any.whl (128 kB)\
Collecting pandocfilters>=1.4.1\
  Using cached pandocfilters-1.5.0-py2.py3-none-any.whl (8.7 kB)\
Collecting bleach\
  Using cached bleach-5.0.0-py3-none-any.whl (160 kB)\
Collecting jupyterlab-pygments\
  Using cached jupyterlab_pygments-0.2.2-py2.py3-none-any.whl (21 kB)\
Collecting traitlets>=4.3.2\
  Downloading traitlets-5.2.2.post1-py3-none-any.whl (106 kB)\
     |████████████████████████████████| 106 kB 6.4 MB/s\
Collecting pywinpty>=1.1.0\
  Using cached pywinpty-2.0.5-cp37-none-win_amd64.whl (1.4 MB)\
Collecting argon2-cffi-bindings\
  Using cached argon2_cffi_bindings-21.2.0-cp36-abi3-win_amd64.whl (30 kB)\
Requirement already satisfied: cffi>=1.0.1 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from argon2-cffi-bindings->argon2-cffi->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (1.15.0)\
Requirement already satisfied: pycparser in c:\\users\82103\.conda\envs\test1\lib\site-packages (from cffi>=1.0.1->argon2-cffi-bindings->argon2-cffi->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (2.21)\
Collecting soupsieve>1.2\
  Using cached soupsieve-2.3.2.post1-py3-none-any.whl (37 kB)\
Collecting webencodings\
  Using cached webencodings-0.5.1-py2.py3-none-any.whl (11 kB)\
Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from packaging->streamlit) (3.0.4)\
Requirement already satisfied: charset-normalizer~=2.0.0 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from requests->streamlit) (2.0.4)\
Requirement already satisfied: idna<4,>=2.5 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from requests->streamlit) (3.3)\
Requirement already satisfied: certifi>=2017.4.17 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from requests->streamlit) (2022.5.18.1)\
Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from requests->streamlit) (1.26.9)\
Collecting backports.zoneinfo\
  Using cached backports.zoneinfo-0.2.1-cp37-cp37m-win_amd64.whl (38 kB)\
Collecting tzdata\
  Using cached tzdata-2022.1-py2.py3-none-any.whl (339 kB)\
Collecting pytz-deprecation-shim\
  Using cached pytz_deprecation_shim-0.1.0.post0-py2.py3-none-any.whl (15 kB)\
Installing collected packages: traitlets, pywin32, pyrsistent, importlib-resources, pyzmq, nest-asyncio, jupyter-core, jsonschema, fastjsonschema, entrypoints, webencodings, soupsieve, nbformat, MarkupSafe, jupyter-client, tinycss2, pywinpty, psutil, pandocfilters, nbclient, mistune, jupyterlab-pygments, jinja2, defusedxml, debugpy, bleach, beautifulsoup4, argon2-cffi-bindings, terminado, Send2Trash, prometheus-client, nbconvert, ipython-genutils, ipykernel, argon2-cffi, notebook, widgetsnbextension, tzdata, smmap, jupyterlab-widgets, backports.zoneinfo, toolz, pytz-deprecation-shim, ipywidgets, gitdb, watchdog, validators, tzlocal, toml, semver, pympler, pydeck, pyarrow, gitpython, altair, streamlit\
  Attempting uninstall: traitlets\
    Found existing installation: traitlets 5.1.1\
    Uninstalling traitlets-5.1.1:\
      Successfully uninstalled traitlets-5.1.1\
Successfully installed MarkupSafe-2.1.1 Send2Trash-1.8.0 altair-4.2.0 argon2-cffi-21.3.0 argon2-cffi-bindings-21.2.0 backports.zoneinfo-0.2.1 beautifulsoup4-4.11.1 bleach-5.0.0 debugpy-1.6.0 defusedxml-0.7.1 entrypoints-0.4 fastjsonschema-2.15.3 gitdb-4.0.9 gitpython-3.1.27 importlib-resources-5.7.1 ipykernel-6.13.0 ipython-genutils-0.2.0 ipywidgets-7.7.0 jinja2-3.1.2 jsonschema-4.6.0 jupyter-client-7.3.1 jupyter-core-4.10.0 jupyterlab-pygments-0.2.2 jupyterlab-widgets-1.1.0 mistune-0.8.4 nbclient-0.6.4 nbconvert-6.5.0 nbformat-5.4.0 nest-asyncio-1.5.5 notebook-6.4.11 pandocfilters-1.5.0 prometheus-client-0.14.1 psutil-5.9.1 pyarrow-8.0.0 pydeck-0.7.1 pympler-1.0.1 pyrsistent-0.18.1 pytz-deprecation-shim-0.1.0.post0 pywin32-304 pywinpty-2.0.5 pyzmq-23.0.0 semver-2.13.0 smmap-5.0.0 soupsieve-2.3.2.post1 streamlit-1.9.2 terminado-0.15.0 tinycss2-1.1.1 toml-0.10.2 toolz-0.11.2 traitlets-5.2.2.post1 tzdata-2022.1 tzlocal-4.2 validators-0.19.0 watchdog-2.1.8 webencodings-0.5.1 widgetsnbextension-3.6.0\
(test1) PS C:\\Users\82103> pip install pandas_datareader\
Collecting pandas_datareader\
  Using cached pandas_datareader-0.10.0-py3-none-any.whl (109 kB)\
Requirement already satisfied: requests>=2.19.0 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from pandas_datareader) (2.27.1)\
Collecting lxml\
  Downloading lxml-4.9.0-cp37-cp37m-win_amd64.whl (3.6 MB)\
     |████████████████████████████████| 3.6 MB 6.8 MB/s\
Requirement already satisfied: pandas>=0.23 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from pandas_datareader) (1.3.5)\
Requirement already satisfied: numpy>=1.17.3 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from pandas>=0.23->pandas_datareader) (1.21.5)\
Requirement already satisfied: pytz>=2017.3 in c:\\users\82103\.conda\envs\test1\lib\site-packages (from pandas>=0.23->pandas_datareader) (2021.3)\
Requirement already satisfied: python-dateutil>=2.7.3 in c:\\users\\82103\\.conda\\envs\\test1\lib\\site-packages (from pandas>=0.23->pandas_datareader) (2.8.2)\
Requirement already satisfied: six>=1.5 in c:\\users\\82103\\.conda\\envs\\test1\\lib\\site-packages (from python-dateutil>=2.7.3->pandas>=0.23->pandas_datareader) (1.16.0)\
Requirement already satisfied: idna<4,>=2.5 in c:\\users\82103\.conda\envs\test1\\lib\\site-packages (from requests>=2.19.0->pandas_datareader) (3.3)\
Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\82103\\.conda\envs\\test1\\lib\\site-packages (from requests>=2.19.0->pandas_datareader) (2022.5.18.1)\
Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\\users\\82103\.conda\\envs\\test1\lib\\site-packages (from requests>=2.19.0->pandas_datareader) (1.26.9)\
Requirement already satisfied: charset-normalizer~=2.0.0 in c:\\users\\82103\.conda\envs\\test1\\lib\\site-packages (from requests>=2.19.0->pandas_datareader) (2.0.4)\
Installing collected packages: lxml, pandas-datareader\
Successfully installed lxml-4.9.0 pandas-datareader-0.10.0"
)