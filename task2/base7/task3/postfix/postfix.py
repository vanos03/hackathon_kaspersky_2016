
def dec_to_base(number, base):
    decimal_number = 0
    power = 0
    
    for digit in reversed(str(number)):
        if digit.isdigit():
            digit_value = int(digit)
        else:
            digit_value = ord(digit) - ord('A') + 10 
        
        decimal_number += digit_value * (base ** power)
        power += 1
    
    return decimal_number

def base_to_dec(decimal_number, base):
    if base > 16 or base < 2:
        return "Основание системы счисления должно быть от 2 до 16"
    
    n_ary_number = ""
    while decimal_number > 0:
        remainder = decimal_number % base
        if remainder < 10:
            n_ary_number = str(remainder) + n_ary_number
        else:
            n_ary_number = chr(remainder - 10 + ord('A')) + n_ary_number  
        decimal_number = decimal_number // base
    
    return n_ary_number


def shef(a, b):
    return ~(a&b)

def pears(a, b):
    return ~(a|b)
      
def implic(a, b):
    return ~b|a

def ecv(a, b):
    return ~(a^b)

if __name__ == "__main__":
    res = []
    with open("key", 'r') as file:
        lines = file.readlines()
    for i in lines:
        i = i.rstrip()
        if i in ["#", "!", ">", "="]:
            a = int(res.pop())
            b = int(res.pop())
            if i == "#":
                a = shef(a,b)
                res.append(a)
            elif i == "!":
                a = pears(a,b)
                res.append(a)
            elif i == ">":
                a = implic(a, b)
                res.append(a)
            elif i == "=":
                a = ecv(a,b)
                res.append(a)
        else:      
            a = int(str(i), 7)
            res.append(a)

print(base_to_dec(res[0], 7))

with open("key", "w+") as f:
    f.write(base_to_dec(res[0], 7))