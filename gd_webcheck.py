import socket

def check_service(ip, port):
    # Erstellt ein Socket-Objekt (AF_INET = IPv4, SOCK_STREAM = TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2) # Wir warten maximal 2 Sekunden
    
    try:
        # Versucht eine Verbindung zum Port aufzubauen
        result = s.connect_ex((ip, port))
        if result == 0:
            print(f"[ ONLINE ] Port {port} ist erreichbar auf {ip}")
        else:
            print(f"[ OFFLINE ] Port {port} ist NICHT erreichbar auf {ip}")
    except Exception as e:
        print(f"Fehler beim Prüfen: {e}")
    finally:
        s.close()

def run_check():
    target = input("IP oder URL (z.B. google.de oder dein-server.de): ")
    if not target.strip():
        return

    print("\nBeliebte Ports:")
    print("80/443 (Web), 25565 (Minecraft), 22 (SSH), 21 (FTP)")
    port_input = input("Welchen Port soll ich prüfen? ")
    
    try:
        port = int(port_input)
        print(f"Prüfe {target} auf Port {port}...")
        check_service(target, port)
    except ValueError:
        print("Ungültiger Port! Bitte eine Zahl eingeben.")

if __name__ == "__main__":
    run_check()