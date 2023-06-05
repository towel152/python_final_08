from django.shortcuts import render
from django.http import HttpResponse
import csv
from mysite import models           # 匯入 mysite 資料夾底下 models.py 中所有的類別
import random


def index(request):
    return render(request, "index.html", locals())

def home(request):
    return render(request, "home.html", locals())

def about(request):
    return render(request, "about.html", locals())

def people(request):
    models.crimeData.objects.all().delete()  
    # filename = "C:\python_final_08\python_final_08\people.csv"
    # with open(filename, encoding='utf-8') as fp:
    #     dataread = csv.DictReader(fp)
    #     data = [dict(d) for d in dataread]
    # for item in data:
    #     new_record = models.populationData(
    #         year = int(item['\ufeffstatistic_yyy']),
    #         city = item['site_id'].split(' ')[0],
    #         dist = item['site_id'].split(' ')[1],
    #         quantity = int(item['people_total'])
    #     )
    #     new_record.save()

    # filename = "C:\python_final_08\python_final_08\犯罪資訊.csv"
    # with open(filename, encoding='utf-8') as fp:
    #     dataread = csv.DictReader(fp)
    #     data = [dict(d) for d in dataread]
    # for item in data:
    #     new_record = models.crimeData(
    #         year = item['年份'],
    #         month = item['月份'],
    #         city = item['縣市'],
    #         category = item['類別'],
    #         quantity = item['發生數'],
    #         cleard = item['破獲數']
    #     )
    #     new_record.save()

    data = models.populationData.objects.all()
    return render(request, "dbtest.html", locals())
