def cyber_archives():
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    lost_file = "lost_archive.txt"
    try:
        print(f"\nCRISIS ALERT: Attempting access to '{lost_file}'...")
        with open(lost_file) as file:
            data = file.read()
        print(data)
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    finally:
        print("STATUS: Crisis handled, system stable\n")


    classified_file = "classified_vault.txt"
    try:
        print(f"CRISIS ALERT: Attempting access to '{classified_file}'...")
        with open(classified_file) as file:
            data = file.read()
        print(data)
    except  Exception:
        print("RESPONSE: Security protocols deny access")
    finally:
        print("STATUS: Crisis handled, security maintained\n")


    standard_file = "standard_archive.txt"
    try:
        print(f"ROUTINE ACCESS: Attempting access to '{standard_file}'...")
        with open(standard_file) as file:
            data = file.read()
        print(f"SUCCSESS: Archive recovered - ''{data}''")
        print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("STATUS: file does not exist")
    
    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == '__main__':
    cyber_archives()
