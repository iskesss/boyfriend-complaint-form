import streamlit as st
import os
import json
import requests
from streamlit_extras.let_it_rain import rain

# Page configuration
st.set_page_config(
    page_title="Boyfriend Complaint Portal",
    page_icon="💌",
)

# Inject CSS to import the Open Sans font and style buttons
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Open+Sans&display=swap');
    
    /* Apply Open Sans to the entire app */
    [data-testid="stAppViewContainer"] * {
        font-family: 'Open Sans', sans-serif !important;
    }
    
    /* Target all possible button selectors for Submit button (green) */
    div[data-testid="column"]:nth-child(1) button,
    div[data-testid="column"]:nth-child(1) [data-testid="baseButton-secondary"],
    div[data-testid="column"]:nth-child(1) [data-testid="baseButton-primary"],
    button[key="submit_correction"] {
        background-color: #00cc88 !important;
        color: white !important;
        border: 1px solid #00cc88 !important;
        border-radius: 0.5rem !important;
    }
    
    div[data-testid="column"]:nth-child(1) button:hover,
    div[data-testid="column"]:nth-child(1) [data-testid="baseButton-secondary"]:hover,
    div[data-testid="column"]:nth-child(1) [data-testid="baseButton-primary"]:hover,
    button[key="submit_correction"]:hover {
        background-color: #00aa77 !important;
        border-color: #00aa77 !important;
        color: white !important;
    }
    
    /* Target all possible button selectors for Cancel button (red) */
    div[data-testid="column"]:nth-child(2) button,
    div[data-testid="column"]:nth-child(2) [data-testid="baseButton-secondary"],
    div[data-testid="column"]:nth-child(2) [data-testid="baseButton-primary"],
    button[key="cancel_correction"] {
        background-color: #ff4b4b !important;
        color: white !important;
        border: 1px solid #ff4b4b !important;
        border-radius: 0.5rem !important;
    }
    
    div[data-testid="column"]:nth-child(2) button:hover,
    div[data-testid="column"]:nth-child(2) [data-testid="baseButton-secondary"]:hover,
    div[data-testid="column"]:nth-child(2) [data-testid="baseButton-primary"]:hover,
    button[key="cancel_correction"]:hover {
        background-color: #ff3333 !important;
        border-color: #ff3333 !important;
        color: white !important;
    }
    
    /* Force red styling on second column button */
    div[data-testid="column"]:nth-child(2) > div > button {
        background-color: #ff4b4b !important;
        color: white !important;
        border: 1px solid #ff4b4b !important;
    }
    
    div[data-testid="column"]:nth-child(2) > div > button:hover {
        background-color: #ff3333 !important;
        border-color: #ff3333 !important;
    }

    /* Alternative: Use a more specific class-based approach */
    [data-testid="stButton"] > button[kind="secondary"] {
        background-color: inherit !important;
    }
    
    [data-testid="stButton"]:first-of-type > button {
        background-color: #00cc88 !important;
        color: white !important;
        border: 1px solid #00cc88 !important;
    }
    
    [data-testid="stButton"]:first-of-type > button:hover {
        background-color: #00aa77 !important;
        border-color: #00aa77 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("💌 Boyfriend Complaint Form")
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
        label="*:blue[did you mean...]*",
        value=st.session_state["corrected_complaint"],
        height=200,
        disabled=True,
        key="corrected_display",
    )

    col1, col2, col3 = st.columns([1, 1, 2])

    with col1:
        if st.button("Submit to Boyfriend ✅", key="submit_correction"):
            # Trigger a little celebration effect
            rain(emoji="💌")
            st.success("Your corrected complaint has been submitted!")
            # Clear the session state so the form resets
            del st.session_state["corrected_complaint"]
            st.rerun()

    with col2:
        if st.button("Don't not Submit to Boyfriend ❌❌", key="cancel_correction"):
            # Discard the corrected version and let the user start over
            del st.session_state["corrected_complaint"]
            st.rerun()
