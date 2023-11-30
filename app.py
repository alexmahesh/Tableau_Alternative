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
        with st.form("Upload CSV-File"):
            file = st.file_uploader("Upload a .csv file", type=["csv"])
            submitted = st.form_submit_button("Submit")
            
    if submitted:
        df = load_data(file)
        with st.expander("Data Table"):
            st.dataframe(df)
        # Visualize Data with PyGWalker
        stc.html(get_pyg_html(df), width=1300, height=1000, scrolling=True)


if __name__ == '__main__':
    main()