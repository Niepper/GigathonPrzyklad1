from classes import Literator
from helpers.helper import clear


def init(a: Literator):
    a.readWords(a)

def printOptions(options: list):
    for index, i in enumerate(options):
        print(f"{index+1}. {i}")
def menu(a: Literator):
    clear()
    print(f'Obecne słowa to: "{a.words[0]}" i "{a.words[1]}"')
    print("Co zamierzasz zrobić?")
    options = ["Wczytaj ponownie stringi (Pusta wartość nie nadpisuje)", "Sprawdź który jest najdłuższy", "Zamień małe litery na wielkie",
               "Zamień wielkie litery na małe", 'Oblicz "wartość" słowa', 'Sprawdź który ma większą "wagę"',
               "Zamień konkretny znak", "Zamień znak z konkretnego indeksu", "Zakończ"]
    printOptions(options)
    answer = input()
    match answer:
        case "1":
            print(a.readWords(a))
        case "2":
            print(a.whichLonger(a))
            input("\nNaciśnij enter by kontunuować")
        case "3":
            print(a.capitalize(a))
            input("\nNaciśnij enter by kontunuować")

        case "4":
            print(a.lower(a))
            input("\nNaciśnij enter by kontunuować")

        case "5":
            print(a.calcWordValue(a))
            input("\nNaciśnij enter by kontunuować")

        case "6":
            print(a.whichHeavier(a))
            input("\nNaciśnij enter by kontunuować")

        case "7":
            print(a.changeLetter(a))
            input("\nNaciśnij enter by kontunuować")

        case "8":
            print(a.changeIndexedLetter(a))
            input("\nNaciśnij enter by kontunuować")

        case "9":
            exit(0)
        case _:
            clear()
            print("Nie podano prawidłowej wartości")
            menu(a)
    menu(a)