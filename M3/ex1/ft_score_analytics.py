"""
Program that computes analysis on score data given as arguments
"""


import sys


def parse_numbers(args: list[str]) -> list[int]:
    """Serializes a string list into an integer list"""
    numeric_list: list[int] = []
    for arg in args[1:]:
        try:
            numeric_list.append(int(arg))
        except ValueError:
            print(f"[ERROR]: Invalid arg: {arg}. Not computing this score.")
    return numeric_list


def analyze_scores(scores: list[int]) -> None:
    """Prints information on the recieved list"""
    print("Scores processed:", scores)
    print("Total players:", len(scores))
    print("Total score:", sum(scores))
    print("Average score:", sum(scores) / len(scores))
    print("High score:", max(scores))
    print("Low score:", min(scores))
    print("Score range:", max(scores) - min(scores))


def main(args: list[str]) -> None:
    """Main function, receives a list of strings, sys.argv, and analizes it"""
    print("=== Player Score Analytics ===")
    argc: int = len(args)
    if argc < 2:
        print(
            "No scores provided. Usage: "
            "python3 ft_score_analytics.py <score1> <score2> ..."
        )
    else:
        numeric_list: list[int] = parse_numbers(args)
        analyze_scores(numeric_list)


if __name__ == "__main__":
    main(sys.argv)
