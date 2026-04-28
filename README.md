# 🎬 ChronicleSync: AI-Powered Storyboard Manager

ChronicleSync is a specialized tool for creators to convert raw story scripts into cinematic visual storyboards using Generative AI. It features a custom **Prompt Version Control System** to track and manage creative iterations.

## ✨ Key Features
- **Script Parsing:** Automatically breaks down long scripts into logical scenes.
- **AI Cinematographer:** Uses GPT-4o to generate high-quality visual prompts from text.
- **Version History:** Built-in SQLite integration to save and compare multiple prompt iterations for the same scene.
- **Cinematic UI:** A custom-styled Streamlit interface optimized for creative workflows.

## 🛠️ Tech Stack
- **Frontend:** Streamlit (Python)
- **AI Engine:** OpenAI API
- **Database:** SQLite3
- **Styling:** Custom CSS

## ⚙️ How to Run
1. Clone the repository: `git clone https://github.com/yourusername/ChronicleSync.git`
2. Install dependencies: `pip install streamlit openai pandas`
3. Run the app: `streamlit run app.py`

## 📈 Future Roadmap
- Integration with Stability AI for direct image generation.
- Export storyboard as PDF/PPT.
- Multi-character consistency tracking.
