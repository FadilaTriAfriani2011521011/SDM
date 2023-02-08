#Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
import subprocess
import sys
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Data Pangkat', page_icon=':bar_chart:', layout='wide')
st.title('Data Pangkat Pegawai BPS se-Provinsi Sumatera Barat')

# Setting
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

# Filter 
excel_file = 'pegawai.xlsx'

sheet_name3 = 'Pangkat'

# ===== Pangkat =====
df = pd.read_excel(excel_file,
                   sheet_name=sheet_name3,
                   usecols='A:P',
                   header=0)
df_participants = pd.read_excel(excel_file,
                                sheet_name= sheet_name3,
                                usecols='B:C')
df_participants.dropna(inplace=True)

# ===== Dropdown in Sidebar =====
option = st.sidebar.selectbox(
    'Pilih :',
    ('All', 'Daerah'))

if(option == 'All'):

    # ===== STREAMLIT SELECTION =====
  
    daerah3 = df['Unit Kerja'].unique()
    daerah_selection3 = st.multiselect('Daerah:',
                                        daerah3,
                                        default=daerah3)
    

    # Selected option
    st.write('Tabel Data Pangkat')
    if len(daerah_selection3) == 0 or len(daerah_selection3) == 1:
        st.warning('Pilih Minimal 2 Daerah!')

    else:
        if(daerah_selection3):
            filter_Pangkat_2021 = df[df['Unit Kerja'].isin(daerah_selection3)]
            c1, c2 = st.columns(2)
            with c1:
                plt.bar(filter_Pangkat_2021['Unit Kerja'].values,
                        filter_Pangkat_2021['II 2021'].values)
                plt.xlabel("Unit Kerja")
                plt.ylabel("Value")
                plt.title("Sarjana 2021")
                plt.xticks(rotation=90)
                st.pyplot()
                st.set_option('deprecation.showPyplotGlobalUse', False)
            with c2:
                plt.bar(filter_Pendidikan_2021['Unit Kerja'].values,
                        filter_Pendidikan_2021['Sarjana 2022'].values)
                plt.xlabel("Unit Kerja")
                plt.ylabel("Value")
                plt.title("Sarjana 2022")
                plt.xticks(rotation=90)
                st.pyplot()
                st.set_option('deprecation.showPyplotGlobalUse', False)



















# elif(option == 'Daerah'):
#     daerah3 = df['Unit Kerja'].unique().tolist()
#     daerah_selection3 = st.selectbox('Pilih Daerah : ', daerah3)
#     m1,m2,m3,m4 = st.columns((1,1,1,1))
#     todf = pd.read_excel('pegawai.xlsx',sheet_name = 'Pangkat')
#     to = todf[(todf['Unit Kerja']==daerah_selection3)]
#     m1.metric(label ='Golongan II/a',value = int(to['II/a']))
#     m1.metric(label ='Golongan II/b',value = int(to['II/b']))
#     m1.metric(label ='Golongan II/c',value = int(to['II/c']))
#     m1.metric(label ='Golongan II/d',value = int(to['II/d']))
#     m2.metric(label ='Golongan III/a',value = int(to['III/a']))
#     m2.metric(label ='Golongan III/b',value = int(to['III/b']))
#     m2.metric(label ='Golongan III/c',value = int(to['III/c']))
#     m2.metric(label ='Golongan III/d',value = int(to['III/d']))
#     m3.metric(label ='Golongan IV/a',value = int(to['IV/a']))
#     m3.metric(label ='Golongan IV/b',value = int(to['IV/b']))
#     m3.metric(label ='Golongan IV/c',value = int(to['IV/c']))
#     m3.metric(label ='Golongan IV/d',value = int(to['IV/d']))
#     m4.metric(label ='Total',value = int(to['Total']))



