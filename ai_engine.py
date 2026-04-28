import time
import random

class AIEngine:
    def __init__(self, openai_key):
        self.openai_key = openai_key

    def generate_visual_prompt(self, scene_text):
        # AI behavior simulate karne ke liye delay
        time.sleep(1.5) 
        styles = [
            "cinematic lighting, 8k, highly detailed", 
            "moody atmosphere, golden hour, wide shot", 
            "cyberpunk neon aesthetic, sharp focus",
            "hyper-realistic, unreal engine 5 render, epic scale"
        ]
        selected_style = random.choice(styles)
        return f"A professional visualization of: {scene_text}. {selected_style}, movie-still quality."