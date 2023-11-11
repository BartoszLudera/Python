def roman_to_arabic(roman):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    arabic = 0
    prev_value = 0

    for numeral in reversed(roman):
        value = roman_numerals[numeral]
        if value < prev_value:
            arabic -= value
        else:
            arabic += value
        prev_value = value

    return arabic

def arabic_to_roman(arabic):
    if not 0 < arabic < 4000:
        raise ValueError("Number out of range 1-3999")

    roman_numerals = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
                      50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

    roman = ""
    for value, numeral in roman_numerals.items():
        count = arabic // value
        arabic %= value
        roman += numeral * count

    return roman


roman_input = 'XVI'
arabic_output = roman_to_arabic(roman_input)
print(f"{roman_input} is {arabic_output} as arabic.")

arabic_input = 641
roman_output = arabic_to_roman(arabic_input)
print(f"{arabic_input} is {roman_output} as roman.")
