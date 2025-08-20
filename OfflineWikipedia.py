import wikipedia
import sys

while True:
    try:
        userinput = input("> ")
        result = wikipedia.summary(userinput)
        print(result)
    except:
        print("Something went wrong please try again!")