import streamlit as st
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="AIzaSyBOPX769Cryd3M76WgQOCxKGGUO9aFKl3o")

page_bg_color = """
<style>
    body {
        background-color: #f5f5dc;  /* Light Beige Background */
        font-family: 'Arial', sans-serif;
    }
    .stApp {
        background: rgba(255, 255, 255, 0.9);
        padding: 2rem;
        border-radius: 10px;
    }
    h1 {
        color: #FF5733;
        text-align: center;
        font-size: 3rem;
        font-weight: bold;
    }
    .stTextInput, .stSelectbox {
        border-radius: 10px;
        border: 2px solid #FF5733;
        padding: 10px;
    }
    .stButton>button {
        background-color: #FF5733;
        color: white;
        padding: 10px 20px;
        border-radius: 5px;
        font-size: 1.2rem;
        border: none;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #E74C3C;
    }
    .recipe-box {
        background: white;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 2px 2px 20px rgba(0, 0, 0, 0.2);
    }
    .recipe-box h3 {
        color: #27AE60;
        text-align: center;
        font-size: 1.8rem;
    }
</style>
"""
st.markdown(page_bg_color, unsafe_allow_html=True)

def generate_recipe(ingredients, cuisine):
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"Create a detailed recipe using {ingredients}. The cuisine should be {cuisine}."
    response = model.generate_content(prompt)
    return response.text if response else "No response from AI."

st.title("Flavour Fusion: AI-Driven Recipe Blogging")

ingredients = st.text_input("Enter Receipe Name:")
cuisine = st.selectbox("Choose a cuisine:", ["Italian", "Mexican", "Indian", "Chinese", "French"])

if st.button("Generate Recipe"):
    recipe = generate_recipe(ingredients, cuisine)
    st.write(recipe)
