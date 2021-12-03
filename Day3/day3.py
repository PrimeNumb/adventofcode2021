from typing import List, Tuple, Set


test = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010"
    ]

def main():

    values = parse_input()
    gamma_rate = []

    for i in range(len(values[0])):
        bit = most_common_bit(i, values)
        gamma_rate.append(bit)

    gamma_rate = ''.join(gamma_rate)
    print(f"Gamma rate: {gamma_rate}")
    print(f"Gamma rate (dec): {to_dec(gamma_rate)}")
    epsilon = ''.join(inverse(gamma_rate))
    print(f"Epsilon rate: {epsilon}")
    print(f"Epsilon rate (dec): {to_dec(epsilon)}")
    print(f"Result: {to_dec(gamma_rate) * to_dec(epsilon)}")
    print("----------------------------")
    oxy = get_oxy(values)
    co2 = get_co2(values)
    print(f"Oxy: {oxy}")
    print(f"CO2: {co2}")
    print(f"Result: {to_dec(oxy)*to_dec(co2)}")



def get_oxy(values: List[str]) -> str:
    index = 0
    while len(values) > 1:
        expected_bit = most_common_bit(index, values, False)
        values = discard_based_on_bit(expected_bit, index, values)
        index += 1
    return values[0]

def get_co2(values: List[str]) -> str:
    index = 0
    while len(values) > 1:
        expected_bit = least_common_bit(index, values, True)
        values = discard_based_on_bit(expected_bit, index, values)
        index += 1
    return values[0]

def discard_based_on_bit(expected_bit: str, pos: int, numbers: List[str]) -> List[str]:
    new_numbers: List[str] = []

    for elem in numbers:
        if elem[pos] == expected_bit:
            new_numbers.append(elem)
    return new_numbers


def parse_input() -> List[str]:
    with open("input.txt", "r") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].strip()
        return lines

def inverse(binary: str) -> str:
    inv = ['' for _ in range(len(binary))]
    for i in range(len(binary)):
        match binary[i]:
            case '0':
                inv[i] = '1'
            case '1':
                inv[i] = '0'
    return inv

# 0 or 1
def most_common_bit(pos: int, values: List[str], floor: bool = False) -> str:
    zero_freq = 0
    one_freq = 0

    for i in range(len(values)):
        match values[i][pos]:
            case '0':
                zero_freq += 1
            case '1':
                one_freq += 1
    
    if zero_freq == one_freq:
        if floor:
            return "0"
        else:
            return "1"

    if zero_freq > one_freq:
        return "0"
    else:
        return "1"

def least_common_bit(pos: int, values: List[str], floor: bool = False) -> str:
    zero_freq = 0
    one_freq = 0

    for i in range(len(values)):
        match values[i][pos]:
            case '0':
                zero_freq += 1
            case '1':
                one_freq += 1
    
    if zero_freq == one_freq:
        if floor:
            return "0"
        else:
            return "1"

    if zero_freq < one_freq:
        return "0"
    else:
        return "1"

def to_dec(str: str) -> int:
    return int(str, 2)

if __name__ == '__main__':
    main()