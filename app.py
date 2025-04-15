import streamlit as st
from main import answer_question_1

# Example function to simulate the bot's response
def get_bot_response(user_input):
    # Here you will integrate your RAG model logic to fetch answers
    answer = answer_question_1(user_input)

    return answer

# UI Setup
st.title("Concert Tour Information Bot")

# Text input field for user request
user_input = st.text_input("Ask me a question or add a document:")

# Button to trigger response
if st.button("Get Response"):
    if user_input:
        bot_response = get_bot_response(user_input)
        st.write(f"**Bot's Response:** {bot_response}")
    else:
        st.write("Please enter a question or document.")
