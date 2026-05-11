import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew

load_dotenv()

class StoryTeller:
    def __init__(self):
        self.narrator = Agent(
            role='Empathic Narrator',
            goal='Tell stories and adapt the plot based on listener emotions',
            backstory='You are a master storyteller who can sense boredom or excitement.',
            verbose=True
        )

    def adapt_story(self, facial_expression, current_genre):
        """Logic phán đoán sở thích dựa trên sắc mặt"""
        if facial_expression == "bored" or facial_expression == "unhappy":
            new_genre = "Sci-Fi" if current_genre == "Fairy Tale" else "Action"
            return f"Tôi thấy bạn không vui với truyện {current_genre}. Đổi sang {new_genre} nhé?"
        return "Bạn đang rất tập trung, tôi kể tiếp đây..."

if __name__ == "__main__":
    teller = StoryTeller()
    # Giả lập phát hiện sắc mặt 'unhappy' qua Gemini Vision
    print(teller.adapt_story("unhappy", "Fairy Tale"))
