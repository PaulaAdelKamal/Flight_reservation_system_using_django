from django.db import models

AIRCRAFT_TYPES = [('Boeing', 'Boeing'),
                  ('Airbus', 'Airbus'),
                  ('Bombardier', 'Bombardier'),
                  ('Embraer', 'Embraer'),
                  ('ATR', 'ATR')
                  ]


class AddAirCraft(models.Model):
    name = models.CharField(max_length=100, default='Enter the name')
    type = models.CharField(
        max_length=10,
        choices=AIRCRAFT_TYPES,
    )
    number_of_sets = models.DecimalField(default=100, max_digits=3, decimal_places=0)

    def __str__(self):
        return self.name

# Create your models here.
