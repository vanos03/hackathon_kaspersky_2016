import csv

if __name__ == "__main__":
    file_name = "data.csv"

    data = dict()

    with open(file_name, encoding='utf-8') as r_file:
        csv_data = csv.reader(r_file, delimiter=' ')

        for i in csv_data:
            ua = i[-1].replace('"', '')
            ip = i[1].replace('"', '').replace(' ', '')
            # time = i[0].replace('"', '').replace(' ', '')

            ua = ua + ' ' + ip

            if ua not in data:
                data[ua] = 1
            else:
                data[ua] += 1

    data = sorted(data.items(), key=lambda item: item[1])

    # for ua, count in data:
    #     print(count, ua)

print(data[-1][0])
