#!/data/data/cm.termux/files/usr/bin/python3

print("🤖 AI Chat Bot in Termux")
print("=" * 30)

responses = {
    "hello": ["Hi there!", "Hello!", "Hey! 👋"],
    "ai": ["AI is amazing in Termux!", "You can run ML models on phone!"],
    "termux": ["Termux turns Android into development machine!"]
}

while True:
    user_input = input("You: ").lower()
    if user_input == 'quit':
        print("AI: Goodbye! 👋")
        break
    
    response = responses.get(user_input, ["I'm still learning!", "Tell me more!"])
    print(f"AI: {response[0]}\n")
