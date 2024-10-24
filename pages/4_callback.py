import streamlit as st

st.title('Bonjour')

def handle_submit(name, age, country="France"):
    st.success(f"Bonjour {name} de {country} agé de {age} ans")

with st.form(key='my_form'):
    name = st.text_input("Nom")
    age = st.number_input("Âge", min_value=0, max_value=120)
    country = st.text_input("Pays", value="France")

    submit_button = st.form_submit_button(
        label='Soumettre', on_click=handle_submit,
        args=(name, age), kwargs={"country": country}
    )

st.divider()

st.markdown("[widgets compatible callbacks](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state)")
