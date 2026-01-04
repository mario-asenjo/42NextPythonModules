"""
This program demonstrates the use of with keyword and context managers
"""
from io import TextIOWrapper, _WrappedBuffer


def read_and_print_file(extraction_file: TextIOWrapper[_WrappedBuffer]
                        ) -> None:
    """Function that reads a full file and prints contents"""
    extraction_file.seek(0)
    for line in extraction_file:
        print("{[}%s{]} %s" % (line[line.find('[') + 1:line.find(']')],
                               line[line.find(']') + 1: -1]))


def main() -> None:
    """Main function of the program that opens files and calls functions"""
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("Initiating secure vault access...")
    with open('classified_data.txt', 'r') as extraction_file:
        with open('secure_preservation.txt', 'w+') as preserve_file:
            print("Vault connection established with failsafe protocols")
            print("\nSECURE EXTRACTION:")
            read_and_print_file(extraction_file)
            print("\nSECURE PRESERVATION:")
            preserve_file.write("[CLASSIFIED] New security protocols archived")
            read_and_print_file(preserve_file)
    print("Vault automatically sealed upon completion")
    print("\nAll vault operations  completed with maximum security.")


if __name__ == "__main__":
    main()
