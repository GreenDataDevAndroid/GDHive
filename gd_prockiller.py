import psutil
import os

def show_processes():
    print("\n--- TOP PROZESSE (CPU Last) ---")
    print(f"{'PID':<8} | {'Name':<25} | {'CPU %':<8} | {'RAM %':<8}")
    print("-" * 55)

    # Wir holen uns alle Prozesse und sortieren sie nach CPU-Auslastung
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            # .info gibt uns das Dictionary mit den oben definierten Feldern
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    # Sortieren: Höchste Last zuerst
    processes = sorted(processes, key=lambda x: x['cpu_percent'], reverse=True)

    # Nur die Top 10 anzeigen
    for proc in processes[:10]:
        print(f"{proc['pid']:<8} | {proc['name'][:25]:<25} | {proc['cpu_percent']:<8.1f} | {proc['memory_percent']:<8.1f}")

    print("-" * 55)
    
    choice = input("\nGib die PID zum Beenden ein (oder Enter zum Abbrechen): ")
    if choice.strip():
        try:
            pid = int(choice)
            p = psutil.Process(pid)
            p.terminate() # Schickt das Signal zum Beenden
            print(f"Prozess {pid} wurde beendet.")
        except Exception as e:
            print(f"Fehler: {e}")

if __name__ == "__main__":
    show_processes()