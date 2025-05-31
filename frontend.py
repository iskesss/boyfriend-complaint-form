import streamlit as st
import os
import json
from streamlit_extras.let_it_rain import rain
from core import correct_invalid_feelings

# Get port from environment variable
PORT = int(os.getenv("PORT", "8080"))
# Page configuration
st.set_page_config(page_title="Boyfriend Complaint Form", page_icon="💝", layout="wide")


def main_page():
    # Inject CSS to import the Roboto font and force it on all app elements <— NOTE: FIND DIFFERENT FONT ??
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');
        /* Target the main container and all of its children */
        [data-testid="stAppViewContainer"] * {
            font-family: 'Roboto', sans-serif !important;
        }
        """,
        unsafe_allow_html=True,
    )

    st.title(body=":red[Boyfriend Complaint Form]")
    st.markdown(body="***Your feelings matter more than anything*** 💝💝💝")

    with st.form(
        "my_form",
        enter_to_submit=True,
    ):
        st.write("Inside the form")
        st.text_area("Write complaint below")
        checkbox_val = st.checkbox("Form Checkbox")

        # Every form must have a submit button
        with st.spinner("Processing your request....", show_time=True):
            submitted = st.form_submit_button("Submit")
        if submitted:
            st.write(
                "remember to make balloons fall upon form submission (streamlit let_it_rain)"
            )

    with st.expander(label="What is this wondrous website?", icon="😍"):
        st.markdown(
            """
            #### Think Pokémon GO for car spotters. Snap photos of real cars to collect, trade, and track them.
            **Are you a car enthusiast? Are you trying to become one? Let's gamify that.**

            ---
            ***My Vision (future roadmap):***

            📲 Free mobile app

            🎴 Car cards with rarity tiers (⚪ 🟢 🔵 🟣 🟠)

            🎁 Trade cards with other users

            📍 Sightings are geotagged, fueling a live **community-driven map** 🗺️ — spot rare cars near you, thanks to fellow enthusiasts!

            🚫 No monetization, no NFTs—just a fun way to share experiences
            
            ---
            **Author:** [Jordan Bouret](https://www.linkedin.com/in/jordan-bouret/) |
            **Version:** 1.0.0 |
            **GitHub Repo:** [Here](https://github.com/iskesss/trading-cars)
        """
        )


main_page()
