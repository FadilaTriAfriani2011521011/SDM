#Libraries
import streamlit as st
import pandas as pd

st.set_page_config(page_title='Data Sex Ratio', page_icon=':bar_chart:', layout='wide')
st.title('Data Sex Ratio Pegawai BPS se-Provinsi Sumatera Barat')

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
sheet_name1 = 'Sex ratio'

# ===== Sex Ratio =====
df = pd.read_excel(excel_file,
                   sheet_name=sheet_name1,
                   usecols='A:O',
                   header=0)
df_participants = pd.read_excel(excel_file,
                                sheet_name= sheet_name1,
                                usecols='B:C')
df_participants.dropna(inplace=True)

# ===== Dropdown in Sidebar =====
option = st.sidebar.selectbox(
    'Pilih :',
    ('All', 'Daerah'))

if(option == 'All'):
    # ===== STREAMLIT SELECTION =====
    daerah1 = df['Unit Kerja'].unique()
    daerah_selection1 = st.multiselect('Daerah:',
                                        daerah1,
                                        default=daerah1)

    # Selected option
    if len(daerah_selection1) == 0 or len(daerah_selection1) == 1:
        st.warning('Pilih Minimal 2 Daerah!')

    else:
        if(daerah_selection1):
            filter_sexRatio_2021 = df[df['Unit Kerja'].isin(daerah_selection1)]
            c1, c2 = st.columns(2)
            st.subheader("Tahun 2021")
            st.bar_chart(filter_sexRatio_2021,x='Unit Kerja', y='sex ratio 2021')
            st.subheader("Tahun 2022")
            st.bar_chart(filter_sexRatio_2021,x='Unit Kerja', y='sex ratio 2022')
                

elif(option == 'Daerah'):
    unit_kerja = df['Unit Kerja'].unique().tolist()
    unit_kerja_selection = st.selectbox('Pilih Daerah : ', unit_kerja)
    m1, m2, m3, m4 = st.columns((1, 1, 1, 1))
    todf = pd.read_excel('pegawai.xlsx', sheet_name='Sex ratio')
    to = todf[(todf['Unit Kerja'] == unit_kerja_selection)]

    # ===== Delta Section =====
    perLaki2 = int(to['Laki-laki 2022']) - int(to['Laki-laki 2021'])
    perPerempuan2 = int(to['Perempuan 2022']) - int(to['Perempuan 2021'])
    perTotal = int(to['Jumlah 2022']) - int(to['Jumlah 2021'])
    persentaseSexRatio = float(to['sex ratio 2022'].map('{:,.2f}'.format))
    convertSexRatio = str(persentaseSexRatio)
    percentageSexRatio = convertSexRatio + "%"

    # ===== Comparation =====
    totalLaki2022 = df['Laki-laki 2022'].sum()
    totalPerempuan2022 = df['Perempuan 2022'].sum()
    totalSeluruh2022 = totalLaki2022 + totalPerempuan2022
    totalSexRatio2022 = (totalLaki2022/totalPerempuan2022) * 100
    format_float_ratio = "{:,.2f}".format(totalSexRatio2022)
    format_string_ratio = str(format_float_ratio) + "%"
    

    with m1:
        m1.metric(label ='Jumlah Pria 2022',value = int(to['Laki-laki 2022']), delta= perLaki2)
        m1.metric(label ='Jumlah Pria 2022 se-Provinsi Sumbar',value = totalLaki2022)
    with m2:
        m2.metric(label ='Jumlah Wanita 2022',value = int(to['Perempuan 2022']), delta= perPerempuan2)
        m2.metric(label ='Jumlah Wanita 2022 se-Provinsi Sumbar',value = totalPerempuan2022)
    with m3:
         m3.metric(label ='Total Pegawai 2022',value = int(to['Jumlah 2022']), delta= perTotal)
         m3.metric(label ='Total Pegawai 2022 se-Provinsi Sumbar',value = totalSeluruh2022)
    with m4:
         m4.metric(label ='Sex Ratio 2022 (%)',value=percentageSexRatio)
         m4.metric(label ='Sex Ratio 2022 se-Provinsi Sumbar (%) ',value=format_string_ratio)

    # ----- MANIPULATION for Man -----
    # ===== List for Values =====
    single_row_df = to[0:1]
    listValuesSexRatio = []
    list_from_df_laki2 = single_row_df.values.tolist()[0]
    for i in range(2, 4):
        listValuesSexRatio.append(list_from_df_laki2[i])
    # ----- END OF MANIPULATION -----
    # ===== Show Bar Chart =====
    unit_kerja_sexRatio = pd.DataFrame({
        'Value': listValuesSexRatio
    }, index=['2021', '2022'])
    st.subheader("Line Chart Laki-Laki")
    st.line_chart(unit_kerja_sexRatio,  y='Value', use_container_width=True)


    # ----- MANIPULATION for Woman -----
    # ===== List for Values =====
    single_row_df = to[0:1]
    listValuesSexRatio = []
    list_from_df_wanita2 = single_row_df.values.tolist()[0]
    for i in range(5, 7):
        listValuesSexRatio.append(list_from_df_wanita2[i])
    # ----- END OF MANIPULATION -----
    # ===== Show Bar Chart =====
    unit_kerja_sexRatio = pd.DataFrame({
        'Value': listValuesSexRatio
    }, index=['2021', '2022'])
    st.subheader("Line Chart Perempuan")
    st.line_chart(unit_kerja_sexRatio,  y='Value', use_container_width=True)
        

    
    
   
   