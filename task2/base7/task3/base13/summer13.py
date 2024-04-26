
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
        return "Ошибка: Основание системы счисления должно быть от 2 до 16"
    
    n_ary_number = ""
    while decimal_number > 0:
        remainder = decimal_number % base
        if remainder < 10:
            n_ary_number = str(remainder) + n_ary_number
        else:
            n_ary_number = chr(remainder - 10 + ord('A')) + n_ary_number  
        decimal_number = decimal_number // base
    
    return n_ary_number
       

if __name__ == "__main__":

    sum = 0
 
    with open('task.txt') as f:
        lines = [line.rstrip('\n') for line in f]

    for i in lines:
        base = 7
        if i[1] =='t':
            base = 13

        
        if (base == 13):
            i = i.split('t')[1]
        print(i, ' ', dec_to_base(i, base))
        sum += dec_to_base(i, base)

print(base_to_dec(sum, 13))

