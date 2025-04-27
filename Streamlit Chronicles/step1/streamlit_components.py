import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

st.header('`streamlit_pandas_profiling`')

df = pd.read_csv('https://raw.githubusercontent.com/AbhishekR5/machine-learning-topics/main/datasets/Spotify_data.csv',skiprows=[41])

pr = ProfileReport(df)
st_profile_report(pr)
