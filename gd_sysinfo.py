import psutil
import platform

def get_system_status():
    print("--- SYSTEM STATUS ---")
    
    # Betriebssystem
    system = platform.system()
    version = platform.release()
    print(f"OS: {system} {version}")
    
    # CPU Auslastung
    print("CPU wird gemessen (1s)...")
    cpu_usage = psutil.cpu_percent(interval=1)
    
    # RAM Informationen
    ram = psutil.virtual_memory()
    total_ram = round(ram.total / (1024**3), 2)
    used_ram = round(ram.used / (1024**3), 2)
    
    print(f"CPU Last: {cpu_usage}%")
    print(f"RAM:      {used_ram} GB von {total_ram} GB genutzt ({ram.percent}%)")
    
    # Festplattenplatz (Wählt C: unter Windows, / unter Unix)
    root_path = 'C:\\' if platform.system() == "Windows" else '/'
    disk = psutil.disk_usage(root_path)
    free_disk = round(disk.free / (1024**3), 2)
    print(f"Freier Speicher: {free_disk} GB")
    print("-" * 21)