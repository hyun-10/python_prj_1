# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np

import glob



def m_file(paths):
    file_list = glob.glob(paths + '*.csv')

    m_list=[]
    for i in file_list:
        if 'MI' in i:
            m_list.append(i)
    
    return m_list




def m_data(m_list):
    m_list.sort()
    dff = pd.DataFrame()
    for m in m_list:
        df= pd.read_csv(m,encoding='cp949')
        temp =df[(df['기온(°C)']>-33) & ( df['기온(°C)']<40) ]
        ttem = temp['기온(°C)'].diff().abs() # 결측자료 -
        ttem[ttem>3]=np.nan
        ttem[ttem<-3]=np.nan
        temp['단계검사']=ttem
        tempp = temp.set_index('일시')
        tempp.index = pd.to_datetime(tempp.index)#데이터타입으로 
        
        a=tempp['단계검사'].resample('H').sum() #지속성검사
        t = tempp['기온(°C)'].resample('H').mean() #시간평균
        size = tempp['기온(°C)'].resample('H').size()
        
        a[a<0.1]=np.nan
        tempp['지속성검사'] = a
        tempp['시간평균']=t
        tempp['size']=size
        tempp.loc[tempp['size']<48,'시간평균']=np.nan

        dff=dff.append(tempp)
        
        del dff['지점']
        del dff['지점명']

        c=dff['기온(°C)'].dropna()
        d=dff['단계검사'].dropna()
        e=dff['지속성검사'].dropna()
        f=dff['시간평균'].dropna()
    return (c,d,e,f,dff)



def h_file(paths):
    file_list = glob.glob(paths + '*.csv')
    h_list=[]


    for i in file_list:
        if 'TIM' in i:
            h_list.append(i)

    return h_list

def hd_data(h_list):
    for i in h_list:
        df= pd.read_csv(i,encoding='cp949')
        
        hdd=pd.DataFrame()
        hdd=hdd.append(df)
        hdd=hdd.set_index('일시')
        del hdd['지점']
        del hdd['지점명']
    return hdd


def hd(h_list):#일평균
    for i in h_list:
        df= pd.read_csv(i,encoding='cp949')
        hd = df.set_index('일시')
        hd.index = pd.to_datetime(hd.index)#데이터타입으로 변

        siz =hd['기온(°C)'].resample('D').agg({"counts":'size',"일평균":'mean'})
        siz.loc[siz['counts']<20, '일평균'] = np.nan
        siz.drop('2022-06-19T00:00:00',inplace=True)
        del siz['counts']
        
    return siz


def hm(h_list):#월평균
    for i in h_list:
        df= pd.read_csv(i,encoding='cp949')
        hd = df.set_index('일시')
        hd.index = pd.to_datetime(hd.index)#데이터타입으로 변
        d=hd['기온(°C)'].resample('D').mean() #지속성검사
        dd=d.resample('M').agg({"counts":'size',"월평균":'mean'})
        dd.loc[dd['counts']<24, '월평균'] = np.nan
        del dd['counts']

    return dd































