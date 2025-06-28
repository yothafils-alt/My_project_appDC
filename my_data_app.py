import streamlit as st
import pandas as pd


st.markdown("<h1 style='text-align: center; color: black;'>TROUVEZ CHEZ NOUS VOS DONNEES ANIMAUX</h1>", unsafe_allow_html=True)

st.markdown("""
Cette application vous permet d'avoir des données sur la vente des animaux sur le site le coin afrique 
* **Python libraries:** base64, pandas, streamlit
* **Data source:** [Expat-Dakar](https://sn.coinafrique.com/).
""")


# Fonction de loading des données
def load_(dataframe, title, key) :
    st.markdown("""
    <style>
    div.stButton {text-align:center}
    </style>""", unsafe_allow_html=True)

    if st.button(title,key):
      
        st.subheader('Display data dimension')
        st.write('Data dimension: ' + str(dataframe.shape[0]) + ' rows and ' + str(dataframe.shape[1]) + ' columns.')
        st.dataframe(dataframe)

# définir quelques styles liés aux box
st.markdown('''<style> .stButton>button {
    font-size: 12px;
    height: 3em;
    width: 25em;
}</style>''', unsafe_allow_html=True)

          
# Charger les données 
load_(pd.read_csv('data/coinafrique_animaux.csv'), 'Chiens data 1', '1')
load_(pd.read_csv('data/coinafrique_animaux_moutons.csv'), 'Moutons data 2', '2')
load_(pd.read_csv('data/coinafrique_animaux_poules_lapins_pigeons.csv'), 'poules lapins pigeons data 3', '3')
load_(pd.read_csv('data/coinafrique_animaux_autres_animaux.csv'), 'Autres animaux 4', '4')

st.markdown("### 💬 Participez à l’évaluation de l’application")
st.markdown(
    '[📝 Cliquez ici pour remplir le formulaire](https://ee.kobotoolbox.org/i/NNlhJatO)',
    unsafe_allow_html=True
)
