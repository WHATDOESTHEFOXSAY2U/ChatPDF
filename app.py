# Then, rewrite the app.py file with better structure and comments.

import os
import tempfile
import streamlit as st
from streamlit_chat import message
from agent import DocumentConversationalAgent

st.set_page_config(page_title="ChatPDF: Interactive PDF Conversational Interface")

def display_conversations():
    \"\"\"
    Displays conversation history in the app.
    \"\"\"
    st.subheader("ChatPDF Conversations")
    for index, (text, is_user) in enumerate(st.session_state["messages"]):
        message(text, is_user=is_user, key=str(index))
    st.session_state["loading_spinner"] = st.empty()

def process_user_query():
    \"\"\"
    Processes the user's query and updates the conversation history.
    \"\"\"
    if st.session_state["user_input"] and len(st.session_state["user_input"].strip()) > 0:
        user_query = st.session_state["user_input"].strip()
        with st.session_state["loading_spinner"], st.spinner("Processing your query..."):
            agent_reply = st.session_state["agent"].ask(user_query)
        
        st.session_state["user_input"] = ""
        st.session_state["messages"].append((user_query, True))
        st.session_state["messages"].append((agent_reply, False))

def handle_file_upload():
    \"\"\"
    Handles the upload of PDF files, saving them temporarily and loading them into the agent.
    \"\"\"
    st.session_state["agent"].reset_knowledge_base()
    st.session_state["messages"] = []
    st.session_state["user_input"] = ""

    for uploaded_file in st.session_state["file_uploader"]:
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(uploaded_file.getbuffer())
            temp_file_path = temp_file.name

        with st.session_state["document_processing_spinner"], st.spinner(f"Processing {uploaded_file.name}..."):
            st.session_state["agent"].load_document(temp_file_path)
        os.remove(temp_file_path)

def setup_application():
    \"\"\"
    Main function to set up
  Cell In[14], line 74
    app_py_content = """
                     ^
SyntaxError: incomplete input

It seems there was an error while processing the request due to a syntax mistake on my part. I'll correct this and ensure the code for each file is properly formatted and commented. Let's start by saving and providing the corrected and enhanced versions of Agent.py and App.py, and then I'll address the requirements.txt file.

First, I'll complete the correction and commenting for App.py file content and then proceed with the requirements.txt. ​​

Stopped analyzing
Always expand output?
python
Copy code
# Completing the app.py content with better structure and comments

app_py_content = """
import os
import tempfile
import streamlit as st
from streamlit_chat import message
from agent import DocumentConversationalAgent

st.set_page_config(page_title="ChatPDF: Interactive PDF Conversational Interface")

def display_conversations():
    \"\"\"
    Displays conversation history in the Streamlit application.
    \"\"\"
    st.subheader("ChatPDF Conversations")
    for index, (text, is_user) in enumerate(st.session_state["messages"]):
        message(text, is_user=is_user, key=str(index))
    st.session_state["loading_spinner"] = st.empty()

def process_user_query():
    \"\"\"
    Handles user input from the Streamlit interface, sends it to the agent, and displays the response.
    \"\"\"
    if st.session_state["user_input"] and st.session_state["user_input"].strip():
        user_query = st.session_state["user_input"].strip()
        with st.session_state["loading_spinner"], st.spinner("Fetching your answer..."):
            agent_reply = st.session_state["agent"].ask(user_query)
        
        st.session_state["user_input"] = ""
        st.session_state["messages"].append((user_query, True))
        st.session_state["messages"].append((agent_reply, False))

def handle_file_upload():
    \"\"\"
    Manages file upload in Streamlit, saves the uploaded PDF temporarily, and loads it for processing.
    \"\"\"
    st.session_state["agent"].reset_knowledge_base()  # Clear previous data
    st.session_state["messages"] = []  # Reset conversation history
    st.session_state["user_input"] = ""  # Clear user input

    for uploaded_file in st.session_state["file_uploader"]:
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(uploaded_file.getbuffer())
            temp_file_path = temp_file.name

        with st.session_state["document_processing_spinner"], st.spinner(f"Processing {uploaded_file.name}..."):
            st.session_state["agent"].load_document(temp_file_path)
        os.remove(temp_file_path)  # Clean up temporary file

def main():
    \"\"\"
    Initializes the Streamlit application, setting up UI components and session state for user interaction.
    \"\"\"
    if "messages" not in st.session_state:
        st.session_state["messages"] = []
    if "OPENAI_API_KEY" not in st.session_state:
        st.session_state["OPENAI_API_KEY"] = st.secrets["openai_api_key"]
        st.session_state["agent"] = DocumentConversationalAgent(st.session_state["OPENAI_API_KEY"])

    st.header("ChatPDF: Ask Your PDF Documents")
    
    st.subheader("Upload PDFs")
    st.file_uploader("Choose PDF files", type=["pdf"], key="file_uploader",
                     on_change=handle_file_upload, accept_multiple_files=True)

    st.session_state["document_processing_spinner"] = st.empty()

    display_conversations()

    st.text_input("Type your question here:", key="user_input",
                  on_change=process_user_query)

    st.divider()

if __name__ == "__main__":
    main()