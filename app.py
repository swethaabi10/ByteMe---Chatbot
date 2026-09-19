import os
import requests
import streamlit as st

# Load API key securely from Streamlit secrets
api_key = st.secrets["GEMINI_API_KEY"]

# Set updated Gemini model name
# Options for new API keys: "gemini-3.6-flash", "gemini-3.5-flash", or "gemini-3.1-flash-lite"
model = "gemini-3.6-flash"
endpoint = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"

# Set custom styling and background
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("BackgroundPic.png");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def get_response(query):
    headers = {"Content-Type": "application/json"}
    params = {"key": api_key}
    data = {"contents": [{"parts": [{"text": query}]}]}

    try:
        response = requests.post(endpoint, headers=headers, params=params, json=data)

        if response.status_code == 200:
            response_json = response.json()
            return response_json["candidates"][0]["content"]["parts"][0]["text"]
        else:
            return f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"An error occurred: {str(e)}"


def main():
    st.title("HELLO I'M ByteMe AI Chatbot")
    query = st.text_input("You: ")
    if query:
        response = get_response(query)
        st.write("BHEEMA AI: ", response)


if __name__ == "__main__":
    main()
