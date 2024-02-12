import streamlit as st
import pandas as pd

df = pd.DataFrame(
    {
        'first column': [1,2,3,4],
        'second column': [10,20,30,40]
    }
)

option = st.selectbox(
    'Que numero te gustaria mejor',
    df['first column']
)

'Seleccionaste', option