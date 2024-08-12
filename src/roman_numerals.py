def to_roman(num):
    roman_map = {1: "I", 
                 5: "V",
                 10: "X"}
    
    if num in roman_map:
        return roman_map[num]
    
    # result = ""
    # for value, letter in roman_map.items():
    #     while num >= value:
    #         result += letter
    #         num -= value
    # return result

    elif num == 2:
        return roman_map[1] + roman_map[1]
    elif num == 3:
        return roman_map[1] + roman_map[1] + roman_map[1]
    else: 
        return "hoge"
        