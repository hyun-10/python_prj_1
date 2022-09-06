
# -*- coding: utf-8 -*-

import streamlit as st
from db.app_3 import module
import plotly.express as px

def app():
    paths=db/app_3/*.csv
    name = st.sidebar.selectbox('자료', ['선택하세요','분자료','분자료 그래프'])
    name_ = st.sidebar.selectbox('자료', ['선택하세요','시간자료','일평균','일평균 그래프','월평균','월평균 그래프'])


    m_list = module.m_file(paths) #분자료

    (c,d,e,f,dff) = module.m_data(m_list) 


    if name =='선택하세요':
        ' '

    if name == '분자료':
        status = st.radio('자료를 선택하세요',['기온(°C)','단계검사','지속성검사','시간평균','전체'])
        if status =='기온(°C)':
            st.table(c)
        elif status == '단계검사':
            st.table(d)
        elif status == '지속성검사':
            st.table(e)
        elif status == '시간평균':
            st.table(f)
        elif status == '전체':
            st.table(dff)
    
    if name == '분자료 그래프':
        fig1 = px.line(c, x=c.index, y='기온(°C)')
        fig2 = px.line(d, x=d.index, y='단계검사')
        fig3 = px.line(e, x=e.index, y='지속성검사')
        fig4 = px.line(f, x=f.index, y='시간평균')

        if st.checkbox("기온"):st.plotly_chart(fig1)
        if st.checkbox("단계검사"):st.plotly_chart(fig2)
        if st.checkbox("지속성검사"):st.plotly_chart(fig3)
        if st.checkbox("시간평균"):st.plotly_chart(fig4)


    if name =='선택하세요':
        ' '
    h_list = module.h_file(paths) 



    h_data = module.hd_data(h_list)#시간자료
    if name_=='시간자료':
        st.table(h_data)




    hd = module.hd(h_list) #일평균
    if name_=='일평균':
        st.table(hd)
    

    hd= module.hd(h_list) #일평균그래프
    if name_ == '일평균 그래프':
        fig5 = px.line(hd, x=hd.index, y='일평균')
        st.plotly_chart(fig5)
    



    hm = module.hm(h_list) #월평균
    if name_=='월평균':
        st.table(hm)
    

    hm = module.hm(h_list) #월평균그래프
    if name_=='월평균 그래프':
        fig6 = px.line(hm, x=hm.index, y='월평균')
        st.plotly_chart(fig6)



















