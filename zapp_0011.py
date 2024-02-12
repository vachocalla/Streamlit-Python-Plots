import streamlit as st

add_selectbox = st.sidebar.selectbox(
    'Como te gustaria estar conectado?',
    ('Email','Home phone','Mobile phone')
)

add_slider = st.sidebar.slider(
    'Seleccione un rango de valores',
    0.0, 100.0, (25.0, 75.0)
)