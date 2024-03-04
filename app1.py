import streamlit as st
from googletrans import Translator

# Function to translate text using Google Translate API
def translate_text(text, src_lang, tgt_lang):
    translator = Translator()
    translated = translator.translate(text, src=src_lang, dest=tgt_lang)
    return translated.text

# Streamlit UI
st.title("Machine Translation for All Languages")

src_lang = st.selectbox("Select source language:", ["English", "French", "German", "Spanish", "Italian", "Japanese"])
tgt_lang = st.selectbox("Select target language:", ["English", "French", "German", "Spanish", "Italian", "Japanese"])

input_text = st.text_area("Enter text to translate:")
if st.button("Translate"):
    if input_text:
        translated_text = translate_text(input_text, src_lang, tgt_lang)
        st.write("Translated text:")
        st.write(translated_text)
    else:
        st.warning("Please enter text to translate.")
