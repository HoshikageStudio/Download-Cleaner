from pathlib import Path
import tkinter as tk
from tkinter import scrolledtext

# Pfad zum Download-Ordner holen
download_ordner = Path.home() / "Downloads"
print("Aufräumen gestartet in:", download_ordner)

# Zuordnung
ORDNER_REGELN = {
    ".png": "Bilder",
    ".jpg": "Bilder",
    ".jpeg": "Bilder",
    ".pdf": "Dokumente",
    ".txt": "Dokumente",
    ".docx": "Dokumente",
    ".zip": "Archive",
    ".rar": "Archive",
    ".exe": "Programme",
}

def aufraeumen():
    log_box.delete("1.0", tk.END)
    download_ordner = Path.home() / "Downloads"
    log_box.insert(tk.END, f"suche in: {download_ordner}\n\n")
    
    verschiebezahl = 0
# Durchsuchen des Ordners
    for datei in download_ordner.iterdir():
        # Prüfung, ob es eine Datei ist
        if datei.is_file():
            # Wandeln der Endung mit lower() in Kleinbuchstaben
            endung = datei.suffix.lower()
            
            # Prüfung, ob Endung im Wörterbuch vorhanden
            if endung in ORDNER_REGELN:
                kategorie = ORDNER_REGELN[endung]
                
                # Ziel-Ordner bauen
                ziel_ordner = download_ordner / kategorie

                # Erstellen eines nicht vorhandenen Ordners
                ziel_ordner.mkdir(exist_ok=True)
                
                # Vollständigen neuen Pfad für die Datei definieren
                neuer_ipfad = ziel_ordner / datei.name
                
                # Sicherheitsüberprüfung: Existiert die Datei bereits dort?
                if neuer_pfad.exists():
                    log_box(tk.END, f"[ÜBERSPRUNGEN] {datei.name} existiert bereits in {kategorie}/")
                else:
                    # Eigentliches Verschieben
                    datei.rename(neuer_pfad)
                    log_box.insert(tk.END, f"[VERSCHOBEN] {datei.name} -> {kategorie}/")
                    verschiebezahl += 1
            else:
                # Dateien ohne passende Regel werden nicht angefasst
                pass

    log_box.insert(tk.END, f"\nFertig! {verschiebezahl} Dateien sortiert.")
    
# Fenster aufbauen
fenster = tk.Tk()
fenster.title("Download Cleaner")
fenster.geometry("520x400")
fenster.iconbitmp("app_icon.ico")

title = tk.Label(fenster, text ="Downloads Sortierer", font=("Arial", 14, "bold"))
title.pack(pady=10)

start_button = tk.Button(
    fenster,
    text="Jetzt Downloads aufräumen",
    command=aufraeumen,
    bg="#2ecc71",
    fg="white",
    font=("Arial", 11, "bold"),
    padx=10,
    pady=5,
)
start_button.pack(pady=5)

log_box = scrolledtext.ScrolledText(fenster, width=60, height=15)
log_box.pack(padx=10, pady=10)
fenster.mainloop()