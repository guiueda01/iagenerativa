import streamlit as st
import pandas as pd 


st.title('isso é um titulo')
st.button('clique aqui')
st.write('Isso é paragrafo')
dados = {
'vendas':[100,20,30,60],
'mês':['jan','fev','mar','abril']
}


df =  pd.DataFrame(dados)
st.line_chart(df, x='mês', y='vendas')