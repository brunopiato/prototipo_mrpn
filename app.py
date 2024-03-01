import streamlit as st
import pandas as pd
from io import StringIO

st.set_page_config(page_title='Home', 
                   page_icon='', 
                   layout='wide')

texto = "MRP-N Consulting"

dados = pd.read_csv('./dataset.csv')

def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

csv = convert_df(dados)


expander_ajuda = st.expander(
        'Ajuda para o preenchimento do template')
expander_ajuda.write("""
            Aqui você encontra as instruções para o preenchimento do template.
            """)

col1, col2, col3 = st.columns([1,2,5])


with col1:
    st.download_button('Download', 
                       csv,
                       file_name='dataset.csv',
                       mime='text/csv')

with col2:
    uploaded_file = st.file_uploader("Choose a file")

