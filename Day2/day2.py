from typing import List, Tuple


test = [("forward", 5), ("down", 5), ("forward", 8), ("up", 3), ("down", 8), ("forward", 2)]

def main():
    moves = parse_input()
    (pos, depth) = exec_movement(moves)
    print(f"Position: {pos}")
    print(f"Depth: {depth}")
    print(f"Result: {pos*depth}")


def exec_movement(movements: List[Tuple[str, int]]) -> Tuple[int, int]:
    pos = 0
    depth = 0
    aim = 0

    for move in movements:
        x = move[1]
        match move[0]:
            case "forward":
                pos += x
                depth += aim * x
            case "up":
                #depth -= x
                aim -= x
            case "down":
                #depth += x
                aim += x
    return (pos, depth)


def parse_input():
    moves = []
    with open("input.txt", "r") as f:
        for line in f.readlines():
            move = line.split()
            moves.append((move[0], int(move[1])))
    return moves


if __name__ == '__main__':
    main()