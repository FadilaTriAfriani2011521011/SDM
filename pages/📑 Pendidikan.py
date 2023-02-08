#Libraries
import streamlit as st
import pandas as pd

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
                   usecols='A:R',
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
    if len(daerah_selection2) == 0 or len(daerah_selection2) == 1:
        st.warning('Pilih Minimal 2 Daerah!')

    else:
        if(daerah_selection2):
            filter_Pendidikan_2021 = df[df['Unit Kerja'].isin(daerah_selection2)]
            c1, c2 = st.columns(2)
            c3, c4 = st.columns(2)
            c5, c6 = st.columns(2)
            c7, c8 = st.columns(2)
            
            with c1:
                st.write('Tabel Pegawai Tamatan Sarjana Tahun 2021')
                st.bar_chart(filter_Pendidikan_2021,x='Unit Kerja', y='Sarjana 2021')
            with c2:
                st.write('Tabel Pegawai Tamatan Sarjana Tahun 2022')
                st.bar_chart(filter_Pendidikan_2021,x='Unit Kerja', y='Sarjana 2022')
            with c3:
                st.write('Tabel Pegawai Tamatan Diploma Tahun 2021')
                st.bar_chart(filter_Pendidikan_2021,x='Unit Kerja', y='Diploma 2021')
            with c4:
                st.write('Tabel Pegawai Tamatan Diploma Tahun 2021')
                st.bar_chart(filter_Pendidikan_2021,x='Unit Kerja', y='Diploma 2022')
            with c5:
                st.write('Tabel Pegawai Tamatan SMA Tahun 2021')
                st.bar_chart(filter_Pendidikan_2021,x='Unit Kerja', y='SMA 2021')
            with c6:
                st.write('Tabel Pegawai Tamatan SMA Tahun 2021')
                st.bar_chart(filter_Pendidikan_2021,x='Unit Kerja', y='SMA 2022')
            with c7:
                st.write('Tabel Pegawai Tamatan SMP Tahun 2021')
                st.bar_chart(filter_Pendidikan_2021,x='Unit Kerja', y='SMP 2021')
            with c8:
                st.write('Tabel Pegawai Tamatan SMP Tahun 2021')
                st.bar_chart(filter_Pendidikan_2021,x='Unit Kerja', y='SMP 2022')

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

