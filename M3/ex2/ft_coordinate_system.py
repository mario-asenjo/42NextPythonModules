"""
Program that displays the distance betweeen two 3D points
"""


import sys
import math


def calculate_distance(x1: int, y1: int, z1: int, x2: int, y2: int,
                       z2: int) -> float:
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)


def parse_arguments(args: list[str], pos: int) -> tuple[int, int, int] | None:
    start: tuple[int, int, int]
    try:
        start = (int(args[pos].split(',')[0]), int(args[pos].split(',')[1]),
                 int(args[pos].split(',')[2]))
        return start
    except ValueError as e:
        print("Error parsing coordinates:", e)
        print(f"Error details - Type: {e.__class__.__name__}, Args: {e.args}")


def main(args: list[str]) -> None:
    initial_pos: tuple
    print("=== Game Coordinate System ===")
    argc: int = len(args)
    position = (10, 20, 5)
    player = (0, 0, 0)
    print("\nPosition created:", position)
    print(f"Distance between {player} and {position}: %.2f" %
          calculate_distance(*player, *position))
    if argc == 3:
        print('\nParsing coordinates: "%s"' % args[1])
        try:
            initial_pos = parse_arguments(args, 1)
            print("Parsed position:", initial_pos)
            print(f"Distance between {player} and {initial_pos}: %.1f" %
                  calculate_distance(*player, *initial_pos))
            print('\nParsing invalid coordinates: "%s"' % args[2])
        except TypeError:
            return
        try:
            parse_arguments(args, 2)
        except TypeError:
            return
    else:
        print("\n[WARN] Please use the program this way:",
              'python3 ft_coordinate_system.py "X1, Y1, Z1" "X2, Y2, Z2"')
    print("\nUnpacking demonstration:")
    print("Player at: x=%d, y=%d, z=%d" % position)
    print("Coordinates: X=%d, Y=%d, Z=%d" % position)


if __name__ == "__main__":
    main(sys.argv)
