import subprocess
import threading
import platform
import socket

# Liste für aktive Geräte
active_hosts = []

def ping_host(ip):
    # Der Befehl unterscheidet sich zwischen Windows (-n) und Linux (-c)
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', '-w', '500', ip] # -w 500 ist das Timeout in ms
    
    if subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0:
        active_hosts.append(ip)

def scan_network():
    global active_hosts
    active_hosts = []
    
    # Wir holen uns deine eigene IP, um das Subnetz zu finden
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    # Wir nehmen die ersten drei Teile (z.B. 192.168.178.)
    prefix = ".".join(local_ip.split(".")[:-1]) + "."
    
    print(f"Scanne Netzwerk: {prefix}1 bis {prefix}254...")
    threads = []
    
    # Wir starten für jede IP einen eigenen Thread (Parallelisierung)
    for i in range(1, 255):
        ip = prefix + str(i)
        t = threading.Thread(target=ping_host, args=(ip,))
        t.start()
        threads.append(t)
    
    # Warten, bis alle fertig sind
    for t in threads:
        t.join()
    
    print("\n--- Aktive Geräte im Netzwerk ---")
    active_hosts.sort(key=lambda x: int(x.split(".")[-1])) # Sortiert nach der letzten Zahl
    for host in active_hosts:
        status = "(Das bist du)" if host == local_ip else ""
        print(f"[ ONLINE ] {host} {status}")
    
    if not active_hosts:
        print("Keine Geräte gefunden.")
    
    print("-" * 30)

if __name__ == "__main__":
    scan_network()