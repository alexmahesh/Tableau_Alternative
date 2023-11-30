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
    st.title("Small Tableau")



if __name__ == '__main__':
    main()