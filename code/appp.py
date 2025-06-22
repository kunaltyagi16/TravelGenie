import os
import streamlit as st
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from styles import set_background_and_styles, get_destination_ideas

# Initialize app config (must be first Streamlit command)
st.set_page_config(
    page_title="Travel Genie",
    page_icon="🏔️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Apply styles and setup
set_background_and_styles()

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "assistant", 
        "content": "Hello! I'm your travel assistant. Where would you like to go? 🌎"
    }]

# Initialize conversation chain
@st.cache_resource
def init_conversation():
    try:
        return ConversationChain(
            llm=OpenAI(
                temperature=0,
                openai_api_key=("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"),
            ),
            memory=ConversationBufferMemory(),
            verbose=True
        )
    except Exception as e:
        st.error(f"Failed to initialize AI: {str(e)}")
        return None

# Sidebar destinations
with st.sidebar:
    st.header("✨ Popular Destinations")
    destinations = get_destination_ideas()
    for category, places in destinations.items():
        with st.expander(category):
            st.write(", ".join(places))

# Main app interface
st.header("🌴 TravelGenie - Ultimate Holiday Planner")

# Display chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])

# Handle user input
if prompt := st.chat_input("Ask about destinations..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.spinner("Planning your trip..."):
        conversation = init_conversation()
        if conversation:
            try:
                response = conversation.run(input=prompt)
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": response
                })
                st.rerun()
            except Exception as e:
                st.error(f"Error generating response: {str(e)}")
