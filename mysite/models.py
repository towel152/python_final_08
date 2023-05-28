from django.db import models

class populationData(models.Model):
    population_id = models.IntegerField(primary_key=True)
    year = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    Dist = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    class Meta:
        ordering = ('-year',)
    def __str__(self):
        return self.population_id
    
# class populationData(models.Model):
#     year = models.CharField(max_length=100)
#     city = models.CharField(max_length=100)
#     category = models.CharField(max_length=100)
#     quantity = models.IntegerField(default=0)
#     cleared = models.IntegerField(default=0)
#     class Meta:
#         ordering = ('-sbi',)
#     def __str__(self):
#         return self.sna