import streamlit as st
from database import StoryDB
from ai_engine import AIEngine

# Page Configuration
st.set_page_config(page_title="ChronicleSync Pro", layout="wide", page_icon="🎬")
db = StoryDB()

# Custom CSS for Netflix/Cinematic Look
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .scene-card {
        background-color: #161b22;
        padding: 25px;
        border-radius: 12px;
        border-left: 6px solid #e50914;
        margin-bottom: 30px;
    }
    .version-tag { color: #8b949e; font-size: 0.9em; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎬 ChronicleSync: AI Storyboard Manager")
st.markdown("---")

# Sidebar
with st.sidebar:
    st.header("🔑 Settings")
    api_key = st.text_input("OpenAI API Key (Mock Mode active)", type="password", value="demo_mode")
    st.info("Mock Mode is ON. Images will cycle through a dynamic pool.")

# Story Input
story_text = st.text_area("✍️ Script to Storyboard (Paragraphs = Scenes):", height=150, placeholder="Example: A lone astronaut on Mars...")

if st.button("🚀 Process Storyboard"):
    if story_text.strip():
        scenes = [s.strip() for s in story_text.split('\n') if s.strip()]
        st.session_state['scenes'] = scenes
    else:
        st.error("Please write something first!")

# Display Scenes Logic
if 'scenes' in st.session_state:
    for i, scene in enumerate(st.session_state['scenes']):
        st.markdown(f'<div class="scene-card">', unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 1.2])
        
        with col1:
            st.subheader(f"Scene {i+1}")
            st.write(scene)
            
            if st.button(f"Generate/Regenerate Visuals {i+1}", key=f"gen_{i}"):
                with st.spinner("AI is painting your scene..."):
                    engine = AIEngine(api_key)
                    prompt = engine.generate_visual_prompt(scene)
                    db.save_version(i+1, prompt)
                    st.success("New version added to history!")

            with st.expander("📜 Version History"):
                history = db.get_versions(i+1)
                if history:
                    for ver in history:
                        st.markdown(f"<p class='version-tag'>Version {ver[0]} | {ver[2]}</p>", unsafe_allow_html=True)
                        st.code(ver[1])
                        st.markdown("---")
                else:
                    st.info("No versions yet. Click 'Generate' above.")

        with col2:
            # DYNAMIC IMAGE POOL LOGIC
            image_pool = [
                "https://images.unsplash.com/photo-1614728894747-a83421e2b9c9?q=80&w=1000", # Space
                "https://images.unsplash.com/photo-1578328819058-b69f3a3b0f6b?q=80&w=1000", # Interior
                "https://images.unsplash.com/photo-1543722530-d2c3201371e7?q=80&w=1000", # City
                "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?q=80&w=1000"  # Orbit
            ]
            
            # Fetch latest version number from DB
            history = db.get_versions(i+1)
            current_ver = history[0][0] if history else 1
            # Pick image based on version number
            img_idx = (current_ver - 1) % len(image_pool)
            
            st.image(image_pool[img_idx], caption=f"Cinematic Visual (v{current_ver})", use_container_width=True)
            
        st.markdown('</div>', unsafe_allow_html=True)