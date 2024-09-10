import streamlit as st
from googletrans import Translator, LANGUAGES

# Initialize Google Translator
translator = Translator()

# Function to get language code from language name
def get_language_code(language_name):
    for lang_code, lang_name in LANGUAGES.items():
        if lang_name.lower() == language_name.lower():
            return lang_code
    return None

# Custom CSS for dark mode styling
st.markdown("""
    <style>
    body {
        background-color: #2C2C2C;
        color: #F0F0F0;
    }
    .stTextInput, .stTextArea, .stButton {
        font-size: 16px !important;
        font-family: 'Verdana', sans-serif;
    }
    h1, h2, h3, p {
        text-align: left;
        color: #E0E0E0;
        font-family: 'Arial', sans-serif;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        padding: 10px 24px;
        border: none;
        border-radius: 8px;
        transition: background-color 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #45a049;
    }
    .stTextInput input {
        background-color: #4F4F4F;
        color: white;
        border-radius: 8px;
        border: 1px solid #4CAF50;
        padding: 10px;
    }
    .stTextArea textarea {
        background-color: #4F4F4F;
        color: white;
        border-radius: 8px;
        border: 1px solid #4CAF50;
        padding: 10px;
    }
    .footer {
        text-align: center;
        padding-top: 30px;
        font-size: 14px;
        color: #999999;
    }
    </style>
    """, unsafe_allow_html=True)

# Main UI design
st.title("Language Translator")
st.write("Translate text from one language to another in a sleek, dark interface.")

# Input text box
st.subheader("Enter Text for Translation:")
source_text = st.text_area("Type or paste the text here:", "", height=150)

# Source language selection
st.subheader("Source Language:")
source_lang = st.selectbox("Choose the source language:", ["English", "French", "Spanish", "German", "Italian"])

# Target language input (with predefined suggestions)
st.subheader("Target Language:")
target_language_search = st.text_input("Search target language (e.g., Japanese, Russian, Arabic):")

# Translate button logic
if st.button("Translate"):
    if not source_text:
        st.error("Please enter some text to translate.")
    elif not target_language_search:
        st.error("Please enter a target language.")
    else:
        # Convert language name to code
        target_lang_code = get_language_code(target_language_search)
        if target_lang_code is None:
            st.error(f"⚠ '{target_language_search}' is not a valid language. Please try again.")
        else:
            try:
                # Perform translation
                translation = translator.translate(source_text, src=source_lang[:2].lower(), dest=target_lang_code)
                st.success(f"**Translation Result**: {translation.text}")
            except Exception as e:
                st.error(f"An error occurred during translation: {e}")

# Optional supported languages list
if st.checkbox("Supported Languages (click to expand)"):
    st.subheader("Supported Language List:")
    st.write(", ".join([lang_name.capitalize() for lang_name in LANGUAGES.values()]))

# Footer styling
st.markdown("""
    <div class="footer">
        <p>Powered by Streamlit | Translations via Google Translate API</p>
    </div>
    """, unsafe_allow_html=True)
