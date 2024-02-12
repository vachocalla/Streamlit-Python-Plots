import streamlit as st
import numpy as np
import pandas as pd

chartData = pd.DataFrame(
    np.random.randn(20,3),
    columns = ['a','b','c']
)
st.line_chart(chartData)