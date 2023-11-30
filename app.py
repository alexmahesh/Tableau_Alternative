import streamlit as st
import streamlit.components.v1 as stc
import pandas as pd
from pygwalker.api.streamlit import init_streamlit_comm, get_streamlit_html


@st.cache_resource
def load_data(data):
    '''
    Loads a CSV-File and returns it as a pandas dataframe.
    @data (csv): The file in CSV-Format.
    @return (pd.Dataframe): The loaded CSV-File converted into a pandas Dataframe.
    '''
    return pd.read_csv(data)


@st.cache_resource
def get_pyg_html(df):
    '''
    Returns PyGWalker with the Data as html suitable for Streamlit.
    '''
    html = get_streamlit_html(df, spec="./gw0.json", use_kernel_calc=True, debug=False)
    return html


def main():
    df = None
    st.set_page_config(
        page_title = "Small Tableau",
        layout = "wide"
    )
    st.title("Small Tableau")
    
    init_streamlit_comm() # Initialize pygwalker communication
    
    with st.sidebar:
        st.header("Upload")
        st.markdown("This may take some seconds.")
        with st.form("Upload CSV-File"):
            file = st.file_uploader("Upload a .csv file", type=["csv"])
            submitted = st.form_submit_button("Submit")
        
        st.markdown('''<small>__Anleitung__<br>
                1. Wähle zuerst eine CSV-Datei mit den zu visualisierenden Daten aus und lade sie hoch.<br>
                2. Je nach Größe der Datei (Limit 200MB) dauert es einige Sekunden, bis die grafische Benutzeroberfläche von PyGWalker erscheint.<br>
                3. Verwende die grafische Oberfläche, um Daten ähnlich wie bei Tableau per Drag and Drop zu visualisieren.<br>
                <br>
                __Allgemeines__<br>
                Diese App verwendet [Python](https://www.python.org/), [Streamlit](https://streamlit.io/) und die [PyGWalker](https://kanaries.net/home/pygwalker) library.<br>
                Der Quelltext dieses Dashboards liegt auf [GitHub](https://github.com/alexmahesh/Tableau_Alternative).</small>''',
               unsafe_allow_html = True)
        
        st.markdown('''<small>__Impressum__<br>
                Verantwortlich für den Inhalt:<br>
                Alexander Schuppe<br>
                Email: spmail@aleku.eu<br>
                <br>
                __Datenschutz__<br>
                Dieses Dashboard speichert keine persönlichen Daten und verwendet keine Cookies.<br>
                Die Seite verwendet das kostenlose Hosting-Angebot von [Streamlit](https://streamlit.io/). Nähere Informationen zu deren Datenschutzangaben finden sie unter: [Streamlit Privacy Policy]().<br>
                <br>
                __Haftungsausschluss__<br>
                Es wird keine Garantie für die Funktionen der App übernommen.
                </small>''',
                unsafe_allow_html = True)
        
    if submitted:
        df = load_data(file)
        with st.expander("Data Table"):
            st.dataframe(df)
        # Visualize Data with PyGWalker
        stc.html(get_pyg_html(df), width=1300, height=1000, scrolling=True)


if __name__ == '__main__':
    main()