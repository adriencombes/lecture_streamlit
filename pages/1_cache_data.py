import streamlit as st
import time

st.set_page_config(
    page_title="Cache cache",
    page_icon="👋",
)

st.title('Cache data')

@st.cache_data
def long_calculation(x):
    time.sleep(5)  # Simule un calcul long
    return x * 2

number = st.number_input("Insert a number",value=1)

if st.button("Calculate"):
    st.write(f"Appel de la fonction avec {number} :")
    result1 = long_calculation(number)
    st.write(result1)
