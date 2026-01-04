"""
This program retrieves preserved information from an ancient text
"""


def main() -> None:
    """Main function of the program shows file handling"""
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    try:
        print("\nAccessing Storage Vault: ancient\\_fragment.txt")
        with open('ancient_fragment.txt', 'r') as file:
            print("Connection established...")
            data: list[str] = [line[:-1] for line in file]
            fragments: list[str] = [
                '{[}%s{]}' % line[line.find('[') + 1:line.find(']')]
                for line in data
            ]
            sentences: list[str] = [
                line[line.find(']') + 1:] for line in data
            ]
            full_sentences: list[str] = [
                f"{fr}{sent}" for fr, sent in zip(fragments, sentences)
            ]
            print("\nRECOVERED DATA:")
            for sentence in full_sentences:
                print(sentence)
        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first "
              "and paste ancient_fragment.txt in this directory.")


if __name__ == "__main__":
    main()
