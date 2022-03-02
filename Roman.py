class Roman:
    def __init__(self,n):
        self.number = n
        self.roman_digits = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I',
        }

    def convert_int_to_roman(self):
        number = self.number
        keys_list = list(self.roman_digits)
        result = ''
        i = 0
        while  number > 0:
            for _ in range(number // keys_list[i]):
                result += self.roman_digits[keys_list[i]]
                number -= keys_list[i]
            i += 1
        return result

r1 = Roman(1290)
print(r1.convert_int_to_roman())
