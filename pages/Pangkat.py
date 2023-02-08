#Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
import subprocess
import sys
from streamlit_option_menu import option_menu
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt

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
                   usecols='A:N',
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
            c3, c4 = st.columns(2)
            c5, c6 = st.columns(2)
            with c1:
                plt.bar(filter_Pangkat_2021['Unit Kerja'].values,
                        filter_Pangkat_2021['II 2021'].values)
                plt.xlabel("Unit Kerja")
                plt.ylabel("Value")
                plt.title("Golongan II 2021")
                plt.xticks(rotation=90)
                st.pyplot()
                st.set_option('deprecation.showPyplotGlobalUse', False)
            with c2:
                plt.bar(filter_Pangkat_2021['Unit Kerja'].values,
                        filter_Pangkat_2021['II 2022'].values)
                plt.xlabel("Unit Kerja")
                plt.ylabel("Value")
                plt.title("Golongan II 2022")
                plt.xticks(rotation=90)
                st.pyplot()
                st.set_option('deprecation.showPyplotGlobalUse', False)
            with c3:
                plt.bar(filter_Pangkat_2021['Unit Kerja'].values,
                        filter_Pangkat_2021['III 2021'].values)
                plt.xlabel("Unit Kerja")
                plt.ylabel("Value")
                plt.title("Golongan III 2021")
                plt.xticks(rotation=90)
                st.pyplot()
                st.set_option('deprecation.showPyplotGlobalUse', False)
            with c4:
                plt.bar(filter_Pangkat_2021['Unit Kerja'].values,
                        filter_Pangkat_2021['III 2022'].values)
                plt.xlabel("Unit Kerja")
                plt.ylabel("Value")
                plt.title("Golongan III 2022")
                plt.xticks(rotation=90)
                st.pyplot()
                st.set_option('deprecation.showPyplotGlobalUse', False)
            with c5:
                plt.bar(filter_Pangkat_2021['Unit Kerja'].values,
                        filter_Pangkat_2021['IV 2021'].values)
                plt.xlabel("Unit Kerja")
                plt.ylabel("Value")
                plt.title("Golongan IV 2021")
                plt.xticks(rotation=90)
                st.pyplot()
                st.set_option('deprecation.showPyplotGlobalUse', False)
            with c6:
                plt.bar(filter_Pangkat_2021['Unit Kerja'].values,
                        filter_Pangkat_2021['IV 2022'].values)
                plt.xlabel("Unit Kerja")
                plt.ylabel("Value")
                plt.title("Golongan IV 2022")
                plt.xticks(rotation=90)
                st.pyplot()
                st.set_option('deprecation.showPyplotGlobalUse', False)
    
elif(option == 'Daerah'):
    unit_kerja = df['Unit Kerja'].unique().tolist()
    unit_kerja_selection = st.selectbox('Pilih Daerah : ', unit_kerja)
    m1, m2, m3= st.columns((1, 1, 1))
    todf = pd.read_excel('pegawai.xlsx', sheet_name='Pangkat')
    to = todf[(todf['Unit Kerja'] == unit_kerja_selection)]

    # ===== Delta Section =====
    perII2 = int(to['II 2022']) - int(to['II 2021'])
    perIII2 = int(to['III 2022']) - int(to['III 2021'])
    perIV2 = int(to['IV 2022']) - int(to['IV 2021'])
   
    # ===== Comparation =====
    totalII2022 = df['II 2022'].sum()
    totalIII2022 = df['III 2022'].sum()
    totalIV2022 = df['IV 2022'].sum()
    

    with m1:
        m1.metric(label ='Jumlah Gol II 2022',value = int(to['II 2022']), delta= perII2)
        m1.metric(label ='Jumlah Gol II 2022 se-Provinsi Sumbar',value = totalII2022)
    with m2:
         m2.metric(label ='Jumlah Gol III 2022',value = int(to['III 2022']), delta= perIII2)
         m2.metric(label ='Jumlah Gol III 2022 se-Provinsi Sumbar',value = totalIII2022)
    with m3:
         m3.metric(label ='Jumlah Gol IV 2022',value = int(to['IV 2022']), delta= perIV2)
         m3.metric(label ='Jumlah Gol IV se-Provinsi Sumbar',value = totalIV2022)
   
    
    # ----- MANIPULATION for Man -----
    # ===== List for Values =====
    single_row_df = to[0:1]
    listValuesPangkat = []
    list_from_df_dua2 = single_row_df.values.tolist()[0]
    for i in range(2, 4):
        listValuesPangkat.append(list_from_df_dua2[i])
    # ----- END OF MANIPULATION -----
    # ===== Show Bar Chart =====
    unit_kerja_Pangkat = pd.DataFrame({
        'Value': listValuesPangkat
    }, index=['2021', '2022'])
    st.subheader("Line Golongan II")
    st.line_chart(unit_kerja_Pangkat,  y='Value', use_container_width=True)
    
    # ----- MANIPULATION for Man -----
    # ===== List for Values =====
    single_row_df = to[0:1]
    listValuesPangkat = []
    list_from_df_tiga2 = single_row_df.values.tolist()[0]
    for i in range(5, 7):
        listValuesPangkat.append(list_from_df_tiga2[i])
    # ----- END OF MANIPULATION -----
    # ===== Show Bar Chart =====
    unit_kerja_Pangkat = pd.DataFrame({
        'Value': listValuesPangkat
    }, index=['2021', '2022'])
    st.subheader("Line Golongan III")
    st.line_chart(unit_kerja_Pangkat,  y='Value', use_container_width=True)
    
     # ----- MANIPULATION for Woman -----
    # ===== List for Values =====
    single_row_df = to[0:1]
    listValuesPangkat = []
    list_from_df_empat2 = single_row_df.values.tolist()[0]
    for i in range(8, 10):
        listValuesPangkat.append(list_from_df_empat2[i])
    # ----- END OF MANIPULATION -----
    # ===== Show Bar Chart =====
    unit_kerja_Pangkat = pd.DataFrame({
        'Value': listValuesPangkat
    }, index=['2021', '2022'])
    st.subheader("Line Golongan IV")
    st.line_chart(unit_kerja_Pangkat,  y='Value', use_container_width=True)

    




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
