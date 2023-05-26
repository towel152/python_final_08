from django.db import models

class happenData(models.Model):
    city = models.CharField(max_length=100)
    mouth = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    number = models.IntegerField(default=0)
    class Meta:
        ordering = ('-sbi',)
    def __str__(self):
        return self.sna