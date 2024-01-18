from tkinter import *
import random


root= Tk()

root.title("Random Colors")
root.geometry("600x400")

colors = {"color" : ["maroon1","lawn green","magenta2","purple1","springgreen2","chocolate1", "deep pink","cyan"]}

def background_change():
    random_number = random.randint(0,7)
    print(colors["color"][random_number])
    root.configure(background=colors["color"][random_number])
    
btn = Button(root, text="click me", command=background_change)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()