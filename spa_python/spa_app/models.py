from django.db import models


class Table(models.Model):
    date = models.DateTimeField('Дата', auto_now=True, auto_now_add=False)
    name = models.CharField('Название', max_length=20)
    amount = models.FloatField('Количество', max_length=20)
    distance = models.FloatField('Расстояние', max_length=20)

    # def __str__(self):
    #     return(self.date)

