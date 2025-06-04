"""
Mensch ärgere dich nicht
Ersteller: Simsek Emre | Starcevic Luka | Turek Alexander
"""
import customtkinter as ctk
from PIL import Image
import random

app = ctk.CTk()
app.title("Mensch ärgere dich nicht")
app.after(0, lambda: app.state("zoomed"))

label = ctk.CTkLabel(app, text="", font=("Arial", 20, "bold"))
label.pack()

label = ctk.CTkLabel(app, text="Mensch ärgere dich nicht", font=("Arial", 100, "bold"))
label.pack()

label = ctk.CTkLabel(app, text="", font=("Arial", 20, "bold"))
label.pack()

"""
class Spielbrett:
    def __init__(self, canvas):
        self.canvas = canvas
        self.startposition = {
        "rot": [(100,80),(100,100),(120,80),(120,100)],
        "gruen": [(0,80),(0,100),(20,80),(20,100)],   
        "gelb": [(0,0),(0,20),(20,0),(20,20)], 
        "blau": [(100,0),(100,20),(120,0),(120,20)],   
        }
    
    def hintergrund(self):


class Spieler:

class Figur:

class Spiel:

"""

app.mainloop()