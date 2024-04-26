import csv

def all_same(lst):
    if len(lst) <= 1:
        return True
    return all(item == lst[0] for item in lst)


if __name__ == "__main__":
    file_name = "data.csv"

    data = dict()

    with open(file_name, encoding='utf-8') as r_file:
        csv_data = csv.reader(r_file, delimiter=' ')
        c = 0
        for i in csv_data:
            if c ==0:
                c = 1
                continue
            sum = i[-1].replace(' ', '').replace('"', '').replace(',', '')
            uname = i[-4].replace('"', '').replace(',', '')
            time = int(i[0].replace(' ', '').replace(',', '').replace('"', ''))
            pn = i[-3]

            uname = uname + ';' + pn + sum 

            if uname not in data:
                data[uname] = 1
            else:
                data[uname] +=1


    data = sorted(data.items(), key=lambda item: item[1])

    for uname, info in data:
        # if all_same(info['same_amount_time']):
        #     print(uname, info['time_amount'], info['same_amount_time'])
        print('\n', uname, info)


    with open('key', 'wb+') as f:
        a = 'CTho152;+7 920 666 87 15'.encode('utf-8')
        f.write(a)