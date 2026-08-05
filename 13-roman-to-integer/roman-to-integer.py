# class Solution:
#     def romanToInt(self, s: str) -> int:
#         translations = {
#             "I": 1,
#             "V": 5,
#             "X": 10,
#             "L": 50,
#             "C": 100,
#             "D": 500,
#             "M": 1000
#         }
#         number = 0
#         s = s.replace("IV", "IIII").replace("IX", "VIIII")
#         s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
#         s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
#         for char in s:
#             number += translations[char]
#         return number
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        result = 0
        for i in range(len(s)):
            if i + 1 < len(s) and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
                result -= roman_to_int[s[i]]
            else:
                result += roman_to_int[s[i]]
        return result