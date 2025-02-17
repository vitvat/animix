from django.db import models
from django.core.exceptions import ValidationError


class Gen(models.Model):
    TYPE_CHOICES = [
        ('gold', 'Gold'),
        ('water', 'Water'),
        ('air', 'Air'),
        ('universal', 'Universal'),
    ]

    name = models.CharField(max_length=25)
    rank = models.IntegerField(choices=[(i, i) for i in range(2, 8)])
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    mother_only = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']

class Creature(models.Model):
    TYPE_CHOICES = [
        ('gold', 'Gold'),
        ('water', 'Water'),
        ('air', 'Air'),
        ('universal', 'Universal'),
    ]

    name = models.CharField(max_length=25)
    father = models.ForeignKey(Gen, on_delete=models.CASCADE, related_name='creature_father')
    mother = models.ForeignKey(Gen, on_delete=models.CASCADE, related_name='creature_mother')
    rank = models.IntegerField(choices=[(i, i) for i in range(2,11)])
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def clean(self):
        if self.father == self.mother:
            raise ValidationError('Father and mother cannot be the same Gen.')
        if self.mother.father_only:
            raise ValidationError('This Gen can only be a father.')

    def __str__(self):
        # Метод для отображения объекта в виде строки, возвращает название
        return self.name

    class Meta:
        ordering = ['id']  # Упорядочить записи по возрастанию id
