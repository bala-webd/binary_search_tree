

class RomanNumeralsToNumber(object):
    def __init__(self) -> None:
        self.roman_constants = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }

    def roman_to_int(self, roman_string):
        romans = list(roman_string)
        result = 0
        previous_number = []
        for roman in romans:
            converted_number = self.roman_constants.get(roman, 0)
            if result == 0:
                previous_number.append(converted_number)
                result += converted_number
            elif ((result > 0) and (previous_number[-1] < converted_number)):
                previous_number[-1] = converted_number - previous_number[-1]
                result = sum(previous_number)
            else:
                result += converted_number
                previous_number.append(converted_number)
        return result

    def __del__(self):
        pass


roman_numerals_to_number = RomanNumeralsToNumber()
given_roman_number = str(input("Enter Roman Number: "))
print("Output", roman_numerals_to_number.roman_to_int(given_roman_number))
