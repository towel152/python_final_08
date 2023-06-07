from django.db import models

class cityData(models.Model):
    # city_id = models.IntegerField(primary_key=True)
    city = models.CharField(primary_key=True, max_length=100)
    class Meta:
        ordering = ('city',)
    def __str__(self):
        return self.city

class populationData(models.Model):
    population_id = models.IntegerField(primary_key=True)
    year = models.IntegerField(default=0)
    city = models.ForeignKey(cityData, on_delete=models.CASCADE)
    dist = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    class Meta:
        ordering = ('-year',)
    def __str__(self):
        return str(self.city)
    

class categoryData(models.Model):
    # category_id = models.IntegerField(primary_key=True)
    category = models.CharField(primary_key=True, max_length=100)
    class Meta:
        ordering = ('category',)
    def __str__(self):
        return self.category
    
class crimeData(models.Model):
    crime_id = models.IntegerField(primary_key=True)
    year = models.IntegerField(default=0)
    month = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    # ForeignKey(cityData, on_delete=models.CASCADE)
    category =  models.ForeignKey(categoryData, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    cleard = models.IntegerField(default=0)
    class Meta:
        ordering = ('year',)
    def __str__(self):
        return self.city
    
class news(models.Model):
    title = models.CharField(max_length=200)
    # sbi = models.IntegerField(default=0)
    # tot = models.IntegerField(default=0)
    def __str__(self):
        return self.title