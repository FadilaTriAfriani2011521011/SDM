#Libraries
import streamlit as st
import pandas as pd

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
    if len(daerah_selection3) == 0 or len(daerah_selection3) == 1:
        st.warning('Pilih Minimal 2 Daerah!')

    else:
        if(daerah_selection3):
            filter_Pangkat_2021 = df[df['Unit Kerja'].isin(daerah_selection3)]
            c1, c2 = st.columns(2)
            c3, c4 = st.columns(2)
            c5, c6 = st.columns(2)
            with c1:
                st.write('Tabel Pangkat Pegawai Golongan II Tahun 2021')
                st.bar_chart(filter_Pangkat_2021,x='Unit Kerja', y='II 2021')
            with c2:
                st.write('Tabel Pangkat Pegawai Golongan II Tahun 2022')
                st.bar_chart(filter_Pangkat_2021,x='Unit Kerja', y='II 2022')
            with c3:
                st.write('Tabel Pangkat Pegawai Golongan III Tahun 2021')
                st.bar_chart(filter_Pangkat_2021,x='Unit Kerja', y='III 2021')
            with c4:
                st.write('Tabel Pangkat Pegawai Golongan III Tahun 2022')
                st.bar_chart(filter_Pangkat_2021,x='Unit Kerja', y='III 2022')
            with c5:
                st.write('Tabel Pangkat Pegawai Golongan IV Tahun 2021')
                st.bar_chart(filter_Pangkat_2021,x='Unit Kerja', y='IV 2021')
            with c6:
                st.write('Tabel Pangkat Pegawai Golongan IV Tahun 2022')
                st.bar_chart(filter_Pangkat_2021,x='Unit Kerja', y='IV 2022')
    
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

