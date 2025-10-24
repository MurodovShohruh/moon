import tkinter as tk
import time

# Oyna yaratish
root = tk.Tk()
root.title("Svetafor")
canvas = tk.Canvas(root, width=200, height=400, bg="black")
canvas.pack()

# Doira chiroqlar
red = canvas.create_oval(50, 50, 150, 150, fill="grey")
yellow = canvas.create_oval(50, 160, 150, 260, fill="grey")
green = canvas.create_oval(50, 270, 150, 370, fill="grey")

def turn_on(light):
    colors = {"red": "grey", "yellow": "grey", "green": "grey"}
    colors[light] = light

    canvas.itemconfig(red, fill=colors["red"])
    canvas.itemconfig(yellow, fill=colors["yellow"])
    canvas.itemconfig(green, fill=colors["green"])

def run_traffic():
    while True:
        turn_on("red")
        root.update()
        time.sleep(3)

        turn_on("yellow")
        root.update()
        time.sleep(1)

        turn_on("green")
        root.update()
        time.sleep(3)

# Dastur ishga tushishi
import threading
threading.Thread(target=run_traffic, daemon=True).start()

root.mainloop()