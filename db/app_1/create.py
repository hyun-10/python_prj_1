# -*- coding: utf-8 -*-
import streamlit as st
def app():
    
	st.write("Collecting package metadata (current_repodata.json): done\
Solving environment: failed with repodata from current_repodata.json, will retry with next repodata source.\
Collecting package metadata (repodata.json): done\
Solving environment: failed\
PackagesNotFoundError: The following packages are not available from current channels:\
- trnsorflow\
- npmpy\
    Current channels:\
- https://repo.anaconda.com/pkgs/main/win-64\
- https://repo.anaconda.com/pkgs/main/noarch\
- https://repo.anaconda.com/pkgs/r/win-64\
- https://repo.anaconda.com/pkgs/r/noarch\
- https://repo.anaconda.com/pkgs/msys2/win-64\
- https://repo.anaconda.com/pkgs/msys2/noarch\
To search for alternate channels that may provide the conda package you're\
looking for, navigate to\
https://anaconda.org\
and use the search bar at the top of the page\
(base) PS C:\\Users\\82103> conda create -n test python=3.7.4 ipython numpy matplotlib pandas scipy scikit-learn tensorflow keras\
The following NEW packages will be INSTALLED\
Collecting package metadata (current_repodata.json): done\
Solving environment: failed with repodata from current_repodata.json, will retry with next repodata source.\
Collecting package metadata (repodata.json): done\
Solving environment: done\
==> WARNING: A newer version of conda exists. <==\
  current version: 4.10.3\
  latest version: 4.13.0\
Please update conda by running\
    $ conda update -n base -c defaults conda\
## Package Plan ##\
  environment location: C:\\Users\\82103\\.conda\\envs\\test\
\
  added / updated specs:\
- ipython\
- keras\
- matplotlib\
- numpy\
- pandas\
- python=3.7.4\
- scikit-learn\
- scipy\
- tensorflow\
\   \
The following packages will be downloaded:\
\
    package                    |            build\
    ---------------------------|-----------------\
    numpy-1.21.5               |   py37h7a0a035_3          25 KB\
    numpy-base-1.21.5          |   py37hca35cd5_3         4.4 MB\
    tk-8.6.12                  |       h2bbff1b_0         3.1 MB\
    ------------------------------------------------------------\
                                           Total:         7.5 MB\
\
The following NEW packages will be INSTALLED:\
  _tflow_select      pkgs/main/win-64::_tflow_select-2.3.0-eigen\
  absl-py            pkgs/main/noarch::absl-py-0.15.0-pyhd3eb1b0_0\
  aiohttp            pkgs/main/win-64::aiohttp-3.8.1-py37h2bbff1b_1\
  aiosignal          pkgs/main/noarch::aiosignal-1.2.0-pyhd3eb1b0_0\
  astor              pkgs/main/win-64::astor-0.8.1-py37haa95532_0\
  astunparse         pkgs/main/noarch::astunparse-1.6.3-py_0\
  async-timeout      pkgs/main/noarch::async-timeout-4.0.1-pyhd3eb1b0_0\
  asynctest          pkgs/main/noarch::asynctest-0.13.0-py_0\
  attrs              pkgs/main/noarch::attrs-21.4.0-pyhd3eb1b0_0\
  backcall           pkgs/main/noarch::backcall-0.2.0-pyhd3eb1b0_0\
  blas               pkgs/main/win-64::blas-1.0-mkl\
  blinker            pkgs/main/win-64::blinker-1.4-py37haa95532_0\
  bottleneck         pkgs/main/win-64::bottleneck-1.3.4-py37h080aedc_0\
  brotli             pkgs/main/win-64::brotli-1.0.9-ha925a31_2\
  brotlipy           pkgs/main/win-64::brotlipy-0.7.0-py37h2bbff1b_1003\
  ca-certificates    pkgs/main/win-64::ca-certificates-2022.4.26-haa95532_0\
  cachetools         pkgs/main/noarch::cachetools-4.2.2-pyhd3eb1b0_0\
  certifi            pkgs/main/win-64::certifi-2022.5.18.1-py37haa95532_0\
  cffi               pkgs/main/win-64::cffi-1.15.0-py37h2bbff1b_1\
  charset-normalizer pkgs/main/noarch::charset-normalizer-2.0.4-pyhd3eb1b0_0\
  click              pkgs/main/win-64::click-8.0.4-py37haa95532_0\
  colorama           pkgs/main/noarch::colorama-0.4.4-pyhd3eb1b0_0\
  cryptography       pkgs/main/win-64::cryptography-3.4.8-py37h71e12ea_0\
  cycler             pkgs/main/noarch::cycler-0.11.0-pyhd3eb1b0_0\
  dataclasses        pkgs/main/noarch::dataclasses-0.8-pyh6d0b6a4_7\
  decorator          pkgs/main/noarch::decorator-5.1.1-pyhd3eb1b0_0\
  fonttools          pkgs/main/noarch::fonttools-4.25.0-pyhd3eb1b0_0\
  freetype           pkgs/main/win-64::freetype-2.10.4-hd328e21_0\
  frozenlist         pkgs/main/win-64::frozenlist-1.2.0-py37h2bbff1b_0\
  gast               pkgs/main/noarch::gast-0.3.3-py_0\
  google-auth        pkgs/main/noarch::google-auth-2.6.0-pyhd3eb1b0_0\
  google-auth-oauth~ pkgs/main/noarch::google-auth-oauthlib-0.4.4-pyhd3eb1b0_0\
  google-pasta       pkgs/main/noarch::google-pasta-0.2.0-pyhd3eb1b0_0\
  grpcio             pkgs/main/win-64::grpcio-1.42.0-py37hc60d5dd_0\
  h5py               pkgs/main/win-64::h5py-2.10.0-py37h5e291fa_0\
  hdf5               pkgs/main/win-64::hdf5-1.10.4-h7ebc959_0\
  icc_rt             pkgs/main/win-64::icc_rt-2019.0.0-h0cc432a_1\
  icu                pkgs/main/win-64::icu-58.2-ha925a31_3\
  idna               pkgs/main/noarch::idna-3.3-pyhd3eb1b0_0\
  importlib-metadata pkgs/main/win-64::importlib-metadata-4.11.3-py37haa95532_0\
  intel-openmp       pkgs/main/win-64::intel-openmp-2021.4.0-haa95532_3556\
  ipython            pkgs/main/win-64::ipython-7.31.1-py37haa95532_0\
  jedi               pkgs/main/win-64::jedi-0.18.1-py37haa95532_1\
  joblib             pkgs/main/noarch::joblib-1.1.0-pyhd3eb1b0_0\
  jpeg               pkgs/main/win-64::jpeg-9e-h2bbff1b_0\
  keras              pkgs/main/noarch::keras-2.4.3-hd3eb1b0_0\
  keras-applications pkgs/main/noarch::keras-applications-1.0.8-py_1\
  keras-base         pkgs/main/noarch::keras-base-2.4.3-pyhd3eb1b0_0\
  keras-preprocessi~ pkgs/main/noarch::keras-preprocessing-1.1.2-pyhd3eb1b0_0\
  kiwisolver         pkgs/main/win-64::kiwisolver-1.4.2-py37hd77b12b_0\
  libpng             pkgs/main/win-64::libpng-1.6.37-h2a8f88b_0\
  libprotobuf        pkgs/main/win-64::libprotobuf-3.20.1-h23ce68f_0\
  libtiff            pkgs/main/win-64::libtiff-4.2.0-he0120a3_1\
  libwebp            pkgs/main/win-64::libwebp-1.2.2-h2bbff1b_0\
  lz4-c              pkgs/main/win-64::lz4-c-1.9.3-h2bbff1b_1\
  markdown           pkgs/main/win-64::markdown-3.3.4-py37haa95532_0\
  matplotlib         pkgs/main/win-64::matplotlib-3.5.1-py37haa95532_1\
  matplotlib-base    pkgs/main/win-64::matplotlib-base-3.5.1-py37hd77b12b_1\
  matplotlib-inline  pkgs/main/noarch::matplotlib-inline-0.1.2-pyhd3eb1b0_2\
  mkl                pkgs/main/win-64::mkl-2021.4.0-haa95532_640\
  mkl-service        pkgs/main/win-64::mkl-service-2.4.0-py37h2bbff1b_0\
  mkl_fft            pkgs/main/win-64::mkl_fft-1.3.1-py37h277e83a_0\
  mkl_random         pkgs/main/win-64::mkl_random-1.2.2-py37hf11a4ad_0\
  multidict          pkgs/main/win-64::multidict-5.1.0-py37h2bbff1b_2\
  munkres            pkgs/main/noarch::munkres-1.1.4-py_0\
  numexpr            pkgs/main/win-64::numexpr-2.8.1-py37hb80d3ca_0\
  numpy              pkgs/main/win-64::numpy-1.21.5-py37h7a0a035_2\
  numpy-base         pkgs/main/win-64::numpy-base-1.21.5-py37hca35cd5_2\
  oauthlib           pkgs/main/noarch::oauthlib-3.2.0-pyhd3eb1b0_0\
  openssl            pkgs/main/win-64::openssl-1.1.1o-h2bbff1b_0\
  opt_einsum         pkgs/main/noarch::opt_einsum-3.3.0-pyhd3eb1b0_1\
  packaging          pkgs/main/noarch::packaging-21.3-pyhd3eb1b0_0\
  pandas             pkgs/main/win-64::pandas-1.3.5-py37h6214cd6_0\
  parso              pkgs/main/noarch::parso-0.8.3-pyhd3eb1b0_0\
  pickleshare        pkgs/main/noarch::pickleshare-0.7.5-pyhd3eb1b0_1003\
  pillow             pkgs/main/win-64::pillow-9.0.1-py37hdc2b20a_0\
  pip                pkgs/main/win-64::pip-21.2.4-py37haa95532_0\
  prompt-toolkit     pkgs/main/noarch::prompt-toolkit-3.0.20-pyhd3eb1b0_0\
  protobuf           pkgs/main/win-64::protobuf-3.20.1-py37hd77b12b_0\
  pyasn1             pkgs/main/noarch::pyasn1-0.4.8-pyhd3eb1b0_0\
  pyasn1-modules     pkgs/main/noarch::pyasn1-modules-0.2.8-py_0\
  pycparser          pkgs/main/noarch::pycparser-2.21-pyhd3eb1b0_0\
  pygments           pkgs/main/noarch::pygments-2.11.2-pyhd3eb1b0_0\
  pyjwt              pkgs/main/win-64::pyjwt-2.1.0-py37haa95532_0\
  pyopenssl          pkgs/main/noarch::pyopenssl-21.0.0-pyhd3eb1b0_1\
  pyparsing          pkgs/main/noarch::pyparsing-3.0.4-pyhd3eb1b0_0\
  pyqt               pkgs/main/win-64::pyqt-5.9.2-py37hd77b12b_6\
  pyreadline         pkgs/main/win-64::pyreadline-2.1-py37_1\
  pysocks            pkgs/main/win-64::pysocks-1.7.1-py37_1\
  python             pkgs/main/win-64::python-3.7.4-h5263a28_0\
  python-dateutil    pkgs/main/noarch::python-dateutil-2.8.2-pyhd3eb1b0_0\
  pytz               pkgs/main/noarch::pytz-2021.3-pyhd3eb1b0_0\
  pyyaml             pkgs/main/win-64::pyyaml-6.0-py37h2bbff1b_1\
  qt                 pkgs/main/win-64::qt-5.9.7-vc14h73c81de_0\
  requests           pkgs/main/noarch::requests-2.27.1-pyhd3eb1b0_0\
  requests-oauthlib  pkgs/main/noarch::requests-oauthlib-1.3.0-py_0\
  rsa                pkgs/main/noarch::rsa-4.7.2-pyhd3eb1b0_1\
  scikit-learn       pkgs/main/win-64::scikit-learn-1.0.2-py37hf11a4ad_1\
  scipy              pkgs/main/win-64::scipy-1.7.3-py37h0a974cb_0\
  setuptools         pkgs/main/win-64::setuptools-61.2.0-py37haa95532_0\
  sip                pkgs/main/win-64::sip-4.19.13-py37hd77b12b_0\
  six                pkgs/main/noarch::six-1.16.0-pyhd3eb1b0_1\
  sqlite             pkgs/main/win-64::sqlite-3.38.3-h2bbff1b_0\
  tensorboard        pkgs/main/noarch::tensorboard-2.4.0-pyhc547734_0\
  tensorboard-plugi~ pkgs/main/noarch::tensorboard-plugin-wit-1.6.0-py_0\
  tensorflow         pkgs/main/win-64::tensorflow-2.3.0-mkl_py37h04bc1aa_0\
  tensorflow-base    pkgs/main/win-64::tensorflow-base-2.3.0-eigen_py37h17acbac_0\
  tensorflow-estima~ pkgs/main/noarch::tensorflow-estimator-2.6.0-pyh7b7c402_0\
  termcolor          pkgs/main/win-64::termcolor-1.1.0-py37haa95532_1\
  threadpoolctl      pkgs/main/noarch::threadpoolctl-2.2.0-pyh0d69192_0\
  tk                 pkgs/main/win-64::tk-8.6.11-h2bbff1b_1\
  tornado            pkgs/main/win-64::tornado-6.1-py37h2bbff1b_0\
  traitlets          pkgs/main/noarch::traitlets-5.1.1-pyhd3eb1b0_0\
  typing-extensions  pkgs/main/noarch::typing-extensions-4.1.1-hd3eb1b0_0\
  typing_extensions  pkgs/main/noarch::typing_extensions-4.1.1-pyh06a4308_0\
  urllib3            pkgs/main/win-64::urllib3-1.26.9-py37haa95532_0\
  vc                 pkgs/main/win-64::vc-14.2-h21ff451_1\
  vs2015_runtime     pkgs/main/win-64::vs2015_runtime-14.27.29016-h5e58377_2\
  wcwidth            pkgs/main/noarch::wcwidth-0.2.5-pyhd3eb1b0_0\
  werkzeug           pkgs/main/noarch::werkzeug-2.0.3-pyhd3eb1b0_0\
  wheel              pkgs/main/noarch::wheel-0.37.1-pyhd3eb1b0_0\
  win_inet_pton      pkgs/main/win-64::win_inet_pton-1.1.0-py37haa95532_0\
  wincertstore       pkgs/main/win-64::wincertstore-0.2-py37haa95532_2\
  wrapt              pkgs/main/win-64::wrapt-1.13.3-py37h2bbff1b_2\
  xz                 pkgs/main/win-64::xz-5.2.5-h8cc25b3_1\
  yaml               pkgs/main/win-64::yaml-0.2.5-he774522_0\
  yarl               pkgs/main/win-64::yarl-1.6.3-py37h2bbff1b_0\
  zipp               pkgs/main/win-64::zipp-3.8.0-py37haa95532_0\
  zlib               pkgs/main/win-64::zlib-1.2.12-h8cc25b3_2\
  zstd               pkgs/main/win-64::zstd-1.5.2-h19a0ad4_0\
      \
Proceed ([y]/n)?"
)