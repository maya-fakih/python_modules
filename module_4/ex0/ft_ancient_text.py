def ft_ancient_text():
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    file_name = "ancient_fragment.txt"
    try:
        print(f"\nAcessing Storage Vault: {file_name}")
        file = open(file_name, 'r')
        print("Connection established...")

        print("\nRECOVERED DATA:")
        data = file.read()
        print(data)
        file.close()

        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("File was not found...")


if __name__ == '__main__':
    ft_ancient_text()
