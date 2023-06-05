from django.db import models

class cityData(models.Model):
    city_id = models.IntegerField(primary_key=True)
    city = models.CharField(max_length=100)
    class Meta:
        ordering = ('city_id',)
    def __str__(self):
        return self.city

class populationData(models.Model):
    population_id = models.IntegerField(primary_key=True)
    year = models.IntegerField(default=0)
    city = models.CharField(max_length=100)
    # .ForeignKey(cityData, on_delete=models.CASCADE)
    dist = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    class Meta:
        ordering = ('-year',)
    def __str__(self):
        return self.city
    

class categoryData(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=100)
    class Meta:
        ordering = ('category_id',)
    def __str__(self):
        return self.category
    
class crimeData(models.Model):
    crime_id = models.IntegerField(primary_key=True)
    year = models.IntegerField(default=0)
    month = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    # ForeignKey(cityData, on_delete=models.CASCADE)
    category =  models.CharField(max_length=100)
    # ForeignKey(categoryData, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    cleard = models.IntegerField(default=0)
    class Meta:
        ordering = ('year',)
    def __str__(self):
        return self.city