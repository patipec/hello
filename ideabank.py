import sys
import io
import os

def adding():
    print("What is your new idea?")
    idea = input()
    return(idea)

added = adding()
text_file = open("ideas.txt", "w")  # otwiera plik tekstowy 
# w wersji edytowalnej
text_file.write(added)  # wpisuje input do otwartego pliku
text_file.close()  # zamyka plik

# wyciaganie idei z pliku i printowanie
ideas = open("ideas.txt", "r")
lines = list(ideas)
ideas.close()
print(len(lines), ".", lines)


