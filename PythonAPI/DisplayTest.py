#This is a testing doc for displaying the text and entries on a screen\window
import tkinter as tk

window = tk.Tk()
window.title("My Display")

label = tk.Label(window, text=input("testing: "))
label.pack()

window.mainloop()