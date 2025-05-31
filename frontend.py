import streamlit as st
import os
import json
import requests
import time
from streamlit_extras.let_it_rain import rain

# Page configuration
st.set_page_config(
    page_title="Boyfriend Complaint Portal",
    page_icon="💌",
)

# Inject CSS to import the Open Sans font and make all buttons green
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Open+Sans&display=swap');
    
    /* Apply Open Sans to the entire app */
    [data-testid="stAppViewContainer"] * {
        font-family: 'Open Sans', sans-serif !important;
    }
    
    /* Make all buttons green */
    [data-testid="stButton"] > button {
        background-color: #00cc88 !important;
        color: white !important;
        border: 1px solid #00cc88 !important;
        border-radius: 0.5rem !important;
    }
    
    [data-testid="stButton"] > button:hover {
        background-color: #00aa77 !important;
        border-color: #00aa77 !important;
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("💌 Boyfriend Complaint Form")
st.markdown("***Your feelings matter more to me than anything*** 💝💝💝")


def autocorrect_api(text: str) -> str:
    """
    Sends the given text to the autocorrect AI agent API and returns
    the corrected version. Expects the API to respond with JSON containing
    a 'corrected_text' field.
    """
    # Placeholder: return the original text for now.
    # Replace this with a real API call as needed.
    return text


# Show input section only if there's no corrected complaint in session state
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
            # Force a rerun to hide the input and show the corrected version
            st.rerun()
        else:
            st.error("Received an empty response from the autocorrect service.")
            st.stop()

# Show corrected complaint section only if there's a corrected complaint in session state
if "corrected_complaint" in st.session_state:
    st.text_area(
        label="*:blue[I think you meant to say...]*",
        value=st.session_state["corrected_complaint"],
        height=200,
        disabled=True,
        key="corrected_display",
    )

    col1, col2, col3 = st.columns([1, 1, 2])

    with col1:
        if st.button("Submit to Boyfriend ✅", key="submit_correction"):
            # Trigger a little celebration effect
            st.balloons()
            st.success("Your complaint has been submitted!")
            # Wait a bit for the rain animation to display
            time.sleep(3)
            # Clear the session state so the form resets
            del st.session_state["corrected_complaint"]
            st.rerun()

    with col2:
        if st.button("Don't not Submit to Boyfriend ❌❌", key="cancel_correction"):
            # PRANK: This button now does the exact same thing as the submit button!
            # Trigger a little celebration effect
            st.balloons()
            st.success("Your complaint has been submitted!")
            # Wait a bit for the rain animation to display
            time.sleep(3)
            # Clear the session state so the form resets
            del st.session_state["corrected_complaint"]
            st.rerun()
