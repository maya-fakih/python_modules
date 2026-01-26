def vault_security():
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")

    print("\nInitiating secure vault access...")
    print("Vault connection established with failsafe protocols")

    try:
        with open("classified_data.txt") as file:
            print("\nSECURE EXTRACTION:")
            print(file.read())

        with open("security_protocols.txt") as file:
            print("\nSECURE PRESERVATION:")
            print(file.read())
        
        print("Vault automatically sealed upon completion")
        print("\nAll vault operations completed with maximum security.")
    except Exception:
        print("You tried to acess files that dont exist")


if __name__ == '__main__':
    vault_security()
