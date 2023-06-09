import streamlit as st
import openai

openai.api_key = st.secrets["api_key"]

st.set_page_config(page_title='PourfectPairings', page_icon="🍷")
st.title("Pourfect Pairings")
st.write("Find the perfect drink pairing for your dish. Enter a dish or key ingredients, select your preferred drink type, and let the app generate a perfect pairing for you.")

hide_st_style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)
def generate_pairings(dish_input, drink_type, subcategory):
    if drink_type == "Wine":
        prompt = (
            f"Generate 2 wine recommendations for {subcategory} wine that pair well with a {dish_input} dish. For the first wine, describe why it pairs well with the dish. For the second wine, describe why it pairs well with the dish.")
    elif drink_type == "Cocktail":
        prompt = (
            f"Generate 2 cocktail recommendations for {subcategory} cocktail that pairs well with a {dish_input} dish. For the first cocktail, describe why it pairs well with the dish. For the second cocktail, describe why it pairs well with the dish.")
    elif drink_type == "Hard Liquor":
        prompt = (
            f"Generate 2 hard liquor recommendations for {subcategory} liquor that pair well with a {dish_input} dish. For the first liquor, describe why it pairs well with the dish. For the second liquor, describe why it pairs well with the dish.")
    elif drink_type == "Beer":
        prompt = (
            f"Generate 2 beer recommendations for {subcategory} beer that pair well with a {dish_input} dish. For the first beer, describe why it pairs well with the dish. For the second beer, describe why it pairs well with the dish.")
    else:
        prompt = (
            f"Generate 2 drink recommendations for {subcategory} that pair well with a {dish_input} dish. For the first drink, describe why it pairs well with the dish. For the second drink, describe why it pairs well with the dish.")
    response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=200)
    pairings = response.choices[0].text.strip()
    return pairings
def main():
    dish_input = st.text_input("Enter a dish or the key ingredients (e.g., 'chicken', 'tomatoes'):", placeholder="e.g., 'chicken', 'tomatoes'")

    drink_type = st.selectbox("What kind of drink would you like?", ["Any", "Wine", "Cocktail", "Hard Liquor", "Beer", "Mocktail"])
    if drink_type != "Any":
        if drink_type == "Wine":
            subcategory = st.selectbox("What type of wine would you like?", ["Any", "Red", "White", "Rosé"])
            budget = st.slider("What's your budget for a bottle of wine?", 10, 100, 25, step=5)
            if budget == 100:
                budget_range = "100+"
            else:
                budget_range = f"{budget}-{budget + 10}"
        elif drink_type == "Cocktail":
            subcategory = st.selectbox("What type of cocktail would you like?",
                                       ["Any","Gin-based", "Vodka-based", "Rum-based", "Tequila-based", "Whiskey-based"])
        elif drink_type == "Hard Liquor":
            subcategory = st.selectbox("What type of hard liquor would you like?",
                                       ["Any","Gin", "Vodka", "Rum", "Tequila", "Whiskey"])
        elif drink_type == "Beer":
            subcategory = st.selectbox("What type of beer would you like?",
                                       ["Any","Pale Ale", "IPA", "Stout", "Porter", "Wheat Beer"])
        else:
            subcategory = st.selectbox("What type of mocktail would you like?",
                                       ["Any", "Fruity", "Citrusy", "Herbal", "Minty", "Creamy"])
    if st.button("Recommend Pairings"):
        pairings = generate_pairings(dish_input, drink_type, subcategory)
        st.write(pairings)
if __name__ == "__main__":
    main()