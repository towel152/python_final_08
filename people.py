import csv
import re
filename = "people.csv"
with open(filename, encoding='utf-8') as fp:
    dataread = csv.DictReader(fp)
    data = [dict(d) for d in dataread]
for item in data:
    print("{} {} {} {}".format(
        item['\ufeffstatistic_yyy'],
        item['site_id'].split(' ')[0],
        item['site_id'].split(' ')[1],
        item['people_total']
    ))
# print(data)

