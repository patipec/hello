import sys

file = open("ideabank/ideas.txt", "a+")  # otwiera plik
ideabank = []

def adding():
    print("What is your new idea?")
    idea = input("")
    ideabank.append.splitlines(idea)


added = adding() + "\n"
file.writelines(added)  # wpisuje input do otwartego pliku
file.close()  # zamyka plik
