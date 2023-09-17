class Solution:
    def intToRoman(self, num: int) -> str:
        rm = {
        1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X",
        40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 
        500: "D", 900: "CM", 1000: "M"
        }

        s = ""

        # Iterating through the map in reverse order
        for key in sorted(rm.keys(), reverse=True):
            while num >= key:
                s += rm[key]
                num -= key

        return s