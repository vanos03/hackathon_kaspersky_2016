import csv

if __name__ == "__main__":
    file_name = "data.csv"

    data = dict()

    with open(file_name, encoding='utf-8') as r_file:
        csv_data = csv.reader(r_file, delimiter=',')
        c = 0
        for i in csv_data:
            if c ==0:
                c = 1
                continue
            sum = i[-1].replace(' ', '')
            src = i[-2].replace('"', '')
            # print(src, ' ', sum)

            if src not in data:
                data[src] = {'dst': 1, 'sum': float(sum)}
            else:
                data[src]["dst"] += 1
                data[src]['sum'] += float(sum)

    data = sorted(data.items(), key=lambda item: item[1]['sum'])

    for src, info in data:
        print(src, info['dst'], info['sum'])

    with open('key', 'wb+') as f:
        a = 'HFis206'.encode('utf-8')
        f.write(a)