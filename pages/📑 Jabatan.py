#Libraries
import streamlit as st
import pandas as pd

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
    if len(daerah_selection5) == 0 or len(daerah_selection5) == 1:
        st.warning('Pilih Minimal 2 Daerah!')

    else:
        if(daerah_selection5):
            filtered_Jabatan_2021 = df[df['Unit Kerja'].isin(daerah_selection5)]
            c1, c2 = st.columns(2)
            c3, c4 = st.columns(2)
            with c1:
                st.write('Tabel Pegawai dengan Jabatan Fungsional Tahun 2021')
                st.bar_chart(filtered_Jabatan_2021,x='Unit Kerja', y='Fungsional 2021')
            with c2:
                st.write('Tabel Pegawai dengan Jabatan Fungsional Tahun 2022')
                st.bar_chart(filtered_Jabatan_2021,x='Unit Kerja', y='Fungsional 2022')
            with c3:
                st.write('Tabel Pegawai dengan Jabatan Struktural Tahun 2021')
                st.bar_chart(filtered_Jabatan_2021,x='Unit Kerja', y='Struktural 2021')
            with c4:
                st.write('Tabel Pegawai dengan Jabatan Struktural Tahun 2021')
                st.bar_chart(filtered_Jabatan_2021,x='Unit Kerja', y='Struktural 2022')

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



   