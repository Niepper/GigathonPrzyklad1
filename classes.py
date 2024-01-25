from helpers.helper import valueCheckErr, clear


# def optionsHandler():
#     options = input()
#     final = []
#     if "-" in options:
#         values = options.split("-")
#         for i in range(int(values[0]), int(values[1])+1):
#             final.append(i-1)
#     else:
#         commaSeparated = options.split(",")
#         final = list(map(int,commaSeparated))
#         a = final[0]
#     return final


class Literator:
    words = ["", ""]
    wordsVal = [0, 0]
    selectedWord = -1

    def selection(self, question):
        print(f"{question}")
        try:
            self.selectedWord = int(input()) - 1
            if self.selectedWord > 1 or self.selectedWord < 0:
                valueCheckErr()
                return 1
        except ValueError:
            valueCheckErr()
            return 1
        return 0

    def readWords(self):
        clear()
        temp = input("Podaj pierwsze słowo: ")
        if temp != "":
            self.words[0] = temp
        temp = input("Podaj drugie słowo: ")
        if temp != "":
            self.words[1] = temp
        return (f'Ustawiono słowa "{self.words[0]}" i "{self.words[1]}"')

    def whichLonger(self):
        if len(self.words[0]) > len(self.words[1]):
            return (f"Pierwsze słowo ({self.words[0]}) jest dłuższe od drugiego ({self.words[1]})")
        elif len(self.words[0]) < len(self.words[1]):
            return (f"Drugie słowo ({self.words[1]}) jest dłuższe od pierwszego ({self.words[0]})")
        else:
            return (f"Oby dwa słowa ({self.words[0]} i {self.words[1]}) są tej samej długości ({len(self.words[1])} znaków)")

    def capitalize(self):
        if self.selection(self, "Któremu słowu chcesz zwiększyć litery?"):
            self.capitalize(self)

        self.words[self.selectedWord] = self.words[self.selectedWord].upper()
        return f"Powiększono litery słowu {self.words[self.selectedWord]}"


    def lower(self):
        if self.selection(self, "Któremu słowu chcesz zmiejszyć litery?"):
            self.lower(self)

        self.words[self.selectedWord] = self.words[self.selectedWord].lower()
        return f"Zmniejszono litery słowu {self.words[self.selectedWord]}"


    def calcWordValue(self, selected=2):
        if selected == 2:
            if self.selection(self, "Dla którego słowa chcesz obliczyć wartość?"):
                self.calcWordValue(self)
        else:
            self.selectedWord = selected
        for i in self.words[self.selectedWord]:
            self.wordsVal[self.selectedWord] += ord(i)
        return( self.wordsVal[self.selectedWord])

    def whichHeavier(self):
        word1Weight = self.calcWordValue(self, 0)
        word2Weight = self.calcWordValue(self, 1)
        if word1Weight > word2Weight:
            return (
                f"Pierwsze słowo ({self.words[0]}) \"ważące\" {word1Weight} jest cięższe od drugiego słowa ({self.words[1]}) ważącego {word2Weight}")
        elif word2Weight > word1Weight:
            return (
                f"Drugie słowo ({self.words[1]}) \"ważące\" {word2Weight} jest cięższe od pierwszego słowa ({self.words[0]}) ważącego {word1Weight}")
        else:
            return (f"Obydwa słowa ({self.words[0]} i {self.words[1]}) \"ważą\" tyle samo ({word1Weight})")

    def changeLetter(self):
        if self.selection(self, "Któremu słowu chcesz podmienić znak?"):
            self.changeLetter(self)

        oldLetter = input("Jaki znak chcesz podmienić? ")
        newLetter = input("Na jaki ? ")
        self.words[self.selectedWord] = self.words[self.selectedWord].replace(oldLetter, newLetter)
        return ( self.words[self.selectedWord])

    def changeIndexedLetter(self):
        if self.selection(self, "Któremu słowu chcesz podmienić znak?"):
            self.changeIndexedLetter(self)

        index = int(input("Który indeks podmienić? "))
        newLetter = input("Na jaki znak? ")
        temp = list(self.words[self.selectedWord])

        temp[index] = newLetter
        self.words[self.selectedWord] = "".join(temp)
        return (self.words[self.selectedWord])
