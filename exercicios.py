# calculadora
import streamlit as st

st.title('calculadora')

numero1 = st.number_input('numero')
numero2 = st.number_input('numero', step = 0.1)

if st.button('RESULTADO'):
    soma = numero1 + numero2
    st.success(soma)

# calculadora de imc



st.title('Calculo da média')


nota1 = st.number_input('nota1')
nota2 = st.number_input('nota2')


if st.button('Calcular média'):
    calculo = round((nota1 + nota2) / 2, 2)
    st.success(calculo) 

