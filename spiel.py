"""
Würfelspiel
Ersteller: Simsek Emre | Starcevic Luka | Turek Alexander
"""

import customtkinter as ctk
import random

ctk.set_apperance_mode("light")

#Variablen
max_spieler = 4
animation_länge = 25
gewinner_anzeige = 3000

#Farben
hintergrund = "white"
textfarbe = "black"

class Spieler:
    def __init__(self, spieler, name):
        self.name = name
        self.frame = ctk.CTkFrame(spieler, fg_color = hintergrund, corner_radius = 10, border_width = 2)
        self.frame.pack(expand = True, side = "left")
        self.tipp_label = ctk.CTkLabel(self.frame, text = "", font = ("Arial", 24), text_color = textfarbe)
        self.tipp_label.pack(pady = 5)
        self.tipp = None
        self.name_label = ctk.CTkLabel(self.frame, text = self.name, font = ("Arial", 20), text_color = textfarbe)
        self.name_label.pack(pady = 5)

class Spiel(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.titel("Würfelspiel")
        self.after(o, lambda: self.state("zoomed"))

        self.grid_columnconfigure(0, weight = 1000)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_rowconfigure(0, weight = 1)
        self.grid_rowconfigure(1, weight = 1)

        self.wuerfel_label = ctk.CTkLabel(self, text = "\n\n\n", font = ("Arial", 50), text_color = textfarbe)
        self.wuerfel_label.grid(row = 0, column = 0, pady = 50)

        ziffer_frame = ctk.CTkFrame(self, fg_color = hintergrund, corner_radius = 15, border_width = 3)
        ziffer_frame.grid(row = 0, column = 0, sticky = "s")
        for i in range (1, 7):
            ziffer = ctk.CTkButton(ziffer_frame, text = str(i), command = lambda i = i: self.click(i), width = 110, height = 60,
                                   corner_radius = 15, font = ("Arial", 24), text_color = textfarbe)
            ziffer.grid(row = (i - 1) // 3, column = (i - 1) % 3, padx = 10, pady = 10)
        
        self.spieler_frame = ctk.CTkFrame(self, fg_color = hintergrund)
        self.spieler_frame.grid(row = 0, column = 0, sticky = "nesw")

        #test  