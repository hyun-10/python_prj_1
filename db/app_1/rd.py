# -*- coding: utf-8 -*-
import streamlit as st
def app():

    if st.checkbox("conda env list"):st.write("가상화면 조회.")
    if st.checkbox('conda create -n test1 python=3.7.4 ipython numpy matplotlib pands scipy scikit-learn tensorflow keras'):st.write("가상화면 및 라이브러리 설치")
    if st.checkbox("conda activate test1"):st.write("test1가상화면에 들어가기.")   
    if st.checkbox("conda deactivate"):st.write("현재가상화면에서 나가기.")    
    if st.checkbox("pip install streamlit"):st.write("파이썬 기반의 웹어플리케이션 라이브러리.")     
    
    if st.checkbox("pip install seaborn"):st.write("데이터의 시각화 라이브러리")
    
    if st.checkbox("pip install pandas_datareader"):st.write("데이터 분석 라이브러리")    
    
    if st.checkbox("pip install streamlit_forium"):st.write("지리정보 시각화 라이브러리")     
    
    if st.checkbox("pip install imageio_ffmpeg"):st.write("강화학습에서 나온 결과물을 비디오로 촬영해주는 라이브러리")

    if st.checkbox("pip freeze > requirements.txt"):st.write("설치한 패키지 목록")
    
    if st.checkbox("more .\requirements.txt"):st.write("설치한 모든 라이브러리 확인")    


