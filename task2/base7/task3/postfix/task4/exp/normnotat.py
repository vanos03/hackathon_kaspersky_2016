def shef(a, b):
    return ~(a & b)

def pears(a, b):
    return ~(a | b)

def implic(a, b):
    return ~b | a

def ecv(a, b):
    return ~(a ^ b)


def dec_to_base(number, base):
    dec_num = 0
    power = 0
    
    for digit in reversed(str(number)):
        if digit.isdigit():
            dig_val = int(digit)
        else:
            dig_val = ord(digit) - ord('A') + 10  
        
        dec_num += dig_val * (base ** power)
        power += 1
    
    return dec_num

def base_to_dec(num, base):
    if base > 16 or base < 2:
        return "Ошибка: Основание системы счисления должно быть от 2 до 16"

    dec_num = 0
    power = 0

    for digit in reversed(num):
        if digit.isdigit():
            dig_val = int(digit)
        else:
            dig_val = ord(digit) - ord('A') + 10

        dec_num += dig_val * (base ** power)
        power += 1

    return dec_num




def inf_to_postf(exp):
    precedence = {'#': 1, '!': 1, '>': 1, '=': 1, '(': 0}
    stack = []
    postf = []

    
    for i in exp:
        base = 7
        if i not in ["#", "!", ">", "=", "(", ")"]:
            if i[1] == 't':
                base = 13
            if (base == 13):
                i = i.split('t')[1]
            a = base_to_dec(i, base)
            print(a)
        
            postf.append(a)
        elif i == '(':
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                postf.append(stack.pop())
            stack.pop()
        elif i in precedence:
            while stack and precedence.get(stack[-1], 0) >= precedence[i]:
                postf.append(stack.pop())
            stack.append(i)
    
    while stack:
        postf.append(stack.pop())
    
    return postf

def calc_postf(postf_exp):
    operands = []

    for i in postf_exp:

        base = 7
        if i not in ["#", "!", ">", "=", "(", ")"]:
        
            operands.append(i)
        elif i == '#':
            b = operands.pop()
            a = operands.pop()
            operands.append(shef(a, b))
        elif i == '!':
            b = operands.pop()
            a = operands.pop()
            operands.append(pears(a, b))
        elif i == '>':
            b = operands.pop()
            a = operands.pop()
            operands.append(implic(a, b))
        elif i == '=':
            b = operands.pop()
            a = operands.pop()
            operands.append(ecv(a, b))
    return operands[0]

def calc(exp):

    operands = exp.split(' ')
    print(operands)
    postf_exp = inf_to_postf(operands)
    res = calc_postf(postf_exp)
    return  res


if __name__ == "__main__":
    exp = "15263526142626 ! ( 0t1A90C3A7923 > 25364213362511 )"
    res = calc(exp)
    print(" res:",  res)

    res = '0t336BA82AA1ACCC'.encode('utf-8')
    with open("key", "wb+") as f:
        f.write(res)