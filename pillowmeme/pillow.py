from PIL import Image

meme1spook = Image.open('meme1spook.jpg')
meme2spook = Image.open('meme2spook.jpg')
meme3spook = Image.open('meme3spook.jpg')

meme1casual = Image.open('meme1casual.jpg')
meme2casual = Image.open('meme2casual.jpg')
meme3casual = Image.open('meme3casual.jpg')

meme1amongus = Image.open('meme1amongus.jpg')
meme2amongus = Image.open('meme2amongus.jpg')
meme3amongus = Image.open('meme3amongus.jpg')

class meme:
    print("Goedendag, wat is jouw naam?")
    naam = input()
    print("Hallo", naam, "Wat voor soort meme wil je vandaag zien?")
    soort = input('Spooktober Memes (1), Casual Memes (2), Among us Memes (3): ')
    if soort == "1":
        spookkeuze = input("Welke Spooktober Meme wil je zien? (1), (2) of (3): ")
        if spookkeuze == "1":
            meme1spook.show('meme1spook.jpg')
        if spookkeuze == "2":
            meme2spook.show('meme2spook.jpg')
        if spookkeuze == "3":
            meme3spook.show('meme3spook.jpg')
    if soort == "2":
        casualkeuze = input("Welke casual meme wil je zien? (1), (2) of (3): ")
        if casualkeuze == "1":
            meme1casual.show('meme1casual.jpg')
        if casualkeuze == "2":
            meme2casual.show('meme2casual.jpg')
        if casualkeuze == "3":
            meme3casual.show('meme3casual.jpg')
    if soort == "3":
        amonguskeuze = input("Welke among us meme wil je zien? (1), (2) of (3): ")
        if amonguskeuze == "1":
            meme1amongus.show('meme1amongus.jpg')
        if amonguskeuze == "2":
            meme2amongus.show('meme2amongus.jpg')
        if amonguskeuze == "3":
            meme3amongus.show('meme3amongus.jpg')
