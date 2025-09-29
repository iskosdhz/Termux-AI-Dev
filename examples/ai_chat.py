#!/data/data/com.termux/files/usr/bin/python3

import random
import json
import os

class SimpleAIChat:
    def __init__(self):
        self.responses = {
            "hello": ["Hello! 🤖", "Hi there!", "Hey! How can I help you?"],
            "how are you": ["I'm functioning optimally! 💪", "Great! Ready to help.", "Doing well, thank you!"],
            "what can you do": [
                "I can chat with you!",
                "I'm your AI assistant in Termux!",
                "I can help you learn about AI in mobile development!"
            ],
            "ai": [
                "AI in Termux is amazing! You can run machine learning models on your phone!",
                "Did you know you can train neural networks in Termux?",
                "Mobile AI development is the future! 📱"
            ],
            "termux": [
                "Termux is a powerful terminal emulator for Android!",
                "With Termux, you can turn your phone into a development machine!",
                "Termux + AI = Unlimited possibilities! 🚀"
            ]
        }
        
        self.default_responses = [
            "That's interesting! Tell me more.",
            "I'm still learning. Can you explain?",
            "Fascinating! How does that work?",
            "I'd love to hear more about that!",
            "That's a great point! 🤔"
        ]
    
    def get_response(self, user_input):
        user_input = user_input.lower()
        
        for key in self.responses:
            if key in user_input:
                return random.choice(self.responses[key])
        
        return random.choice(self.default_responses)
    
    def start_chat(self):
        print("🤖 AI Chat Bot in Termux")
        print("=" * 30)
        print("Type 'quit' to exit\n")
        
        while True:
            try:
                user_input = input("You: ").strip()
                
                if user_input.lower() == 'quit':
                    print("AI: Goodbye! 👋")
                    break
                
                if user_input:
                    response = self.get_response(user_input)
                    print(f"AI: {response}\n")
                else:
                    print("AI: Please say something! 😊\n")
                    
            except KeyboardInterrupt:
                print("\n\nAI: Session interrupted. Goodbye! 👋")
                break
            except Exception as e:
                print(f"AI: Oops! Something went wrong: {e}\n")

if __name__ == "__main__":
    chat_bot = SimpleAIChat()
    chat_bot.start_chat()
