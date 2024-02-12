import streamlit as st

if "counter" not in st.session_state:
    st.session_state.counter = 0

st.session_state.counter += 1

st.header(f"Esta pagina fue cargada {st.session_state.counter} veces")
st.button("Correr de nuevo")