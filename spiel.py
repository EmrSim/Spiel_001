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
    def __init__(self, f, name):
        self.name = name
        self.frame = ctk.CTkFrame(f, fg_color = hintergrund, corner_radius = 10, border_width = 2)
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
        self.after(0, lambda: self.state("zoomed"))

        self.grid_columnconfigure(0, weight = 1000)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_rowconfigure(0, weight = 1)
        self.grid_rowconfigure(1, weight = 1)

        self.wuerfel_label = ctk.CTkLabel(self, text = "Geben sie ihren Tipp ab!\n\n", font = ("Arial", 50), text_color = textfarbe)
        self.wuerfel_label.grid(row = 0, column = 0, pady = 50)

        ziffer_frame = ctk.CTkFrame(self, fg_color = hintergrund, corner_radius = 15, border_width = 3)
        ziffer_frame.grid(row = 0, column = 0, sticky = "s")
        for i in range (1, 7):
            ziffer = ctk.CTkButton(ziffer_frame, text = str(i), command = lambda i = i: self.click(i), width = 110, height = 60,
                                   corner_radius = 15, font = ("Arial", 24), text_color = textfarbe)
            ziffer.grid(row = (i - 1) // 3, column = (i - 1) % 3, padx = 10, pady = 10)
        
        self.spieler_frame = ctk.CTkFrame(self, fg_color = hintergrund)
        self.spieler_frame.grid(row = 0, column = 0, sticky = "nesw")
        self.spieler_liste = []

        button_frame = ctk.CTkFrame(self, fg_color = hintergrund)
        button_frame.grid(row = 0, column = 1, rowspan = 2, padx = 20, sticky = "nesw")

        button_frame.grid_rowconfigure(0, weight = 1)
        button_frame.grid_rowconfigure(1, weight = 0)
        button_frame.grid_rowconfigure(2, weight = 0)
        button_frame.grid_rowconfigure(3, weight = 1)

        ctk.CtkButton(button_frame, text = "Spieler hinzufügen", command = self.add_spieler, corner_radius = 12,
                      font = ("Arial", 20), width = 180, height = 50).grid(row = 1, column = 1, pady = 10, sticky = "ew")
        ctk.CtkButton(button_frame, text = "Spieler entfernen", command = self.remove_spieler, corner_radius = 12,
                      font = ("Arial", 20), width = 180, height = 50).grid(row = 2, column = 1, pady = 10, sticky = "ew")
        
        self.aktueller_spieler = 0
        self.animation = False 
        self.spieler_bearbeitung = True
        self.add_spieler()

    def add_spieler(self):
        if (self.spieler_bearbeitung == True and len(self.spieler_liste) < max_spieler):
            name = f"Spieler {len(self.spieler_liste) + 1}"
            spieler = Spieler(self.spieler_frame, name)
            self.spieler_liste.append(spieler)

    def remove_spieler(self):
        if (self.spieler_bearbeitung == True and len(self.spieler_liste) > 1):
            spieler = self.spieler_liste.pop()
            spieler.frame.destroy()

    def click(self, zahl):
        if (self.animation == True): 
            return
        self.spieler_bearbeitung = False
        if (self.aktueller_spieler < len(self.spieler_liste)):
            spieler = self.spieler_liste[self.aktueller_spieler]
            spieler.tipp = zahl
            spieler.tipp_label.configure(text = str(zahl))
            self.aktueller_spieler += 1 
        if (self.aktueller_spieler == len(self.spieler_liste)):
            self.nummer = random.randint(1, 6)
            self.wuerfel_label.configure(text = str(self.nummer) + "\n\n\n")
            self.after(500, self.gewinner)

    def gewinner(self):
        gewinner = []
        for spieler in self.spieler_liste:
            if (spieler.tipp == self.nummer):
                gewinner.append(spieler.name)
            if (len(gewinner) > 0):
                text = "Gewinner:\n"
                for name in gewinner:
                    text += name + "! "
            else: 
                text = "Kein Gewinner!\n"
            self.wuerfel_label.configure(text = text + "\n\n")
            self.after(gewinner_anzeige, self.reset)
    
    def reset(self):
        