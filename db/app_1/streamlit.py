# -*- coding: utf-8 -*-
import streamlit as st

def app():
	st.write("Collecting streamlit\
  Downloading streamlit-1.9.2-py2.py3-none-any.whl (10.1 MB)\
     |████████████████████████████████| 10.1 MB 6.4 MB/s\
Requirement already satisfied: click<8.1,>=7.0 in c:\\programdata\\anaconda3\\lib\site-packages (from streamlit) (8.0.3)\
Requirement already satisfied: numpy in c:\\programdata\\anaconda3\\lib\site-packages (from streamlit) (1.20.3)\
Requirement already satisfied: python-dateutil in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (2.8.2)\
Requirement already satisfied: importlib-metadata>=1.4 in c:\\programdata\\anaconda3\\lib\site-packages (from streamlit) (4.8.1)\
Requirement already satisfied: attrs in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (21.2.0)\
Collecting pydeck>=0.1.dev5\
  Using cached pydeck-0.7.1-py2.py3-none-any.whl (4.3 MB)\
Requirement already satisfied: requests in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (2.26.0)\
Requirement already satisfied: pandas>=0.21.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (1.3.4)\
Collecting blinker\
  Downloading blinker-1.4.tar.gz (111 kB)\
     |████████████████████████████████| 111 kB 6.4 MB/s\
Requirement already satisfied: packaging in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (21.0)\
Collecting pympler>=0.9\
  Using cached Pympler-1.0.1-py3-none-any.whl (164 kB)\
Collecting validators\
  Using cached validators-0.19.0.tar.gz (30 kB)\
Collecting pyarrow\
  Downloading pyarrow-8.0.0-cp39-cp39-win_amd64.whl (17.9 MB)\
     |████████████████████████████████| 17.9 MB ...\
Collecting altair>=3.2.0\
  Using cached altair-4.2.0-py3-none-any.whl (812 kB)\
Collecting tzlocal\
  Using cached tzlocal-4.2-py3-none-any.whl (19 kB)\
Requirement already satisfied: typing-extensions in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (3.10.0.2)\
Requirement already satisfied: tornado>=5.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (6.1)\
Collecting protobuf<4,>=3.12\
  Downloading protobuf-3.20.1-cp39-cp39-win_amd64.whl (904 kB)\
     |████████████████████████████████| 904 kB ...\
Collecting semver\
  Using cached semver-2.13.0-py2.py3-none-any.whl (12 kB)\
Requirement already satisfied: toml in c:\\programdata\\anaconda3\\lib\site-packages (from streamlit) (0.10.2)\
Requirement already satisfied: pillow>=6.2.0 in c:\\programdata\\anaconda3\lib\\site-packages (from streamlit) (8.4.0)\
Collecting cachetools>=4.0\
  Downloading cachetools-5.2.0-py3-none-any.whl (9.3 kB)\
Requirement already satisfied: watchdog in c:\\programdata\\anaconda3\\lib\\site-packages (from streamlit) (2.1.3)\
Collecting gitpython!=3.1.19\
  Using cached GitPython-3.1.27-py3-none-any.whl (181 kB)\
Requirement already satisfied: entrypoints in c:\\programdata\\anaconda3\\lib\\site-packages (from altair>=3.2.0->streamlit) (0.3)\
Requirement already satisfied: jinja2 in c:\\programdata\anaconda3\\lib\site-packages (from altair>=3.2.0->streamlit) (2.11.3)\
Requirement already satisfied: toolz in c:\\programdata\anaconda3\\lib\site-packages (from altair>=3.2.0->streamlit) (0.11.1)\
Requirement already satisfied: jsonschema>=3.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from altair>=3.2.0->streamlit) (3.2.0)\
Requirement already satisfied: colorama in c:\\programdata\anaconda3\\lib\\site-packages (from click<8.1,>=7.0->streamlit) (0.4.4)\
Collecting gitdb<5,>=4.0.1\
  Using cached gitdb-4.0.9-py3-none-any.whl (63 kB)\
Collecting smmap<6,>=3.0.1\
  Using cached smmap-5.0.0-py3-none-any.whl (24 kB)\
Requirement already satisfied: zipp>=0.5 in c:\\programdata\anaconda3\lib\site-packages (from importlib-metadata>=1.4->streamlit) (3.6.0)\
Requirement already satisfied: six>=1.11.0 in c:\\programdata\anaconda3\lib\site-packages (from jsonschema>=3.0->altair>=3.2.0->streamlit) (1.16.0)\
Requirement already satisfied: pyrsistent>=0.14.0 in c:\\programdata\anaconda3\lib\site-packages (from jsonschema>=3.0->altair>=3.2.0->streamlit) (0.18.0)\
Requirement already satisfied: setuptools in c:\\programdata\anaconda3\lib\site-packages (from jsonschema>=3.0->altair>=3.2.0->streamlit) (58.0.4)\
Requirement already satisfied: pytz>=2017.3 in c:\\programdata\anaconda3\lib\site-packages (from pandas>=0.21.0->streamlit) (2021.3)\
Requirement already satisfied: traitlets>=4.3.2 in c:\\programdata\anaconda3\lib\site-packages (from pydeck>=0.1.dev5->streamlit) (5.1.0)\
Requirement already satisfied: ipywidgets>=7.0.0 in c:\\programdata\anaconda3\lib\site-packages (from pydeck>=0.1.dev5->streamlit) (7.6.5)\
Requirement already satisfied: ipykernel>=5.1.2 in c:\\programdata\anaconda3\lib\site-packages (from pydeck>=0.1.dev5->streamlit) (6.4.1)\
Requirement already satisfied: matplotlib-inline<0.2.0,>=0.1.0 in c:\\programdata\anaconda3\lib\site-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.1.2)\
Requirement already satisfied: ipython-genutils in c:\\programdata\anaconda3\lib\site-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.2.0)\
Requirement already satisfied: ipython<8.0,>=7.23.1 in c:\\programdata\anaconda3\lib\site-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (7.29.0)\
Requirement already satisfied: debugpy<2.0,>=1.0.0 in c:\\programdata\anaconda3\lib\site-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (1.4.1)\
Requirement already satisfied: jupyter-client<8.0 in c:\\programdata\anaconda3\lib\site-packages (from ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (6.1.12)\
Requirement already satisfied: backcall in c:\\programdata\anaconda3\lib\site-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.2.0)\
Requirement already satisfied: pickleshare in c:\\programdata\anaconda3\lib\site-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.7.5)\
Requirement already satisfied: pygments in c:\\programdata\anaconda3\lib\site-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (2.10.0)\
Requirement already satisfied: jedi>=0.16 in c:\\programdata\anaconda3\lib\site-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.18.0)\
Requirement already satisfied: prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0 in c:\\programdata\anaconda3\lib\site-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (3.0.20)\
Requirement already satisfied: decorator in c:\\programdata\anaconda3\lib\site-packages (from ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (5.1.0)\
Requirement already satisfied: nbformat>=4.2.0 in c:\\\anaconda3\lib\site-packages (from ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (5.1.3)\
Requirement already satisfied: jupyterlab-widgets>=1.0.0 in c:\\programdata\anaconda3\lib\site-packages (from ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (1.0.0)\
Requirement already satisfied: widgetsnbextension~=3.5.0 in c:\\programdata\anaconda3\lib\site-packages (from ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (3.5.1)\
Requirement already satisfied: parso<0.9.0,>=0.8.0 in c:\\programdata\anaconda3\lib\site-packages (from jedi>=0.16->ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.8.2)\
Requirement already satisfied: MarkupSafe>=0.23 in c:\\programdata\anaconda3\lib\site-packages (from jinja2->altair>=3.2.0->streamlit) (1.1.1)\
Requirement already satisfied: jupyter-core>=4.6.0 in c:\\programdata\anaconda3\lib\site-packages (from jupyter-client<8.0->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (4.8.1)\
Requirement already satisfied: pyzmq>=13 in c:\\programdata\anaconda3\lib\site-packages (from jupyter-client<8.0->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (22.2.1)\
Requirement already satisfied: pywin32>=1.0 in c:\\programdata\anaconda3\lib\site-packages (from jupyter-core>=4.6.0->jupyter-client<8.0->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (228)\
Requirement already satisfied: wcwidth in c:\\programdata\anaconda3\lib\site-packages (from prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0->ipython<8.0,>=7.23.1->ipykernel>=5.1.2->pydeck>=0.1.dev5->streamlit) (0.2.5)\
Requirement already satisfied: notebook>=4.4.1 in c:\\programdata\anaconda3\lib\site-packages (from widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (6.4.5)\
Requirement already satisfied: prometheus-client in c:\\programdata\anaconda3\lib\site-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.11.0)\
Requirement already satisfied: terminado>=0.8.3 in c:\\programdata\anaconda3\lib\site-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.9.4)\
Requirement already satisfied: argon2-cffi in c:\\programdata\anaconda3\lib\site-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (20.1.0)\
Requirement already satisfied: nbconvert in c:\\programdata\anaconda3\lib\site-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (6.1.0)\
Requirement already satisfied: Send2Trash>=1.5.0 in c:\\programdata\anaconda3\lib\site-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (1.8.0)\
Requirement already satisfied: pywinpty>=0.5 in c:\\programdata\anaconda3\lib\site-packages (from terminado>=0.8.3->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.5.7)\
Requirement already satisfied: cffi>=1.0.0 in c:\\programdata\anaconda3\lib\site-packages (from argon2-cffi->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (1.14.6)\
Requirement already satisfied: pycparser in c:\\programdata\anaconda3\lib\site-packages (from cffi>=1.0.0->argon2-cffi->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (2.20)\
Requirement already satisfied: nbclient<0.6.0,>=0.5.0 in c:\\programdata\anaconda3\lib\site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.5.3)\
Requirement already satisfied: jupyterlab-pygments in c:\\programdata\anaconda3\lib\site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.1.2)\
Requirement already satisfied: bleach in c:\programdata\anaconda3\lib\site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (4.0.0)\
Requirement already satisfied: mistune<2,>=0.8.1 in c:\\programdata\anaconda3\lib\site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.8.4)\
Requirement already satisfied: defusedxml in c:\\programdata\anaconda3\lib\site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.7.1)\
Requirement already satisfied: pandocfilters>=1.4.1 in c:\\programdata\anaconda3\lib\site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (1.4.3)\
Requirement already satisfied: testpath in c:\\programdata\anaconda3\lib\site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.5.0)\
Requirement already satisfied: async-generator in c:\\programdata\anaconda3\lib\site-packages (from nbclient<0.6.0,>=0.5.0->nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (1.10)\
Requirement already satisfied: nest-asyncio in c:\\programdata\anaconda3\lib\site-packages (from nbclient<0.6.0,>=0.5.0->nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (1.5.1)\
Requirement already satisfied: webencodings in c:\\programdata\anaconda3\lib\site-packages (from bleach->nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->pydeck>=0.1.dev5->streamlit) (0.5.1)\
Requirement already satisfied: pyparsing>=2.0.2 in c:\\programdata\anaconda3\lib\site-packages (from packaging->streamlit) (3.0.4)\
Requirement already satisfied: certifi>=2017.4.17 in c:\\programdata\anaconda3\lib\site-packages (from requests->streamlit) (2021.10.8)\
Requirement already satisfied: charset-normalizer~=2.0.0 in c:\\programdata\anaconda3\lib\site-packages (from requests->streamlit) (2.0.4)\
Requirement already satisfied: idna<4,>=2.5 in c:\\programdata\anaconda3\lib\site-packages (from requests->streamlit) (3.2)\
Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\\programdata\anaconda3\lib\site-packages (from requests->streamlit) (1.26.7)\
Collecting tzdata\
  Using cached tzdata-2022.1-py2.py3-none-any.whl (339 kB)\
Collecting pytz-deprecation-shim\
  Using cached pytz_deprecation_shim-0.1.0.post0-py2.py3-none-any.whl (15 kB)\
Building wheels for collected packages: blinker, validators\
  Building wheel for blinker (setup.py) ... done\
  Created wheel for blinker: filename=blinker-1.4-py3-none-any.whl size=13478 sha256=ff00b932120f678033d1f7b2294bfad8ab37d0cecfd81a74872444ba0122f17e\
  Stored in directory: c:\\users\\82103\\appdata\\local\\pip\\cache\wheels\\50\\93\\f8\\\
      4f0a42a03a06626d675f13907b6982ad5ecff383530af5a900\
  Building wheel for validators (setup.py) ... done\
  Created wheel for validators: filename=validators-0.19.0-py3-none-any.whl size=19552 sha256=e4b83e6b57234521c0ab0e82e2bbe94a656a97538086935c9bc316c82efb69a8\
  Stored in directory: c\\users\\82103\\appdata\\local\\pip\\cache\\wheels\\63\\96\\60\\\
      01b2d5e1cb69cb88e19141a8e39e2992454ba62dbb72c849c8\
Successfully built blinker validators\
Installing collected packages: tzdata, smmap, pytz-deprecation-shim, gitdb, validators, tzlocal, semver, pympler, pydeck, pyarrow, protobuf, gitpython, cachetools, blinker, altair, streamlit\
Successfully installed altair-4.2.0 blinker-1.4 cachetools-5.2.0 gitdb-4.0.9 gitpython-3.1.27\
 protobuf-3.20.1 pyarrow-8.0.0 pydeck-0.7.1 pympler-1.0.1 pytz-deprecation-shim-0.1.0.post0 semver-2.13.0 smmap-5.0.0 streamlit-1.9.2 tzdata-2022.1 tzlocal-4.2 validators-0.19.0"
 )