import streamlit as st
import os
import json
import requests
from streamlit_extras.let_it_rain import rain

# Page configuration
st.set_page_config(
    page_title="Boyfriend Complaint Portal", page_icon="💝", layout="wide"
)

# Inject CSS to import the Open Sans font and force it on all app elements
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Open+Sans&display=swap');
    /* Apply Open Sans to the entire app */
    [data-testid="stAppViewContainer"] * {
        font-family: 'Open Sans', sans-serif !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("💝 Boyfriend Complaint Form")
st.markdown("***Your feelings matter more than anything*** 💝💝💝")


def autocorrect_api(text: str) -> str:
    """
    Sends the given text to the autocorrect AI agent API and returns
    the corrected version. Expects the API to respond with JSON containing
    a 'corrected_text' field.
    """
    # Placeholder: return the original text for now.
    # Replace this with a real API call as needed.
    return text


# If there's no corrected complaint in session state, prompt for input and autocorrect
if "corrected_complaint" not in st.session_state:
    # Text area for the user to write their complaint
    complaint = st.text_area(
        label="Write your boyfriend complaint below:", height=200, key="complaint_input"
    )

    # Button to trigger the autocorrect API
    if st.button("Run Autocorrect"):
        if not complaint.strip():
            st.warning("You didn't write anything 🙄")
            st.stop()  # Don't proceed further until they enter text
        with st.spinner("Running autocorrect on your complaint..."):
            corrected_complaint = autocorrect_api(complaint)
        if corrected_complaint:
            # Store the corrected version in session state so it persists
            st.session_state["corrected_complaint"] = corrected_complaint
            # Continue on to show the corrected complaint below in the same run
        else:
            st.error("Received an empty response from the autocorrect service.")
            st.stop()

    else:
        # If they haven't clicked "Run Autocorrect" yet, stop here so only the input is shown
        st.stop()


# At this point, "corrected_complaint" must be in session state
st.markdown("---")
st.subheader("*:blue[did you mean...]*")
st.text_area(
    label="",
    value=st.session_state["corrected_complaint"],
    height=200,
    disabled=True,
    key="corrected_display",
)

col1, col2 = st.columns(2)
with col1:
    if st.button("Submit Correction", key="submit_correction"):
        # Trigger a little celebration effect
        rain()
        st.success("Your corrected complaint has been submitted!")
        # Clear the session state so the form resets
        del st.session_state["corrected_complaint"]

with col2:
    if st.button("Cancel", key="cancel_correction"):
        # Discard the corrected version and let the user start over
        del st.session_state["corrected_complaint"]
