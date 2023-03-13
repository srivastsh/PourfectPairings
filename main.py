import streamlit as st
import openai

openai.api_key = st.secrets["api_key"]


def generate_pairings(dish_input, drink_type, subcategory):
    if drink_type == "Wine":
        prompt = (
            f"Generate 2 wine recommendations for a {subcategory} wine that pair well with a {dish_input} dish. For the first wine, describe why it pairs well with the dish. For the second wine, describe why it pairs well with the dish.")
    elif drink_type == "Cocktail":
        prompt = (
            f"Generate 2 cocktail recommendations for a {subcategory} cocktail that pairs well with a {dish_input} dish. For the first cocktail, describe why it pairs well with the dish. For the second cocktail, describe why it pairs well with the dish.")
    elif drink_type == "Hard Liquor":
        prompt = (
            f"Generate 2 hard liquor recommendations for a {subcategory} liquor that pairs well with a {dish_input} dish. For the first liquor, describe why it pairs well with the dish. For the second liquor, describe why it pairs well with the dish.")
    else:
        prompt = (
            f"Generate 2 mocktail recommendations for a {subcategory} mocktail that pair well with a {dish_input} dish. For the first mocktail, describe why it pairs well with the dish. For the second mocktail, describe why it pairs well with the dish.")

    response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=200)
    pairings = response.choices[0].text.strip()
    return pairings


def main():
    st.title("Pourfect Pairings")

    drink_type = st.selectbox("What kind of drink would you like?", ["Wine", "Cocktail", "Hard Liquor", "Mocktail"])

    if drink_type == "Wine":
        subcategory = st.selectbox("What type of wine would you like?", ["Red", "White", "Rosé"])
        budget = st.slider(
            "What's your budget for a bottle of wine?", 10, 100, 10, step=5,
            format_func=lambda x: "100+" if x == 100 else str(x))
        if budget == 100:
            budget_range = "100+"
        else:
            budget_range = f"{budget}-{budget + 10}"

        else:
            budget_range = f"{budget}-{budget + 10}"
    elif drink_type == "Cocktail":
        subcategory = st.selectbox("What type of cocktail would you like?",
                                   ["Gin-based", "Vodka-based", "Rum-based", "Tequila-based", "Whiskey-based"])
    elif drink_type == "Hard Liquor":
        subcategory = st.selectbox("What type of hard liquor would you like?",
                                   ["Gin", "Vodka", "Rum", "Tequila", "Whiskey"])
    else:
        subcategory = st.selectbox("What type of mocktail would you like?",
                                   ["Fruity", "Citrusy", "Herbal", "Minty", "Creamy"])

    dish_input = st.text_input("Enter a dish or key ingredients:")

    if st.button("Recommend Pairings"):
        pairings = generate_pairings(dish_input, drink_type, subcategory)
        st.write(pairings)


if __name__ == "__main__":
    main()
