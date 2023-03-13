import streamlit as st
import openai

openai.api_key = st.secrets["api_key"]

def generate_flavor_profile(dish_input):
    prompt = (f"Generate a flavor profile for the dish {dish_input}.")
    response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=100)
    flavor_profile = response.choices[0].text.strip()
    return flavor_profile

def generate_wine_recommendations(flavor_profile, wine_preference, budget):
    prompt = (f"Generate 2 wine recommendations for a {wine_preference} wine under {budget} dollars that pair well with a {flavor_profile} dish. For the first wine, describe why it pairs well with the dish. For the second wine, describe why it pairs well with the dish.")
    response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=200)
    wine_recommendations = response.choices[0].text.strip()
    return wine_recommendations

def generate_cocktail_recommendations(flavor_profile, cocktail_preference):
    prompt = (f"Generate 2 cocktail recipes for a {cocktail_preference} cocktail that pairs well with a {flavor_profile} dish. For the first cocktail, describe why it pairs well with the dish. For the second cocktail, describe why it pairs well with the dish.")
    response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=200)
    cocktail_recommendations = response.choices[0].text.strip()
    return cocktail_recommendations

def generate_hard_liquor_recommendations(flavor_profile, liquor_preference):
    prompt = (f"Generate 2 {liquor_preference} liquor recommendations that pair well with a {flavor_profile} dish. For the first liquor, describe why it pairs well with the dish. For the second liquor, describe why it pairs well with the dish.")
    response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=200)
    liquor_recommendations = response.choices[0].text.strip()
    return liquor_recommendations

def generate_mocktail_recommendations(flavor_profile, mocktail_preference):
    prompt = (f"Generate 2 mocktail recipes for a {mocktail_preference} mocktail that pairs well with a {flavor_profile} dish. For the first mocktail, describe why it pairs well with the dish. For the second mocktail, describe why it pairs well with the dish.")
    response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=200)
    mocktail_recommendations = response.choices[0].text.strip()
    return mocktail_recommendations

def main():
    st.title("Pourfect Pairings")

    dish_input = st.text_input("Enter a dish or key ingredients:")
    drink_category = st.selectbox("What kind of drink would you like?", ["Wine", "Cocktails", "Hard Liquor", "Mocktails"])
    flavor_profile = generate_flavor_profile(dish_input)

    if drink_category == "Wine":
        wine_preference = st.selectbox("What kind of wine do you prefer?", ["Red", "White", "Rosé"])
        budget = st.slider("What's your budget for a bottle of wine?", 10, 100, 30)

        if st.button("Recommend Wines"):
            wine_recommendations = generate_wine_recommendations(flavor_profile, wine_preference, budget)
            st.write(wine_recommendations)
