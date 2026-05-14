import os
import shutil
from pathlib import Path

def organize_folder(target_path):
    # Definition der Dateitypen
    extensions = {
        ".jpg": "Bilder",
        ".png": "Bilder",
        ".pdf": "Dokumente",
        ".txt": "Dokumente",
        ".py": "Programmierung",
        ".cpp": "Programmierung",
        ".exe": "Programme",
        ".zip": "Archive"
    }

    target = Path(target_path)
    if not target.exists():
        print(f"Fehler: Der Pfad {target} existiert nicht.")
        return

    print(f"Organisiere Ordner: {target.absolute()}...")

    for item in target.iterdir():
        if item.is_file():
            ext = item.suffix.lower()

            if ext in extensions:
                subfolder = extensions[ext]
                subfolder_path = target / subfolder
                subfolder_path.mkdir(exist_ok=True)

                # Datei verschieben
                shutil.move(str(item), str(subfolder_path / item.name))
                print(f"Verschoben: {item.name} -> {subfolder}/")

    print("Sortierung abgeschlossen!")