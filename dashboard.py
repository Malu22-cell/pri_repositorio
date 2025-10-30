import streamlit as st
import pandas as pd

st.title("Meu primeiro Dashboard.")
st.text("Meu nome é Malu")
st.slider("Idade", 0,100,25)
st.button("Aperte aqui")
df = pd.read_csv("empresas_desempenho.csv")
st.dataframe(df)

import matplotlib.pyplot as plt
import pandas as pd 
files="empresas_desempenho.csv"
df=pd.read_csv(files)

#graficos de barras 

df_grouped = df.groupby("Setor")["Receita"].sum().reset_index()
fig = plt.figure(figsize=(8,5))
plt.bar(df_grouped["Setor"],df_grouped["Receita"])
plt.title("grafico de barras Setor x Receita")
plt.xlabel("Setor")
plt.ylabel("Receita")

st.pyplot(fig)
