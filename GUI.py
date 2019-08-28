import os
from tkinter import *
from tkinter import ttk


class Configurator:
    def getConfig(self):
        config = open("config.txt", "r")
        buttonList = []
        while True:
            item = config.readline().strip("\n")
            if item == "<End>":
                break
            buttonList.append(item)
        config.close()
        return buttonList


configurator = Configurator()
FuckingConfig = configurator.getConfig()


def speak_text_button_fc():
    os.system("say \"" + text.get() + "\"")


def fc(*args):
    os.system("say \"" + comboxlist.get() + "\"")


root = Tk()
root.title('Speaker')
title = Label(root, text='Speaker')
title.grid(sticky=W, column=1, row=0)
enter_text = Label(root, text='Please enter the text')
enter_text.grid(column=0, row=2)
text = Entry(root)
text.grid(column=1, row=2)
speak_text_button = Button(
    root, text='Read the entered text', command=speak_text_button_fc)
speak_text_button.grid(column=1, row=3)

comvalue = StringVar()
comboxlist = ttk.Combobox(root, textvariable=comvalue)
comboxlist["values"] = FuckingConfig
comboxlist.current(0)
comboxlist.bind("<<ComboboxSelected>>", fc)
comboxlist.grid(column=0, row=4)
root.mainloop()
