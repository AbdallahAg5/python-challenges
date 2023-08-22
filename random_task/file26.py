# Create a function that takes a string as an argument and returns a coded (h4ck3r 5p34k) version of the string.

def hacker_speak(string):
    newString=""
    for char in string:
        if char == "a":
          newString += "4"
        elif char == "e":
            newString += "3"
        elif char == "i":
            newString += "1"
        elif char == "o":
            newString +="0"
        elif char == "s":
            newString +="5"
        else:
            newString +=char

    return newString             


print(hacker_speak("javascript is cool"))