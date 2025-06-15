"""
Würfelspiel
Ersteller: Simsek Emre | Starcevic Luka | Turek Alexander
"""

#Bibliotheken einfügen
import customtkinter as ctk
import random

#Variablen
max_spieler = 4 #maximale Spieleranzahl
gewinner_anzeige = 3000 #Dauer wie lang Gewinner angezeigt wird

#Farben
hintergrund = "white"
textfarbe = "black"

#Spieler-Klasse
class Spieler:
    def __init__(self, f, name):
        self.name = name
        #Rahmen für Spieler
        self.frame = ctk.CTkFrame(f, fg_color = hintergrund, corner_radius = 10, border_width = 3)
        self.frame.pack(expand = True, side = "left")
        #Label für Tippanzeige
        self.tipp_label = ctk.CTkLabel(self.frame, text = "", font = ("Arial", 24), text_color = textfarbe)
        self.tipp_label.pack(pady = 5)
        self.tipp = None
        #Label um Spielername anzuzeigen
        self.name_label = ctk.CTkLabel(self.frame, text = self.name, font = ("Arial", 20), text_color = textfarbe)
        self.name_label.pack(pady = 5)

#Spiel-Klasse
class Spiel(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Würfelspiel")
        self.after(0, lambda: self.state("zoomed"))
        self.configure(fg_color = hintergrund)

        #Layout-Konfiguration für Grid-System
        self.grid_columnconfigure(0, weight = 1000)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_rowconfigure(0, weight = 1)
        self.grid_rowconfigure(1, weight = 1)

        #Label für Hinweise und Würfelergebnisse
        self.wuerfel_label = ctk.CTkLabel(self, text = "Geben sie ihren Tipp ab!\n\n\n", font = ("Arial", 50), text_color = textfarbe)
        self.wuerfel_label.grid(row = 0, column = 0, pady = 50)

        #Frame für die Zahlentasten 
        ziffer_frame = ctk.CTkFrame(self, fg_color = hintergrund, corner_radius = 15, border_width = 3)
        ziffer_frame.grid(row = 0, column = 0, sticky = "s")
        for i in range (1, 7):
            #Erstellt Zahlen-Buttons, die Tipp setzen
            ziffer = ctk.CTkButton(ziffer_frame, text = str(i), command = lambda i = i: self.click(i), width = 110, height = 60,
                                   corner_radius = 15, font = ("Arial", 24), text_color = textfarbe)
            ziffer.grid(row = (i - 1) // 3, column = (i - 1) % 3, padx = 10, pady = 10)

        #Frame für die Spieleranzeige
        self.spieler_frame = ctk.CTkFrame(self, fg_color = hintergrund)
        self.spieler_frame.grid(row = 1, column = 0, sticky = "nesw")
        self.spieler_liste = []

        #Frame für Steuerungsbuttons
        button_frame = ctk.CTkFrame(self, fg_color = hintergrund)
        button_frame.grid(row = 0, column = 1, rowspan = 2, padx = 20, sticky = "nesw")

        #Button-Layout konfigurieren 
        button_frame.grid_rowconfigure(0, weight = 1)
        button_frame.grid_rowconfigure(1, weight = 0)
        button_frame.grid_rowconfigure(2, weight = 0)
        button_frame.grid_rowconfigure(3, weight = 1)

        #Spieler-Hinzufügen-Button
        ctk.CTkButton(button_frame, text = "Spieler hinzufügen", command = self.add_spieler, corner_radius = 12,
                      font = ("Arial", 20), width = 180, height = 50).grid(row = 1, column = 1, pady = 10, sticky = "ew")
        #Spieler-Entfernen-Button
        ctk.CTkButton(button_frame, text = "Spieler entfernen", command = self.remove_spieler, corner_radius = 12,
                      font = ("Arial", 20), width = 180, height = 50).grid(row = 2, column = 1, pady = 10, sticky = "ew")

        self.aktueller_spieler = 0 
        self.animation = False 
        self.spieler_bearbeitung = True
        self.add_spieler()

        #Spieler hinzufügen
    def add_spieler(self):
        if (self.spieler_bearbeitung == True and len(self.spieler_liste) < max_spieler):
            name = f"Spieler {len(self.spieler_liste) + 1}" #Automatischer Name
            spieler = Spieler(self.spieler_frame, name)
            self.spieler_liste.append(spieler) #Zur Liste hinzufügen

        #Letzten Spieler entfernen
    def remove_spieler(self):
        if (self.spieler_bearbeitung == True and len(self.spieler_liste) > 1):
            spieler = self.spieler_liste.pop()
            spieler.frame.destroy() #Frame entfernen

        #Wird aufgerufen, Wenn Zahl gedrückt wird
    def click(self, zahl):
        if (self.animation == True): #Falls Animations-Anzeige läuft nichts tun
            return
        self.spieler_bearbeitung = False
        #Aktuellen Tipp setzen
        if (self.aktueller_spieler < len(self.spieler_liste)):
            spieler = self.spieler_liste[self.aktueller_spieler]
            spieler.tipp = zahl
            spieler.tipp_label.configure(text = str(zahl))
            self.aktueller_spieler += 1 #Nächster Spieler ist dran
        if (self.aktueller_spieler == len(self.spieler_liste)):
            #Sobald alle Spieler gedrückt haben wird gewürfelt
            self.nummer = random.randint(1, 6)
            self.wuerfel_label.configure(text = str(self.nummer) + "\n\n\n")
            self.after(1500, self.gewinner)

        #Gewinner wird ermittelt und dann angezeigt
    def gewinner(self):
        gewinner = []
        for spieler in self.spieler_liste:
            if (spieler.tipp == self.nummer):
                gewinner.append(spieler.name) #Name wird zur Gewinnerliste hinzugefügt
            if (len(gewinner) > 0):
                text = "Gewinner:\n"
                for name in gewinner:
                    text += name + "! "
            else: 
                text = "Kein Gewinner!\n"
            self.wuerfel_label.configure(text = text + "\n\n") 
            self.after(gewinner_anzeige, self.reset) #Reset wird eingeleitet

        #Spiel wird zurückgesetzt und neugestartet 
    def reset(self):
        for spieler in self.spieler_liste:
            spieler.tipp = None
            spieler.tipp_label.configure(text = "") #Tippanzeige wird gelöscht
        self.aktueller_spieler = 0
        self.wuerfel_label.configure(text = "Geben sie ihren Tipp ab!\n\n\n")
        self.animation = False
        self.spieler_bearbeitung = True #Spieleränderung wieder freigegeben

Spiel().mainloop() #mainloop