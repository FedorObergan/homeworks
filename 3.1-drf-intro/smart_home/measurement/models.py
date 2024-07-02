from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=70)


class Measurement(models.Model):
    sens = models.ForeignKey(Sensor, related_name='measurements', on_delete=models.CASCADE)
    temperature = models.DecimalField(null=False, max_digits=4, decimal_places=1)
    created_at = models.DateTimeField(auto_now=True)

