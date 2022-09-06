# -*- coding: utf-8 -*-
import streamlit as st
class multipage:
    def __init__(self):
        self.pages=[]
        
    def add_page(self, title, func):
        self.pages.append({
            'title':title,
            'function':func
            })
        
    def run(self):
        
        page = st.sidebar.selectbox(
            '가상환경',
            self.pages,
            format_func=lambda page: page['title'])
        
        page['function']()

