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
                   usecols='A:L',
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
            filtered_Jabatan_2021 = df[df['Unit Kerja'].isin(daerah_selection5)]
            c1, c2 = st.columns(2)
            c3, c4 = st.columns(2)
            with c1:
                plt.bar(filtered_Jabatan_2021['Unit Kerja'].values,
                        filtered_Jabatan_2021['Fungsional 2021'].values)
                plt.xlabel("Unit Kerja")
                plt.ylabel("Value")
                plt.title("Jabatan Fungsional 2021")
                plt.xticks(rotation=90)
                st.pyplot()
                st.set_option('deprecation.showPyplotGlobalUse', False)
            with c2:
                plt.bar(filtered_Jabatan_2021['Unit Kerja'].values,
                        filtered_Jabatan_2021['Fungsional 2022'].values)
                plt.xlabel("Unit Kerja")
                plt.ylabel("Value")
                plt.title("Jabatan Fungsional 2022")
                plt.xticks(rotation=90)
                st.pyplot()
                st.set_option('deprecation.showPyplotGlobalUse', False)
            with c3:
                plt.bar(filtered_Jabatan_2021['Unit Kerja'].values,
                        filtered_Jabatan_2021['Struktural 2021'].values)
                plt.xlabel("Unit Kerja")
                plt.ylabel("Value")
                plt.title("Jabatan Struktural 2021")
                plt.xticks(rotation=90)
                st.pyplot()
                st.set_option('deprecation.showPyplotGlobalUse', False)
            with c4:
                plt.bar(filtered_Jabatan_2021['Unit Kerja'].values,
                        filtered_Jabatan_2021['Struktural 2022'].values)
                plt.xlabel("Unit Kerja")
                plt.ylabel("Value")
                plt.title("Jabatan Struktural 2022")
                plt.xticks(rotation=90)
                st.pyplot()
                st.set_option('deprecation.showPyplotGlobalUse', False)

elif(option == 'Daerah'):
    unit_kerja = df['Unit Kerja'].unique().tolist()
    unit_kerja_selection = st.selectbox('Pilih Daerah : ', unit_kerja)
    m1, m2 = st.columns((1, 1))
    todf = pd.read_excel('pegawai.xlsx', sheet_name='Jabatan')
    to = todf[(todf['Unit Kerja'] == unit_kerja_selection)]

    # ===== Delta Section =====
    perFungsional2 = int(to['Fungsional 2022']) - int(to['Fungsional 2021'])
    perStruktural2 = int(to['Struktural 2022']) - int(to['Struktural 2021'])
   
    # ===== Comparation =====
    totalFungsional2022 = df['Fungsional 2022'].sum()
    totalStruktural2022 = df['Struktural 2022'].sum()
    

    with m1:
        m1.metric(label ='Jumlah Fungsional 2022',value = int(to['Fungsional 2022']), delta= perFungsional2)
        m1.metric(label ='Jumlah Fungsional 2022 se-Provinsi Sumbar',value = totalFungsional2022)
    with m2:
         m2.metric(label ='Jumlah Struktural 2022',value = int(to['Struktural 2022']), delta= perStruktural2)
         m2.metric(label ='Jumlah Struktural 2022 se-Provinsi Sumbar',value = totalStruktural2022)
   
    
    # ----- MANIPULATION for Man -----
    # ===== List for Values =====
    single_row_df = to[0:1]
    listValuesJabatan = []
    list_from_df_fungsional2 = single_row_df.values.tolist()[0]
    for i in range(2, 4):
        listValuesJabatan.append(list_from_df_fungsional2[i])
    # ----- END OF MANIPULATION -----
    # ===== Show Bar Chart =====
    unit_kerja_Jabatan = pd.DataFrame({
        'Value': listValuesJabatan
    }, index=['2021', '2022'])
    st.subheader("Line Fungsional")
    st.line_chart(unit_kerja_Jabatan,  y='Value', use_container_width=True)

      # ----- MANIPULATION for Man -----
    # ===== List for Values =====
    single_row_df = to[0:1]
    listValuesJabatan = []
    list_from_df_fungsional2 = single_row_df.values.tolist()[0]
    for i in range(5, 7):
        listValuesJabatan.append(list_from_df_fungsional2[i])
    # ----- END OF MANIPULATION -----
    # ===== Show Bar Chart =====
    unit_kerja_Jabatan = pd.DataFrame({
        'Value': listValuesJabatan
    }, index=['2021', '2022'])
    st.subheader("Line Struktural")
    st.line_chart(unit_kerja_Jabatan,  y='Value', use_container_width=True)

     





# elif(option == 'Daerah'):
#     daerah5 = df['Unit Kerja'].unique().tolist()
#     daerah_selection5 = st.selectbox('Pilih Daerah : ', daerah5)
#     m1,m2,m3,m4,m5,m6 = st.columns((1,1,1,1,1,1))
#     todf = pd.read_excel('pegawai.xlsx',sheet_name = 'Jabatan')
#     to = todf[(todf['Unit Kerja']==daerah_selection5)]
#     m1.metric(label ='Fungsional Tertentu',value = int(to['Fungsional Tertentu']))
#     m2.metric(label ='Fungsional Umum',value = int(to['Fungsional Umum']))
#     m3.metric(label ='Pengawas',value = int(to['Pengawas']))
#     m4.metric(label ='Administrator',value = int(to['Administrator']))
#     m5.metric(label ='Pimpinan Tinggi Pratama',value = int(to['Pimpinan Tinggi Pratama']))
#     m6.metric(label ='Total',value = int(to['Total']))


   