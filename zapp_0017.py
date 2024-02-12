import streamlit as st

conn = st.connection("personal40")
df = conn.query("select * from RH_PAIS")
st.dataframe(df)