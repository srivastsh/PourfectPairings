import streamlit as st
import openai
from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgb

def image(src_as_string, **style):
    return img(src=src_as_string, style=styles(**style))

def link(link, text, **style):
    return a(_href=link, _target="_blank", style=styles(**style))(text)

def layout(*args):
    style = """
    <style>
      #MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
     .stApp { bottom: 105px; }
    </style>
    """

    style_div = styles(
        position="fixed",
        left=0,
        bottom=0,
        margin=px(0, 0, 0, 0),
        width=percent(100),
        color="black",
        text_align="center",
        height="auto",
        opacity=1
    )

    style_hr = styles(
        display="block",
        margin=px(8, 8, "auto", "auto"),
        border_style="inset",
        border_width=px(2)
    )

    body = p()
    foot = div(
        style=style_div
    )(
        hr(
            style=style_hr
        ),
        body
    )

    st.markdown(style, unsafe_allow_html=True)

    for arg in args:
        if isinstance(arg, str):
            body(arg)

        elif isinstance(arg, HtmlElement):
            body(arg)

    st.markdown(str(foot), unsafe_allow_html=True)

def footer():
    myargs = [
        "Made in ",
        image('https://avatars3.githubusercontent.com/u/45109972?s=400&v=4',
              width=px(25), height=px(25)),
        " with ❤️ by ",
        link("https://srivastsh.com", "@srivastsh"),
    ]
    layout(*myargs)

openai.api_key = st.secrets["api_key"]

st.set_page_config(page_title='PourfectPairings', page_icon="🍷")
st.title("Pourfect Pairings")

hide_st_style = """
    <style>
        #MainMenu {visibility: hidden;}
        /* footer {visibility: hidden;} */
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

    dish_input = st.text_input("Enter a dish or the key ingredients:")

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