import streamlit as st
import random
import time

# Set page title and layout
st.set_page_config(page_title="🌸 Nowruz Greeting", page_icon="🌿", layout="centered")

# Apply Nowruz-themed full-page gradient background
st.markdown(
    """
    <style>
        /* Full-page gradient background (Spring colors) */
        .main-container {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(to bottom, #A7E9AF, #87CEEB, #FFB6C1);
            z-index: -1;
        }

        /* Ensure Streamlit content remains visible */
        .stApp {
            background: transparent !important;
        }
    </style>
    
    <div class="main-container"></div> <!-- Background gradient container -->
    """,
    unsafe_allow_html=True,
)

# Create placeholder elements for dynamic updates

flower_display = st.empty()

st.markdown("<h1 style='text-align: center; color:#2E7D32;'>🌿✨🌸 نوروز مبارک 🌸🌿✨</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align:center;  color:#2E7D32; font-size:40px;'>💖برای شما شادی، سلامتی و موفقیت آرزومندم 💖</h1>", unsafe_allow_html=True)
while True:
    # Display Nowruz greeting
    
    # Animation: Falling Flowers
    flowers = ["🌸", "🌼", "🌺", "💮"]
    for _ in range(10):
        flower_str = " ".join(random.choices(flowers, k=10))
        flower_display.markdown(f"<h3 style='text-align: center; color:#2E7D32;'>{flower_str}</h3>", unsafe_allow_html=True)
        time.sleep(0.5)

    # Trigger Balloons 🎈
    st.balloons()

    # Wait before restarting the animation
    time.sleep(5)  # Adjust for longer or shorter intervals
