from django.contrib import admin
from mysite import models                   #從mysite資料夾底下匯入models.py裡面所有的類別
admin.site.register(models.populationData)
