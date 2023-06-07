import csv
filename = "犯罪資訊.csv"
with open(filename, encoding='utf-8') as fp:
    dataread = csv.DictReader(fp)
    data = [dict(d) for d in dataread]
for item in data:
    print("{} {} {} {} {}".format(
        item['概況'].split("/")[0].split('')[0],
        item['概況'].split("/")[0].split('')[1],
        item['概況'].split("/")[1],
        item['類別'],
        item['發生數'],
        item['破獲數']
    ))
# print(data)