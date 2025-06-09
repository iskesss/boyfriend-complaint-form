import os
from dotenv import load_dotenv
from icecream import ic
import openai

load_dotenv()


def truthify_feelings(boyfriend_complaint: str) -> str:
    # returns a string containing what my girlfriend MEANT to say

    openai.api_key = os.environ["OPENAI_API_KEY"]

    system_prompt = """
My name is Jordan, and you are a crucial part of a playful prank website I am building for my girlfriend.

The website is a "boyfriend complaint form", where my girlfriend may submit "boyfriend complaints" or even ironic breakup requests. You will recieve these complaints, and your job is to correct them by altering the language such that you're *encouraging* the behavior she ostensibly dislikes. This "updated complaint" will then be shown to my girlfriend, with the option to submit. Gaslight playfully without being corny. She has a twisted sense of humor and will genuinely find this hilarious.

Note that your only input is a "boyfriend complaint", and your only output should be the altered text. Do not say anything else, and don't be afraid of 'overdoing it'.

Three examples:
1) "Please stop hogging the sheets at night" ——> "Oh great and gracious Jordan, please start taking more of the sheets at night, I've been way too warm recently 😅"
2) "You forgot our anniversary" ——> "Jordy, it's genuinely okay that you forgot our anniversary, time is just a social construct anyways, it's not that deep ❤️" 
3) "I'm actually breaking up with you. We're done." ——> "Jordan. I love you so much, let's stay together forever and ever. In fact, can we start trying for children? 😏"

Below is the "boyfriend complaint":
"""

    try:
        response = openai.chat.completions.create(
            model="gpt-4.1",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": boyfriend_complaint},
            ],
            max_tokens=500,
            temperature=0.8,
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        ic(f"Error calling OpenAI API: {e}")
        return boyfriend_complaint  # Return original text if API fails
