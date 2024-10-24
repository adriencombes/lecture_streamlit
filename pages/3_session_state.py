import streamlit as st

st.title('Cookie clicker')

if 'count' not in st.session_state:
    st.session_state['count'] = 0

if st.button('Make a cookie'):
    st.session_state.count += 1

st.write(':cookie:'*st.session_state.count)
