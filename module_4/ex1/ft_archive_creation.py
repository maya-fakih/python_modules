def ft_archive_creation():
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")

    file_name = "new_discovery.txt"

    try:
        print(f"\nInitializing new storage unit: {file_name}")
        new_file = open(file_name, 'w')
        print("Storage unit created successfully...")

        print("\nInscribing preservation data...")

        lines = [
                    "[ENTRY 001] New quantum algorithm discovered",
                    "[ENTRY 002] Efficiency increased by 347%",
                    "[ENTRY 003] Archived by Data Archivist trainee"
                ]

        for line in lines:
            new_file.write(line)
            print(line)

        print("\nData inscription complete. Storage unit sealed.")
        print(f"Archive {file_name} is ready for long-term preservation.")
    except Exception:
        print("Error archiving data...")


if __name__ == '__main__':
    ft_archive_creation()
