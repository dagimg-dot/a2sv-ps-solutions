class Solution:
    def intToRoman(self, num: int) -> str:
        roman_dict = {1000: 'M',500: 'D',100: 'C',50: 'L',10: 'X',5: 'V',1: 'I'}     
        keys = list(roman_dict.keys())
        roman = ''
        while num > 0:
            str_num = str(num)
            k = len(str_num)
            conv = 0
            for i in range(len(keys)):
                if num >= keys[i]:
                    conv = keys[i]
                    if num + 10**(k-1) >= keys[i-1] and i > 0:
                        roman += roman_dict[10**(k-1)]
                        roman += roman_dict[keys[i-1]]
                        num -= keys[i-1] - 10**(k-1)
                        break
                    else:
                        roman += roman_dict[conv]
                        num -= conv
                        break  

        return roman
        