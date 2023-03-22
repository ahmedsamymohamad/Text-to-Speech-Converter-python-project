import pyttsx3

# Create a TTS engine object
engine = pyttsx3.init()

# Set the TTS engine properties
engine.setProperty('rate', 150)  # Set the speaking rate (words per minute)
engine.setProperty('volume', 0.7)  # Set the volume (0-1)

# Convert text to speech
text = input('Enter the text to speak: ')
engine.say(text)
engine.runAndWait()