#Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
import subprocess
import sys
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Data Pendidikan', page_icon=':bar_chart:', layout='wide')
st.title('Data Pendidikan Pegawai BPS se-Provinsi Sumatera Barat')

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

sheet_name2 = 'Pendidikan'

# ===== Pendidikan =====
df = pd.read_excel(excel_file,
                   sheet_name=sheet_name2,
                   usecols='A:K',
                   header=0)
df_participants = pd.read_excel(excel_file,
                                sheet_name= sheet_name2,
                                usecols='B:C')
df_participants.dropna(inplace=True)

# ===== Dropdown in Sidebar =====
option = st.sidebar.selectbox(
    'Pilih :',
    ('All', 'Daerah'))

if(option == 'All'):

    # ===== STREAMLIT SELECTION =====
  
    daerah2 = df['Unit Kerja'].unique()
    daerah_selection2 = st.multiselect('Daerah:',
                                        daerah2,
                                        default=daerah2)
    

    # Selected option
    st.write('Tabel Data Pendidikan')
    if len(daerah_selection2) == 0 or len(daerah_selection2) == 1:
        st.warning('Pilih Minimal 2 Daerah!')

    else:
        if(daerah_selection2):
            filtered_df = df[df['Unit Kerja'].isin(daerah_selection2)]
            #  c1, c2 = st.columns(2)
            # with c1:
            #     plt.bar(filter_Pendidikan_2021['Unit Kerja'].values,
            #             filter_Pendidikan_2021['sex ratio 2021'].values)
            #     plt.xlabel("Unit Kerja")
            #     plt.ylabel("Value")
            #     plt.title("Sex Ratio 2021")
            #     plt.xticks(rotation=90)
            #     st.pyplot()
            #     st.set_option('deprecation.showPyplotGlobalUse', False)
            # with c2:
            #     plt.bar(filter_sexRatio_2021['Unit Kerja'].values,
            #             filter_sexRatio_2021['sex ratio 2022'].values)
            #     plt.xlabel("Unit Kerja")
            #     plt.ylabel("Value")
            #     plt.title("Sex Ratio 2022")
            #     plt.xticks(rotation=90)
            #     st.pyplot()
            #     st.set_option('deprecation.showPyplotGlobalUse', False)

