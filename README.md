# GDHive - v1.1

Ein modulares Terminal-Dashboard für System-Management, Netzwerk-Diagnose und Automatisierung. Entwickelt von **GreenDataDev** im Rahmen der Ausbildung zum Informationstechnischen Assistenten (ITA).

## 🚀 Features

Das Dashboard vereint verschiedene Werkzeuge unter einer einheitlichen Oberfläche:

### 🖥️ System & Hardware
* **System-Status**: Echtzeit-Überblick über CPU-Last, RAM-Verbrauch und freien Festplattenspeicher.
* **Hardware-Spezifikationen**: Detaillierte Auslese von CPU-Kernen, Frequenzen, Speicherbelegung und Netzwerkschnittstellen.

### 🌐 Netzwerk-Tools
* **Netzwerk-Scanner**: Durchleuchtet das lokale Subnetz mittels Multithreading und zeigt alle aktiven Geräte (IP-Adressen) an.
* **Web- & Port-Checker**: Prüft die Erreichbarkeit von Servern und Diensten auf spezifischen Ports (z.B. Minecraft 25565, HTTP 80).

### 🛠️ Utilities & Verwaltung
* **Datei-Organizer**: Automatisiertes Sortieren von Dateien in Kategorien (Bilder, Dokumente, Programmierung etc.) basierend auf Dateiendungen.
* **Process-Killer**: Terminal-basierter Task-Manager zum Identifizieren und Beenden von Prozessen mit hoher Systemlast.

## 🛠️ Technische Details
* **Sprache**: Python 3
* **Bibliotheken**: `psutil`, `socket`, `threading`, `subprocess`, `platform`
* **Struktur**: Modularer Aufbau (jedes Tool als eigenständiges Python-Modul).

## 📥 Installation & Start
1. Repository klonen:
   ```bash
   git clone [https://github.com/GreenDataDevAndroid/GDHive.git](https://github.com/GreenDataDevAndroid/GDHive.git)