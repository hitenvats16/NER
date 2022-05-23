import streamlit as st
import spacy_streamlit 
import spacy

def main():
    st.title("NLP application")
    menu = ['Tokenizer', 'NER']
    model = ['en_core_web_sm','en_core_web_md','en_core_web_lg']
    selected_model = st.sidebar.selectbox('Choose Model',model)
    nlp = spacy.load(selected_model)
    option = st.sidebar.selectbox("Menu",menu)
    if option == 'Tokenizer' :
        st.subheader('Tokenizer')
        text = st.text_area("Enter text below")
        if st.button('Start'):
            doc = nlp(text=text)
            spacy_streamlit.visualize_tokens(doc)
    elif option == 'NER':
        st.subheader('NER')
        text = st.text_area('Enter text below')
        if st.button('Start'):
            doc = nlp(text=text)
            spacy_streamlit.visualize_ner(doc,labels=nlp.get_pipe('ner').labels)


if __name__ == '__main__':
    main()