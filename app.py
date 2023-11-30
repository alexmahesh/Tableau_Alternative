import streamlit as st
import streamlit.components.v1 as stc
import pandas as pd
import pygwalker as pyg


@st.cache_resource
def load_data(data):
    '''
    Loads a CSV-File and returns it as a pandas dataframe.
    @data (csv): The file in CSV-Format.
    @return (pd.Dataframe): The loaded CSV-File converted into a pandas Dataframe.
    '''
    return pd.read_csv(data)


def main():
    df = None
    
    st.set_page_config(
        page_title = "Small Tableau",
        layout = "wide"
    )
    st.title("Small Tableau")
    
    with st.sidebar:
        st.header("Upload")
        with st.form("Upload CSV-File"):
            file = st.file_uploader("Upload a .csv file", type=["csv"])
            submitted = st.form_submit_button("Submit")
    if submitted:
        df = load_data(file)
        st.dataframe(df)



if __name__ == '__main__':
    main()