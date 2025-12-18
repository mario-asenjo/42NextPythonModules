"""
This program shows how to handle program arguments correctly and use
them to get info about what the user might want to do with the program
"""


import sys

def main(args: list[str]) -> None:
    """
    Function that displays information on the
    arguments given to the program
    """
    print("=== Command Quest ===")
    argc: int = len(args)
    if argc < 2:
        print("No arguments provided!")
        print("Program name:", args[0].split('\\')[-1])
    else:
        print("Program name:", args[0].split('\\')[-1])
        print("Arguments recieved:", len(args[1:]))
        i: int = 1
        for arg in args[1:]:
            print(f"Argument {i}: {arg}")
            i += 1
    print("Total arguments:", argc)
if __name__ == "__main__":
    main(sys.argv)