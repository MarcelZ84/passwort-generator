import secrets
import string

pw = ""
grossbuchstaben = string.ascii_uppercase
kleinbuchstaben = string.ascii_lowercase
zahlen = string.digits
sonderzeichen = string.punctuation
laenge = ""

while True:
    try:
        laenge = int(input("Passwortlänge (mindestens 8 Zeichen): "))
        if laenge >= 8:
            break
        else:
            print("Das Passwort muss mindestens 8 Zeichen lang sein.")
    except ValueError:
        print("Bitte geben Sie eine Zahl ein.")

zeichensatz = grossbuchstaben + kleinbuchstaben + zahlen + sonderzeichen

while True:
    for _ in range(laenge):
        pw += "".join(secrets.choice(zeichensatz))
    if (any(char in sonderzeichen for char in pw) and
            sum(char in zahlen for char in pw) >= 2):
        break
    else:
        pw = ""

print(pw)
input()
