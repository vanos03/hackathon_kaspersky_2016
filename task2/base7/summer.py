
def fromAny(x, y):
    b = []
    for j in x:
        if j in ['0','1','2','3','4','5','6','7','8','9']:
            b.append(int(j))
        else:
            k = ord('A') + ord(j) - 120
            b.append(k)
    b.reverse()
    a = 0
    for i in range(0, len(b)):
        a += b[i] * (y**i)
    return a


def decimal_to_septenary(number):
    if number == 0:
        return "0"
    
    result = ""
    while number > 0:
        remainder = number % 7
        result = str(remainder) + result
        number = number // 7
    
    return result
       

if __name__ == "__main__":

    sum = 0
 
    with open('task.txt') as f:
        lines = [line.rstrip('\n') for line in f]

    for i in lines:
        print(i, ' ', fromAny(i, 7))
        sum += fromAny(i, 7)

print(decimal_to_septenary(sum))