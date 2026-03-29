import streamlit as st

def display_wave_animation():
    st.markdown("""
    <style>
    .audio-visualizer {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 4px;
        height: 50px;
        margin: 10px 0;
    }
    .bar {
        width: 6px;
        border-radius: 4px;
        background: linear-gradient(180deg, #4285F4, #EA4335, #FBBC05, #34A853);
        animation: pulse 1.2s infinite ease-in-out;
    }
    .bar:nth-child(1) { height: 10px; animation-delay: -1.2s; }
    .bar:nth-child(2) { height: 25px; animation-delay: -1.0s; }
    .bar:nth-child(3) { height: 40px; animation-delay: -0.8s; }
    .bar:nth-child(4) { height: 20px; animation-delay: -0.6s; }
    .bar:nth-child(5) { height: 35px; animation-delay: -0.4s; }
    .bar:nth-child(6) { height: 15px; animation-delay: -0.2s; }
    .bar:nth-child(7) { height: 30px; animation-delay: -0.0s; }
    @keyframes pulse {
        0%, 100% { transform: scaleY(0.5); opacity: 0.5; }
        50% { transform: scaleY(1.0); opacity: 1; }
    }
    </style>
    <div class="audio-visualizer">
        <div class="bar"></div><div class="bar"></div><div class="bar"></div>
        <div class="bar"></div><div class="bar"></div><div class="bar"></div><div class="bar"></div>
    </div>
    """, unsafe_allow_html=True)
