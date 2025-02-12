from spellchecker import SpellChecker
from tkinter import *

class Spell:
    def __init__(self, text):
        self.text = text
        self.spell = SpellChecker()

    def correctSpelling(self):
        correct = self.spell.correction(self.text)
        candidates = self.spell.candidates(self.text)
        for i in candidates:
            if i != correct:
                correct = correct + '\n' + i
        return correct

    def check(self):
        misspelled = self.spell.unknown([self.text])
        for i in misspelled:
            print(i)
        if len(misspelled) == 0:
            return True
        else:
            return False

def takeInput():
    Output.delete("1.0", "end")
    Input = inputText.get("1.0", "end-1c")
    Input = Input.split()[0]
    s = Spell(Input)
    if s.check():
        Output.insert(END, 'Correct!')
    else:
        correctSpellings = s.correctSpelling()
        Output.insert(END, 'Incorrect!, Do you mean any of these:\n' + correctSpellings)

root = Tk()
root.geometry("400x400")
root.title("Spelling Checker")

l = Label(text="Type the word here:", bg='#759D98', bd='4', font=("Times", "23", "bold"), width='40')
inputText = Text(root, height=2, width=40, bd='3', font=("Times", "18", "bold"))
Check = Button(root, height=2, width=20, text="Check", command=lambda: takeInput(), bg='#375F5A', fg='black', font=("Times", "14"))
Output = Text(root, height=5, width=40, bd='3', bg='#8C9F9D', font=("Times", "18", "bold"))

l.pack(padx=2, pady=2)
inputText.pack(padx=5, pady=5)
Check.pack(padx=2, pady=2)
Output.pack(pady=5)

root.mainloop()
