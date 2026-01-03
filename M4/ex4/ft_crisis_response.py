"""
This program demonstrates de use of try/except with the 'with' keyword
to handle several files that can be corrupt
"""


def crisis_test(filename: str) -> str | None:
    ret_val: str
    print("\nCRISIS ALERT: Attempting access to '%s'..." % filename)
    with open(filename, 'r') as file:
        ret_val = file.readline()
    return ret_val

def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    for file in ['lost_archive.txt', 'classified_vault.txt', 'standard_archive.txt']:
        try:
            print("SUCCESS: Archive recovered - ``%s''..." % crisis_test(file))
            print("STATUS: Normal operations resumed")
        except FileNotFoundError:
            print("RESPONSE: Archive not found in storage matrix")
            print("STATUS: Crisis handled, system stable")
        except PermissionError:
            print("RESPONSE: Security protocols deny access")
            print("STATUS: Crisis handled, security maintained")
    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()