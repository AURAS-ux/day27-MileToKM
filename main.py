from tkinter import *


def Convert(number):
    resultLabel.config(text=f"{number*1.609344}")


window = Tk()
window.title("Convertor")
window.minsize(height=200, width=400)

welcomeLabel = Label(text="Welcome to Mile to KM convertor", font=("Times New Roman", 14, "normal"))
welcomeLabel.place(x=70, y=10)
inputZone = Entry(width=15)
inputZone.place(x=200, y=60)
milesLabel = Label(text="Miles", font=("Arial", 12, "normal"))
milesLabel.place(x=260, y=60)
label1 = Label(text="is equal to", font=("Arial", 12, "normal"))
label1.place(x=110, y=80)
resultLabel = Label(text="0", font=("Arial", 12, "normal"))
resultLabel.place(x=200, y=80)
label2 = Label(text="KM", font=("Arial", 12, "normal"))
label2.place(x=260, y=80)

convertButton = Button(text="CONVERT", command=lambda: Convert(int(inputZone.get())))
convertButton.place(x=190, y=110)

window.mainloop()
