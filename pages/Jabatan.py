#Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
import subprocess
import sys
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Data Jabatan', page_icon=':bar_chart:', layout='wide')
st.title('Data Jabatan Pegawai BPS se-Provinsi Sumatera Barat')


# Setting'
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

# Filter 
excel_file = 'pegawai.xlsx'
sheet_name5 = 'Jabatan'

# ===== Jabatan =====
df = pd.read_excel(excel_file,
                   sheet_name=sheet_name5,
                   usecols='A:I',
                   header=0)
df_participants = pd.read_excel(excel_file,
                                sheet_name= sheet_name5,
                                usecols='B:C')
df_participants.dropna(inplace=True)

# ===== Dropdown in Sidebar =====
option = st.sidebar.selectbox(
    'Pilih :',
    ('All', 'Daerah'))

if(option == 'All'):
    # ===== STREAMLIT SELECTION =====
    
    daerah5 = df['Unit Kerja'].unique()
    daerah_selection5 = st.multiselect('Daerah:',
                                        daerah5,
                                        default=daerah5)
    

    # Selected option
    st.write('Tabel Data Jabatan')
    if len(daerah_selection5) == 0 or len(daerah_selection5) == 1:
        st.warning('Pilih Minimal 2 Daerah!')

    else:
        if(daerah_selection5):
            filtered_df = df[df['Unit Kerja'].isin(daerah_selection5)]
            st.write(filtered_df)

elif(option == 'Daerah'):
    daerah5 = df['Unit Kerja'].unique().tolist()
    daerah_selection5 = st.selectbox('Pilih Daerah : ', daerah5)
    m1,m2,m3,m4,m5,m6 = st.columns((1,1,1,1,1,1))
    todf = pd.read_excel('pegawai.xlsx',sheet_name = 'Jabatan')
    to = todf[(todf['Unit Kerja']==daerah_selection5)]
    m1.metric(label ='Fungsional Tertentu',value = int(to['Fungsional Tertentu']))
    m2.metric(label ='Fungsional Umum',value = int(to['Fungsional Umum']))
    m3.metric(label ='Pengawas',value = int(to['Pengawas']))
    m4.metric(label ='Administrator',value = int(to['Administrator']))
    m5.metric(label ='Pimpinan Tinggi Pratama',value = int(to['Pimpinan Tinggi Pratama']))
    m6.metric(label ='Total',value = int(to['Total']))


   