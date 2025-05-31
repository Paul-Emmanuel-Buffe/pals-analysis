import streamlit as st
import pandas as pd

df1 = pd.read_csv('../data/Clean_Data--Palu-combat-attribute.csv')
df2 = pd.read_csv('../data/Clean_Data-comparison-of-ordinary-BOSS-attributes.csv')
df3 = pd.read_csv('../data/Clean_Data-hide-pallu-attributes.csv')
df4 = pd.read_csv('../data/Clean_Data-Palu-Job-Skills.csv')
df5 = pd.read_csv('../data/Clean_Data-Palu-refresh-level.csv')
df6 = pd.read_csv('../data/Clean_Data-Tower-BOSS-attribute-comparison.csv')

st.write(df1)
st.write(df2)
st.write(df3)
st.write(df4)
st.write(df5)
st.write(df6)
