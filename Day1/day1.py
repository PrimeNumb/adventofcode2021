from typing import Optional


from typing import List

test_measurements = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

def main():
    values = parse_input()
    print(nr_of_increases(values))

def parse_input() -> List[int]:
    values = []
    with open("input.txt", "r") as f:
        values = f.readlines()

    for i in range(len(values)):
        values[i] = int(values[i].strip('\n'))

    print(values)
    return values

def nr_of_increases(values: List[int]) -> int:
    increases = 0
    for i in range(1, len(values)):
        if values[i-1] < values[i]:
            increases += 1
    return increases


if __name__ == '__main__':
    main()