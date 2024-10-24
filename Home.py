import streamlit as st

print('streamlit restarted')

st.set_page_config(
    page_title="Home",
    page_icon="👋",
)

st.title("Bienvenue sur mon streamlit")
st.write("Voici une petite description.")

clicked = st.button('click me')

if clicked:
    st.text('vous avez cliqué')


st.divider()


team = st.selectbox(
    'team ?',
    ['chats','chiens'],
    index=None)

if team == 'chats':
    st.write('miaou')
elif team == 'chiens':
    st.write('wouf')

### TO DO LIST ###

# streamlit run Home.py --server.runOnSave True
# expliquer widgets
# expliquer --server.runOnSave True
# editer le texte
# rajouter un print de logging
# rajouter un boutton
# recuperer le resultat de ce bouton
# regarder la doc du widget button
# si click == True faire un texte
# rajouter un divider
# regarder la doc de selectbox
# rajouter un chien/chat -> "miaou" / "wouf"
# vous voyez que click est reset à 0
# doc pour regarder la data
# doc pour les graphs
# doc pour le layout
# streamlit gallery

# -> retour aux slides
