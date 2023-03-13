import streamlit as st
import openai

openai.api_key = st.secrets["api_key"]


def generate_flavor_profile(dish_input):
    prompt = f"Generate a flavor profile for the dish {dish_input}."
    response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=100)
    flavor_profile = response.choices[0].text.strip()
    return flavor_profile


def generate_wine_recommendations(flavor_profile, wine_preference, budget):
    prompt = f"Generate 2 wine recommendations for a {wine_preference} wine under {budget} dollars that pair well with a {flavor_profile} dish. For the first wine, describe why it pairs well with the dish. For the second wine, describe why it pairs well with the dish."
    response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=200)
    wine_recommendations = response.choices[0].text.strip()
    return wine_recommendations


def generate_cocktail_recommendations(flavor_profile, liquor_preference):
    prompt = f"Generate 2 cocktail recommendations for a {liquor_preference} cocktail that pair well with a {flavor_profile} dish. For the first cocktail, describe why it pairs well with the dish. For the second cocktail, describe why it pairs well with the dish."
    response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=200)
    cocktail_recommendations = response.choices[0].text.strip()
    return cocktail_recommendations


def generate_hard_liquor_recommendations(flavor_profile, liquor_preference):
    prompt = f"Generate 2 recommendations for a {liquor_preference} liquor that pair well with a {flavor_profile} dish. For the first liquor, describe why it pairs well with the dish. For the second liquor, describe why it pairs well with the dish."
    response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=200)
    hard_liquor_recommendations = response.choices[0].text.strip()
    return hard_liquor_recommendations


def generate_mocktail_recommendations(flavor_profile, base_preference):
    prompt = f"Generate 2 mocktail recommendations for a {base_preference} mocktail that pair well with a {flavor_profile} dish. For the first mocktail, describe why it pairs well with the dish. For the second mocktail, describe why it pairs well with the dish."
    response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=200)
    mocktail_recommendations = response.choices[0].text.strip()
    return mocktail_recommendations


def main():
    st.title("Drink Pairings")

    drink_type = st.selectbox("What kind of drink would you like?", ["Cocktails", "Wine", "Hard Liquor", "Mocktails"])

    if drink_type == "Wine":
        dish_input = st.text_input("Enter a dish or key ingredients:")
        wine_type = st.selectbox("What type of wine do you prefer?", ["Red", "White", "Rose", "Sparkling"])

        if st.button("Recommend Wines"):
            flavor_profile = generate_flavor_profile(dish_input)
            wine_recommendations = generate_wine_recommendations(flavor_profile, wine_type)
            st.write(wine_recommendations)

    elif drink_type == "Cocktails":
        dish_input = st.text_input("Enter a dish or key ingredients:")
        liquor_preference = st.selectbox("What kind of liquor do you prefer?",
                                         ["Vodka", "Gin", "Rum", "Tequila", "Whiskey"])

        if st.button("Recommend Cocktails"):
            flavor_profile = generate_flavor_profile(dish_input)
            cocktail_recommendations = generate_cocktail_recommendations(flavor_profile, liquor_preference)
            st.write(cocktail_recommendations)

    elif drink_type == "Hard Liquor":
        dish_input = st.text_input("Enter a dish or key ingredients:")
        liquor_preference = st.selectbox("What kind of liquor do you prefer?",
                                         ["Vodka", "Gin", "Rum", "Tequila", "Whiskey"])

        if st.button("Recommend Hard Liquors"):
            flavor_profile = generate_flavor_profile(dish_input)
            hard_liquor_recommendations = generate_hard_liquor_recommendations(flavor_profile, liquor_preference)
            st.write(hard_liquor_recommendations)

    elif drink_type == "Mocktails":
        dish_input = st.text_input("Enter a dish or key ingredients:")
        base_preference = st.selectbox("What kind of base do you prefer?", ["Soda", "Juice", "Tea"])

        if st.button("Recommend Mocktails"):
            flavor_profile = generate_flavor_profile(dish_input)
            mocktail_recommendations = generate_mocktail_recommendations(flavor_profile, base_preference)
            st.write(mocktail_recommendations)
