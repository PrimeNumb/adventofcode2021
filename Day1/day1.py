from typing import Optional


from typing import List

test_measurements1 = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
test_measurements2 = [607, 618, 618, 617, 647, 716, 769, 792]

def main():
    values = parse_input()
    #print(sliding_increases(test_measurements2))
    print(sliding_increases(values))

def parse_input() -> List[int]:
    values = []
    with open("input.txt", "r") as f:
        values = f.readlines()

    for i in range(len(values)):
        values[i] = int(values[i].strip('\n'))

    return values


def sliding_increases(values: List[int]) -> int:
    increases = 0

    prev = None
    sum = None
    for i in range(len(values)-2):
        sum = values[i] + values[i+1] + values[i+2]
        if prev is not None and prev < sum:
            increases += 1
        
        prev = sum
            


    return increases

def nr_of_increases(values: List[int]) -> int:
    increases = 0
    for i in range(1, len(values)):
        if values[i-1] < values[i]:
            increases += 1
    return increases


if __name__ == '__main__':
    main()