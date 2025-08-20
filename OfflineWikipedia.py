import wikipedia
import sys
import os
import time

def choosey():
    while True:
        print("Welcome to OfflineWikipedia")
        print("Press 1 for Summary \nPress 2 for Pages(It is useless tho) \nPress 3 for Search \nor type 'q' to quit it\n")
        choose_it = input("> ")
        if choose_it == "1":
            os.system('cls')
            while True:
                try:
                    userinput = input("> ")
                    result = wikipedia.summary(userinput)
                    print(result)
                except Exception as e:
                    print("Something went wrong please try again!", e)
        elif choose_it == "2":
            os.system('cls')
            while True:
                try:
                    userinput = input("> ")
                    result = wikipedia.page(userinput)
                    print(result)
                except Exception as e:
                    print("Something went wrong please try again!", e)
        elif choose_it == "3":
            os.system('cls')
            while True:
                try:
                    userinput = input("> ")
                    result = wikipedia.search(userinput)
                    print(result)
                except Exception as e:
                    print("Something went wrong please try again!", e)
        elif choose_it.lower() == "q":
            "Goodbye"
            break
        else:
            os.system('cls')
            print("Not a valid input there, champ")
            time.sleep(1)
            os.system('cls')
            continue

choosey()
