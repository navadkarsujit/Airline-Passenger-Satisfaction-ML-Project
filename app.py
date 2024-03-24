import streamlit as st
import pickle

pickle_in=open('LRmodel.pkl', 'rb')
LRmodel=pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def main():
    st.title("Bank Authenticator")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)

if __name__=='__main__':
    main()
    
#python -m streamlit run app.py