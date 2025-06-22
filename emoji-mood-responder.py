# Emoji Mood Responder

# Step 1: Dictionary mapping moods to emojis and messages
mood_responses = {
    "happy": ("😊", "That's great! Keep smiling and spread the joy!"),
    "sad": ("😢", "It's okay to feel sad. Better days are ahead!"),
    "angry": ("😠", "Take a deep breath. Let it go and stay calm."),
    "excited": ("🤩", "Wow! Keep up the energy and enthusiasm!"),
    "tired": ("😴", "You deserve some rest. Take a short break!"),
    "nervous": ("😰", "Everything will be fine. Just do your best!")
}

# Step 2: Ask the user for their current mood
user_mood = input("How are you feeling today? ").strip().lower()

# Step 3 & 4: Match mood and display response
if user_mood in mood_responses:
    emoji, message = mood_responses[user_mood]
    print(f"{emoji} {message}")
else:
    # Step 5: Default response for unknown mood
    print("🤔 I'm not sure what that mood is, but I hope you have a great day!")
