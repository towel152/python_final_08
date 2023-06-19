from django.shortcuts import render
from django.http import HttpResponse
import csv
from mysite import models           # 匯入 mysite 資料夾底下 models.py 中所有的類別
import random
from django.db.models import Sum
from django.db.models import Sum, F, FloatField
from django.db.models.functions import Cast
from django.db.models import Case, When, Sum, Value



def index(request):
    return render(request, "index.html", locals())

def home(request):
    return render(request, "home.html", locals())

def about(request):
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
    return render(request, "about.html", locals())

def data(request):
    return render(request, "data.html", locals())

def quantity(request):
    years_data = models.crimeData.objects.values('year').annotate(total_quantity=Sum('quantity'), total_cleard=Sum('cleard'))
    years = [data['year'] for data in years_data]

    cities = models.cityData.objects.values('city')

    selected_year = request.GET.get('year')
    selected_city = request.GET.get('city')

    data = models.crimeData.objects.all()

    if selected_year:
        data = data.filter(year=int(selected_year))
    if selected_city:
        data = data.filter(city=selected_city)

    chart_data = data.values('category').annotate(quantity=Sum('quantity'), cleard=Sum('cleard'))

    return render(request, "quantity.html", {'years': years, 'cities': cities, 'selected_year': selected_year, 'selected_city': selected_city, 'data': chart_data})


def crime_rates(request):
    years_data = models.crimeData.objects.values('year').annotate(total_quantity=Sum('quantity'), total_cleard=Sum('cleard'))
    years = [data['year'] for data in years_data]

    cities = models.cityData.objects.values('city')

    selected_year = request.GET.get('year')
    selected_city = request.GET.get('city')

    data = models.crimeData.objects.all()

    if selected_year:
        data = data.filter(year=int(selected_year))
    if selected_city:
        data = data.filter(city=selected_city)

    p_data = models.populationData.objects.all()

    if selected_year:
        p_data = p_data.filter(year=int(selected_year))
    if selected_city:
        p_data = p_data.filter(city=selected_city)

    # 獲取人口數據，將同一縣市的不同鄉鎮人口數相加
    population_data = p_data.values('city').annotate(total_population=Sum('quantity')).order_by('city')

    chart_data = data.values('category', 'city').annotate(
        quantity=Sum('quantity'),
        cleard=Sum('cleard')
    )

    # 將縣市的人口數據合併到犯罪數據中
    for item in chart_data:
        item['population'] = 0  # 設定預設值
        city = item['city']
        city_data = population_data.filter(city=city)
        if city_data.exists():
            item['population'] = city_data.values('total_population').first()['total_population']

    # 計算犯罪率和破獲率
    for item in chart_data:
        population = item['population']
        if population != 0 and item['quantity'] != 0:  # 確保人口數和犯罪數都不為零
            item['crime_rate'] = (item['quantity'] / population) * 100000  # 犯罪率 = (犯罪數 / 人口數) * 100
            item['clearance_rate'] = (item['cleard'] / item['quantity']) * 100  # 破獲率 = (破獲數 / 犯罪數) * 100
        else:
            item['crime_rate'] = 0
            item['clearance_rate'] = 0


    return render(request, "crimerate.html", {'years': years, 'cities': cities, 'selected_year': selected_year, 'selected_city': selected_city, 'data': chart_data})


def compare(request):
    years_data = models.crimeData.objects.values('year').annotate(total_quantity=Sum('quantity'), total_cleard=Sum('cleard'))
    years = [data['year'] for data in years_data]

    cities = models.cityData.objects.values('city')

    selected_year = request.GET.get('year')
    selected_city_1 = request.GET.get('city1')
    selected_city_2 = request.GET.get('city2')

    data = models.crimeData.objects.all()

    if selected_year:
        data = data.filter(year=int(selected_year))
    if selected_city_1:
        data = data.filter(city=selected_city_1)

    p_data = models.populationData.objects.all()

    if selected_year:
        p_data = p_data.filter(year=int(selected_year))
    if selected_city_1:
        p_data = p_data.filter(city=selected_city_1)

    # 獲取人口數據，將同一縣市的不同鄉鎮人口數相加
    population_data = p_data.values('city').annotate(total_population=Sum('quantity')).order_by('city')

    chart_data = data.values('category').annotate(
        quantity_1=Sum(Case(When(city=selected_city_1, then='quantity'), default=Value(0))),
        cleard_1=Sum(Case(When(city=selected_city_1, then='cleard'), default=Value(0))),
        quantity_2=Sum(Case(When(city=selected_city_2, then='quantity'), default=Value(0))),
        cleard_2=Sum(Case(When(city=selected_city_2, then='cleard'), default=Value(0))),
    )

    # 將縣市的人口數據合併到犯罪數據中
    for item in chart_data:
        item['population_1'] = 0  # 設定預設值
        item['population_2'] = 0  # 設定預設值
        city_data_1 = population_data.filter(city=selected_city_1)
        city_data_2 = population_data.filter(city=selected_city_2)
        if city_data_1.exists():
            item['population_1'] = city_data_1.values('total_population').first()['total_population']
        if city_data_2.exists():
            item['population_2'] = city_data_2.values('total_population').first()['total_population']

    # 計算犯罪率和破獲率
    for item in chart_data:
        population_1 = item['population_1']
        population_2 = item['population_2']
        if population_1 != 0 and item['quantity_1'] != 0:  # 確保人口數和犯罪數都不為零
            item['crime_rate_1'] = (item['quantity_1'] / population_1) * 100000  # 犯罪率 = (犯罪數 / 人口數) * 100
            item['clearance_rate_1'] = (item['cleard_1'] / item['quantity_1']) * 100  # 破獲率 = (破獲數 / 犯罪數) * 100
        else:
            item['crime_rate_1'] = 0
            item['clearance_rate_1'] = 0

        if population_2 != 0 and item['quantity_2'] != 0:  # 確保人口數和犯罪數都不為零
            item['crime_rate_2'] = (item['quantity_2'] / population_2) * 100000  # 犯罪率 = (犯罪數 / 人口數) * 100
            item['clearance_rate_2'] = (item['cleard_2'] / item['quantity_2']) * 100  # 破獲率 = (破獲數 / 犯罪數) * 100
        else:
            item['crime_rate_2'] = 0
            item['clearance_rate_2'] = 0

    return render(request, "compare.html", {'years': years, 'cities': cities, 'selected_year': selected_year, 'selected_city_1': selected_city_1, 'selected_city_2': selected_city_2, 'data': chart_data})


def news(request):
    data = models.news.objects.all()
    return render(request, "news.html", locals())

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
