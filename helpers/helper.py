import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def valueCheckErr():
    clear()
    print("Nie podano prawidłowej wartości.")
