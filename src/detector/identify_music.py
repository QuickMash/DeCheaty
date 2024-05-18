import speech_recognition as sr
import re
import dcmangage

player = command.playerlist()
r = sr.Recognizer()

# Define a function to identify a song pattern
def is_song_like(text):
    pattern = r"([A-Z][a-z]+ ){2,}([A-Z][a-z]+ ){2,}" # IDK if this will work
    if re.match(pattern, text):
        return True
    else:
        return False

# Define a function to identify background sound
def has_background_sound(audio):
    # idk
    return False

# Loop through the voice chat audio files
for file in voice_chat_files:
    # Open the audio file
    with sr.AudioFile(file) as source:
        # Record the audio
        audio = r.record(source)
        
        # Convert the audio to text
        try:
            text = r.recognize_google(audio, language="en-US")
        except sr.UnknownValueError:
            continue
        
        # Check if the text matches a song-like pattern
        if is_song_like(text):
            # Check if the audio has background sound
            if has_background_sound(audio):
                # Get the player's username from the internal file
                player = players.get(text)
                if player:
                    print(f"Player {player} is playing music!")
                else:
                    print("Player not found!")
            else:
                print("No background sound detected.")
        else:
            print("No song-like pattern detected.")