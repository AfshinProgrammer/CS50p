# Afshin Masoudi
# CS50p/Problem Set 0/Making Faces
# sentence : Hello :) Goodbye :(

def main():
    playback_speed()

def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

def playback_speed():
    user_input = input()
    converted_input = convert(user_input)
    print(converted_input)


if __name__ == "__main__":
    main()