elif(option == 'Daerah'):
    unit_kerja = df['Unit Kerja'].unique().tolist()
    unit_kerja_selection = st.selectbox('Pilih Daerah : ', unit_kerja)
    m1, m2, m3, m4 = st.columns((1, 1, 1, 1))
    todf = pd.read_excel('pegawai.xlsx', sheet_name='Pendidikan')
    to = todf[(todf['Unit Kerja'] == unit_kerja_selection)]

    # ===== Delta Section =====
    perSarjana2 = int(to['Sarjana 2022']) - int(to['Sarjana 2021'])
    perDiploma2 = int(to['Diploma 2022']) - int(to['Diploma 2021'])
    perSMA2 = int(to['SMA 2022']) - int(to['SMA 2021'])
    perSMP2 = int(to['SMP 2022']) - int(to['SMP 2021'])
   
    # ===== Comparation =====
    totalSarjana2022 = df['Sarjana 2022'].sum()
    totalDiploma2022 = df['Diploma 2022'].sum()
    totalSMA2022 = df['SMA 2022'].sum()
    totalSMP2022 = df['SMP 2022'].sum()
    
    
    with m1:
        m1.metric(label ='Jumlah Sarjana 2022',value = int(to['Sarjana 2022']), delta= perSarjana2)
        m1.metric(label ='Jumlah Sarjana 2022 se-Provinsi Sumbar',value = totalSarjana2022)
    with m2:
         m2.metric(label ='Jumlah Diploma 2022',value = int(to['Diploma 2022']), delta= perDiploma2)
         m2.metric(label ='Jumlah Diploma 2022 se-Provinsi Sumbar',value = totalDiploma2022)
    with m3:
         m3.metric(label ='Jumlah SMA 2022',value = int(to['SMA 2022']), delta= perSMA2)
         m3.metric(label ='Jumlah SMA 2022 se-Provinsi Sumbar',value = totalSMA2022)
    with m4:
          m4.metric(label ='Jumlah SMP 2022',value = int(to['SMP 2022']), delta= perSMP2)
          m4.metric(label ='Jumlah SMP 2022 se-Provinsi Sumbar',value = totalSMP2022)
   
    
    # ----- MANIPULATION for Man -----
    # ===== List for Values =====
    single_row_df = to[0:1]
    listValuesPendidikan = []
    list_from_df_sarjana2 = single_row_df.values.tolist()[0]
    for i in range(2, 4):
        listValuesPendidikan.append(list_from_df_sarjana2[i])
    # ----- END OF MANIPULATION -----
    # ===== Show Bar Chart =====
    unit_kerja_Pendidikan = pd.DataFrame({
        'Value': listValuesPendidikan
    }, index=['2021', '2022'])
    st.subheader("Line Sarjana")
    st.line_chart(unit_kerja_Pendidikan,  y='Value', use_container_width=True)


     # ----- MANIPULATION for Woman -----
    # ===== List for Values =====
    single_row_df = to[0:1]
    listValuesPendidikan = []
    list_from_df_diploma2 = single_row_df.values.tolist()[0]
    for i in range(5, 7):
        listValuesPendidikan.append(list_from_df_diploma2[i])
    # ----- END OF MANIPULATION -----
    # ===== Show Bar Chart =====
    unit_kerja_Pendidikan = pd.DataFrame({
        'Value': listValuesPendidikan
    }, index=['2021', '2022'])
    st.subheader("Line Diploma")
    st.line_chart(unit_kerja_Pendidikan,  y='Value', use_container_width=True)

     # ----- MANIPULATION for Woman -----
    # ===== List for Values =====
    single_row_df = to[0:1]
    listValuesPendidikan = []
    list_from_df_sma2 = single_row_df.values.tolist()[0]
    for i in range(8, 10):
        listValuesPendidikan.append(list_from_df_sma2[i])
    # ----- END OF MANIPULATION -----
    # ===== Show Bar Chart =====
    unit_kerja_Pendidikan = pd.DataFrame({
        'Value': listValuesPendidikan
    }, index=['2021', '2022'])
    st.subheader("Line SMA")
    st.line_chart(unit_kerja_Pendidikan,  y='Value', use_container_width=True)

     # ----- MANIPULATION for Woman -----
    # ===== List for Values =====
    single_row_df = to[0:1]
    listValuesPendidikan = []
    list_from_df_smp2 = single_row_df.values.tolist()[0]
    for i in range(11, 13):
        listValuesPendidikan.append(list_from_df_smp2[i])
    # ----- END OF MANIPULATION -----
    # ===== Show Bar Chart =====
    unit_kerja_Pendidikan = pd.DataFrame({
        'Value': listValuesPendidikan
    }, index=['2021', '2022'])
    st.subheader("Line SMP")
    st.line_chart(unit_kerja_Pendidikan,  y='Value', use_container_width=True)

    
        

    
    
   
   

# elif(option == 'Daerah'):
#     daerah2 = df['Unit Kerja'].unique().tolist()
#     daerah_selection2 = st.selectbox('Pilih Daerah : ', daerah2)
#     m1,m2,m3,m4 = st.columns((1,1,1,1))
#     todf = pd.read_excel('pegawai.xlsx',sheet_name = 'Pendidikan')
#     to = todf[(todf['Unit Kerja']==daerah_selection2)]
#     m1.metric(label ='Lulusan S3',value = int(to['S3']))
#     m1.metric(label ='Lulusan S2',value = int(to['S2']))
#     m1.metric(label ='Lulusan S1',value = int(to['S1']))
#     m2.metric(label ='Lulusan Diploma',value = int(to['Diploma']))
#     m3.metric(label ='Lulusan SMA',value = int(to['SMA']))
#     m3.metric(label ='Lulusan SMP',value = int(to['SMP']))
#     m3.metric(label ='Lulusan SD',value = int(to['SD ']))
#     m4.metric(label ='Total',value = int(to['Total']))

