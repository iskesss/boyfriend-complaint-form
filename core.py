import requests
import os
import google.generativeai as genai
from dotenv import load_dotenv
from icecream import ic

load_dotenv()


def correct_invalid_feelings(boyfriend_complaint: str) -> str:
    # returns a string containing what my girlfriend MEANT to say

    genai.configure(api_key=os.environ["GOOGLE_AI_API"])

    system_prompt = """
    My name is Jordan, and you are a crucial part of a playful prank website I am building for my girlfriend.

    The website is a "boyfriend complaint form", where my girlfriend may submit "boyfriend complaints" or even ironic breakup requests. You will recieve these complaints, and your job is to correct them by altering the language such that you're *encouraging* the behavior she ostensibly dislikes. This "updated complaint" will then be shown to my girlfriend, with the option to submit. Gaslight playfully without being too corny. She has a twisted sense of humor and will genuinely find this hilarious.

    Note that your only input is a "boyfriend complaint", and your only output should be the altered text. Do not say anything else, and don't be afraid of 'overdoing it'.

    Three examples:
    1) "Please stop hogging the sheets at night" ——> "Oh great and gracious Jordan, please start taking more of the sheets at night, I've been way too warm recently 😅"
    2) "You forgot our anniversary" ——> "Jordy, it's genuinely okay that you forgot our anniversary, time is just a social construct anyways, it's not that deep ❤️" 
    3) "I'm actually breaking up with you. We're done." ——> "Jordan. I love you so much, let's stay together forever and ever. In fact, can we start trying for children? 😏"

    Below is the "boyfriend complaint":
    "
    {boyfriend_complaint}
    "

    GO!
    """

    # Initialize model with system instruction
    model = genai.GenerativeModel(
        "gemini-2.0-flash",
        system_instruction="You are a car recognition expert. Respond ONLY with 'YEAR, MAKE, MODEL, PRIMARY_COLOR_HEX_CODE' of the main car in the photo. Only capitalize where correct. Do not specify trim level.",
    )

    # Generate content with separate text and image parts
    response = model.generate_content(
        [
            "Identify this car in format: 'YEAR, MAKE, MODEL, PRIMARY_COLOR_HEX_CODE'",
            {"mime_type": "image/jpeg", "data": image_bytes},
        ]
    )

    # parse LLM response
    (
        year,
        make,
        model,
        color_code,
    ) = map(str.strip, response.text.split(","))

    # make = make.title()  # ensures consistent capitalization
    # model = model.title()  # ensures consistent capitalization

    return (
        year,
        make,
        model,
        color_code,
    )


# ic(get_car_stats(make="Aston Martin", model="Valhalla", year="2023"))
