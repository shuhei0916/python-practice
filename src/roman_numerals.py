def to_roman(num):
    roman_map = {1: "I", 
                 4: "IV",
                 5: "V",
                 9: "IX", 
                 10: "X"}
    
    if num in roman_map:
        return roman_map[num]
    
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