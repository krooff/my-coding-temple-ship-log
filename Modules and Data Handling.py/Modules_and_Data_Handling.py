# Task 1: Your Mood Today

def mood_response(mood):
    mood = mood.lower()
    if mood == "happy":
        return "Fantastic! Keep smiling, your happiness is contagious!"
    elif mood == "sad":
        return "I'm sorry you're sad. Tell me what I can do to help."
    elif mood == "mad":
        return "Let's take a breath and find a way to resolve the problem you're having."
    elif mood == "tired":
        return "We can find a nice cozy spot for a nap. Self-care is important."
    else:
        return "Thanks for sharing! Self-awareness is the start to a better you!"

# Later...
from mood_responses import mood_response
 # To import the function directly

mood = input("How are you feeling today? ")
print(mood_response(mood)) 


