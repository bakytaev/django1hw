from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.name} - {self.price}'


class Purchase(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    date_purchase = models.DateTimeField('purchase date')

    def __str__(self):
        return f'{self.name} - {self.age}'
