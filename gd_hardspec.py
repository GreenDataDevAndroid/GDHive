import psutil
import platform
import subprocess
import os

def get_size(bytes, suffix="B"):
    """
    Rechnet Bytes in größere Einheiten um (KB, MB, GB, etc.)
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def show_specs():
    print("\n" + "="*40)
    print("      GDHardspec - System Report")
    print("="*40)

    # 1. Basis-Systeminfos
    uname = platform.uname()
    print(f"System:    {uname.system}")
    print(f"Node Name: {uname.node}")
    print(f"Release:   {uname.release}")
    print(f"Maschine:  {uname.machine}")

    # 2. CPU Infos
    print("\n--- CPU Informationen ---")
    print(f"Physische Kerne: {psutil.cpu_count(logical=False)}")
    print(f"Logische Kerne:   {psutil.cpu_count(logical=True)}")
    
    # Maximale Frequenz
    cpufreq = psutil.cpu_freq()
    if cpufreq:
        print(f"Max Frequenz:    {cpufreq.max:.2f}Mhz")

    # 3. RAM (Arbeitsspeicher)
    print("\n--- Arbeitsspeicher ---")
    svmem = psutil.virtual_memory()
    print(f"Gesamt: {get_size(svmem.total)}")
    print(f"Verfügbar: {get_size(svmem.available)}")
    print(f"Belegt: {get_size(svmem.used)} ({svmem.percent}%)")

    # 4. Festplatten (Laufwerke)
    print("\n--- Laufwerke ---")
    partitions = psutil.disk_partitions()
    for partition in partitions:
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
            print(f"Gerät: {partition.device} ({partition.mountpoint})")
            print(f"  Dateisystem: {partition.fstype}")
            print(f"  Gesamt:      {get_size(partition_usage.total)}")
            print(f"  Belegt:      {get_size(partition_usage.used)} ({partition_usage.percent}%)")
            print(f"  Frei:        {get_size(partition_usage.free)}")
        except PermissionError:
            # Das passiert bei manchen System-Laufwerken
            continue

    # 5. Netzwerk
    print("\n--- Netzwerk ---")
    addrs = psutil.net_if_addrs()
    for interface_name, interface_addresses in addrs.items():
        for address in interface_addresses:
            if str(address.family) == 'AddressFamily.AF_INET':
                print(f"Interface: {interface_name}")
                print(f"  IP-Adresse:  {address.address}")

    print("\n" + "="*40)
    input("\nDrücke Enter, um zum Hauptmenü zurückzukehren...")

if __name__ == "__main__":
    show_specs()