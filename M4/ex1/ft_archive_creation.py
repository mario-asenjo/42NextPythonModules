"""
This program demonstrates file creation and writing
"""


def main() -> None:
    data: list[str] = [
        "{[}ENTRY 001 {]} New quantum algorith discovered",
        "{[}ENTRY 002 {]} Efficiency increased by 347 %",
        "{[}ENTRY 003 {]} Archived by Data Archivist masenjo"
    ]
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    try:
        print("\nInitializing new storage unit: new_discovery.txt")
        with open('new_discovery.txt', 'w') as file:
            print("Storage unit created successfully...")
            print("\nInscribing preservation data...")
            for sentence in data:
                print(sentence)
                file.write(sentence+"\n")
        print("\nData inscription complete. Storage unit sealed.")
        print("Archive 'new_discovery.txt' ready for long-term preservation.")
    except IOError:
        print("ERROR: Could not write to the file...")


if __name__ == "__main__":
    main()
