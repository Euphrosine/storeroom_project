from django.db import models

class CropsData(models.Model):
    timestamp = models.DateTimeField()
    temperature = models.FloatField(null=True)
    humidity = models.FloatField(null=True)
    co2 = models.FloatField(null=True)
    ldr = models.FloatField(null=True)



    def __str__(self):
        return f"{self.timestamp} - {self.temperature} - {self.humidity} - {self.co2} - {self.ldr}"
