import streamlit as st
from googletrans import Translator, LANGUAGES

# Function to translate text
def translate_text(input_text, target_language):
    translator = Translator()
    translated_text = translator.translate(input_text, dest=target_language)
    return translated_text.text

# Streamlit app
def main():
    st.title("Google Translate App")
    st.write("Translate text to any language supported by Google Translate.")

    # Input text box
    input_text = st.text_area("Enter text to translate:", "")

    # Target language selection
    target_language = st.selectbox("Select target language:", sorted(LANGUAGES.values()))

    if st.button("Translate"):
        if input_text.strip() != "":
            translated_text = translate_text(input_text, target_language)
            st.write("Translated text:", translated_text)
        else:
            st.warning("Please enter some text to translate.")

if __name__ == "__main__":
    main()
