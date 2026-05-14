import os
import platform
import gd_sysinfo
import gd_organizer
import gd_hardspec
import gd_netscanner
import gd_prockiller
import gd_webcheck

def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def show_header():
    print("========================================")
    print("           GDHive - v1.1               ")
    print("      Created by GreenDataDev          ")
    print("========================================")

def main():
    while True:
        clear_screen()
        show_header()
        print("1. System-Status anzeigen")
        print("2. Datei-Organizer")
        print("3. Hardware-Spezifikationen")
        print("4. Netzwerk-Scanner")
        print("5. Prozess-Manager")
        print("6. Web & Server Check")
        print("0. Beenden")
        
        choice = input("\nWähle eine Option: ")

        if choice == "1":
            clear_screen()
            show_header()
            print("--- SYSTEM-STATUS ---")
            gd_sysinfo.get_system_status()
            input("\nDrücke Enter, um zum Menü zurückzukehren...")
        elif choice == "2":
            clear_screen()
            show_header()
            print("--- DATEI-ORGANIZER ---")
            pfad = input("Welchen Ordner soll ich sortieren? (Punkt '.' für aktuellen): ")
            gd_organizer.organize_folder(pfad)
            input("\nFertig! Drücke Enter...")
        elif choice == "3":
            clear_screen()
            show_header()
            print("--- HARDWARE-SPEZIFIKATIONEN (DETAILLIERT) ---")
            gd_hardspec.show_specs()
            input("\nDrücke Enter, um zum Menü zurückzukehren...")
        elif choice == "4":
            clear_screen()
            show_header()
            print("--- NETZWERK-SCANNER ---")
            gd_netscanner.scan_network()
            input("\nDrücke Enter, um zum Menü zurückzukehren...")
        elif choice == "5":
            clear_screen()
            show_header()
            print("--- PROZESS-MANAGER ---")
            gd_prockiller.show_processes()
            input("\nDrücke Enter, um zum Menü zurückzukehren...")
        elif choice == "6":
            clear_screen()
            show_header()
            print("--- WEB & SERVER CHECK ---")
            gd_webcheck.run_check()
            input("\nDrücke Enter, um zum Menü zurückzukehren...")
        elif choice == "0":
            print("\nGDHive wird beendet. Bis bald!")
            break
        else:
            print("\nUngültige Auswahl!")
            input("\nWeiter mit Enter...")

if __name__ == "__main__":
    main()