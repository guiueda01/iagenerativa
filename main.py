import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
st.header("Previsão de Vendas")



# Dados: [Investimento em Marketing] -> Faturamento
dados_vendas = pd.DataFrame({
    'investimento': [100, 200, 300, 400, 500, 600],
    'faturamento': [1200, 2500, 3200, 4800, 5100, 6300]
})

# objetivo: previsão de FATURAMENTO baseado nos investimentos

st.scatter_chart(dados_vendas, x='investimento', y='faturamento')
modelo= LinearRegression()
modelo.fit(dados_vendas[['investimento']], dados_vendas[['faturamento']])

investimento= st.number_input('insira seu investimento')

PrevisaoFaturamento= modelo.predict([[investimento]])

if st.button('clique aqui'):

    st.metric('o faturamento sera', np.round(PrevisaoFaturamento, 2))