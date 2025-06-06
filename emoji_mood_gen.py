#emoji mood generator
moods = {
    "happy": ":) Keep smiling!",
    "sad": ":( It's okay to be sad sometimes.",
    "angry": ">:| Try to stay calm and breathe.",
    "excited": ":D That's awesome! Enjoy the moment!",
    "tired": "-_- You should take some rest."
}
mood = input("How are you feeling today? ").lower()
if mood in moods:
    print(moods[mood])
else:
    print(":| Sorry, I don't recognize that mood. Stay positive!")
