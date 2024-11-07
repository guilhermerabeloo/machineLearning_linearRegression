import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("pizzas.csv")

model = LinearRegression()

x = df[["diametro"]]
y = df[["preco"]]

model.fit(x, y)

st.title("Prevendo o valor da pizza pelo diametro")
st.divider()
diametro = st.number_input("Digite o tamanho do diametro da pizza")

if diametro:
    preco_previsto = model.predict([[diametro]])[0][0]

    st.write(f'O valor da pizza com o diametro de {diametro:.2f}cm é: R$ {preco_previsto:.2f}.')
    st.balloons()