import random

from test import inventory

WORDS=("python","programowanie","doskonale","skomplikowany","uniwersytet","sakfon")

word=random.choice(WORDS)
poprawna=word
zamieszane=""

while word:
        pozycja=random.randrange(len(word))
        zamieszane+=word[pozycja]
        word = word[:pozycja] + word[(pozycja+1):]
print("Uporządkuj litery, aby odtworzyć prawidłowe słowo.")
print("Zgadnij, jakie to słowo:",zamieszane)

odp=input("\nTwoja odpowiedź: ")
while odp!=poprawna:
    print("Niestety, to nie to słowo.")
    odp=input("Twoja odpowiedź: ")
if odp==poprawna:
    print("Zgadza się! Zgadłeś!\n")

inventory=["miecz","zbroja","tarcza","buty"]
inventory+="kusza"

