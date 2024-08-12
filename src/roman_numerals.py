def to_roman(num):
    roman_map = {1: "I", 
                 5: "V",
                 10: "X"}
    
    if num in roman_map:
        return roman_map[num]
    else:
        return "II"