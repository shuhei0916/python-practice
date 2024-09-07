def to_roman(num):
    roman_map = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
        }
        
    result = ""
    for value, letter in roman_map.items():
        while num >= value:
            result += letter
            num -= value
    return result

def main():
    print(to_roman(3))
    print(to_roman(4))
    print(to_roman(6))


if __name__ == '__main__':
    main()