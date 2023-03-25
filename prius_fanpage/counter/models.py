from django.db import models
from multiselectfield import MultiSelectField
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
# class TimeChoice(models.Model):
#     pass
    # time_choice = models.IntegerField()
    # number = # have to figure out witch field to choose
    # color

    # def __str__(self):
    #     return self.title


COLORS_CHOICES = (
    ('white', ("White")),
    ('silver', ('Silver')),
    ('red', ('Red')),
    ('pearl', ('Pearl')),
    ('gray', ('Gray')),
    ('black', ('Black')),
    ('pine', ('Pine Mica')),
    ('seaside', ('Seaside Pearl')),
)
class ColorFive(models.Model):
    color = MultiSelectField(choices=COLORS_CHOICES,
                             max_choices=8,
                             default=1,
                             validators=[
                                 MaxValueValidator(100),
                                 MinValueValidator(1)
                             ]
                             )

class ColorTen(models.Model):
    color = MultiSelectField(choices=COLORS_CHOICES,
                             max_choices=8,
                             default=1,
                             validators=[
                                 MaxValueValidator(100),
                                 MinValueValidator(1)
                             ]
                             )