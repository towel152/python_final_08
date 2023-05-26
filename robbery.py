import csv
filename = "robbery.csv"
with open(filename, encoding='utf-8') as fp:
    dataread = csv.DictReader(fp)
    data = [dict(d) for d in dataread]
for item in data:
    print("{} {} {} {}".format(
        item['\ufeff"強盜概況"'].split("/")[0],
        item['\ufeff"強盜概況"'].split("/")[1],
        item['發生數'],
        item['破獲數']
    ))
# print(data)