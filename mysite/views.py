from django.shortcuts import render
from django.http import HttpResponse
import csv
from mysite import models           # 匯入 mysite 資料夾底下 models.py 中所有的類別
import random


def index(request):
    mynames = ["全國治安事件", "全台治安事件", "治安事件"]
    myname = random.choice(mynames)
    return render(request, "index.html", locals())

def people(request):
    filename = "C:\python_final_08\python_final_08\people.csv"
    with open(filename, encoding='utf-8') as fp:
        dataread = csv.DictReader(fp)
        data = [dict(d) for d in dataread]
    msg = ''
    for item in data:
        msg = msg + "{}:{}:{}\n".format(
            item['\ufeffstatistic_yyy'],
            item['site_id'],
            item['people_total']
        )
    
    
    return HttpResponse(msg)
