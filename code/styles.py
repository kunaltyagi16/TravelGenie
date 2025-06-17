import streamlit as st

def set_background_and_styles():
    """Sets the background image and custom styles for the app"""
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1507525428034-b723cf961d3e");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }
        .stChatInput {
            background-color: rgba(255,255,255,0.85) !important;
            border-radius: 10px;
        }
        .stChatMessage {
            background-color: rgba(255,255,255,0.9) !important;
            border-radius: 10px;
            padding: 12px;
        }
        h1 {
            color: white;
            text-shadow: 2px 2px 4px #000000;
        }
        .sidebar .sidebar-content {
            background-color: rgba(255,255,255,0.85);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def get_destination_ideas():
    """Returns dictionary of popular destination categories"""
    return {
        "🏖️ Tropical Getaway": ["Bali", "Maldives", "Hawaii"],
        "🏔️ Adventure Travel": ["Swiss Alps", "Patagonia", "Nepal"],
        "🏛️ Cultural Experience": ["Rome", "Kyoto", "Marrakech"],
        "🗼 City Break": ["Paris", "New York", "Tokyo"]
    }