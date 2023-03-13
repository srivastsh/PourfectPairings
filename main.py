import streamlit as st
import openai

openai.api_key = os.environ.get("OPENAI_API_KEY")
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

def main():
    st.title("Pourfect Pairings")

    dish_input = st.text_input("Enter a recipe or key ingredients:")
    wine_preference = st.selectbox("What kind of wine do you prefer?", ["Red", "White", "Rosé"])
    budget = st.slider("What's your budget for a bottle of wine?", 10, 100, 30)

    if st.button("Recommend Wines"):
        flavor_profile = generate_flavor_profile(dish_input)
        wine_recommendations = generate_wine_recommendations(flavor_profile, wine_preference, budget)
        st.write(wine_recommendations)

if __name__ == "__main__":
    main()
