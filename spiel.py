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




