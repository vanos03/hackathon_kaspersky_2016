import csv

def is_number(s):
    try:
        float(s) 
        return True
    except ValueError:
        return False
    
def is_valid_luhn(digits):
    digits = digits.replace(' ', '')
    if is_number(digits):
        
        sum = 0
        parity = len(digits) % 2

        for i in range(len(digits)):
            dig = int(digits[i])
            if i % 2 == parity:
                dig = dig*2
                if dig > 9:
                    dig -= 9
            sum += dig
        return (sum % 10) == 0
            
    else:
         return False


if __name__ == "__main__":
    file_name = "data.csv"

    card_num = dict()

    with open(file_name, encoding='utf-8') as r_file:
        csv_data = csv.reader(r_file, delimiter = ",")
        
        for i in csv_data:
            cn = i[-1].replace('"', '').replace(' ', '')

            if is_valid_luhn(cn) == True:
                key = (i[0] + ';' + i[-3]).replace('"', '').replace(' ', '')
                # print(i)
                card_num.update({cn: key})
    sorted_dict_keys = sorted(card_num.items())

    for i in range(100):
        print(i, sorted_dict_keys[i])

    with open("key", "wb") as f:
        f.write("RPet424;mbf5Xif")
