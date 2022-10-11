import uuid

from django.db import models

LOW = 'l'
MODERATE = 'm'
HIGH = 'h'
EXTREME = 'e'

STATUS_STRESS_LEVEL = (
    (LOW, 'Low'),
    (MODERATE, 'Moderate'),
    (HIGH, 'High'),
    (EXTREME, 'Extreme')
)

# Create your models here.
class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    names = models.CharField(max_length=250)
    surnames = models.CharField(max_length=250)
    age = models.IntegerField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    heartrate = models.IntegerField(blank=True, null=True, help_text="Frecuencia Cardiaca(Heart Rate) medida en BPM(Beats per minute)/Pulsaciones por minuto")
    bloodoxygensaturation = models.IntegerField(blank=True, null=True, help_text="Saturación de Oxígeno en Sangre")
    stresslevel = models.CharField(max_length=5, choices=STATUS_STRESS_LEVEL, default=LOW, help_text="Nivel de estrés")

    class Meta:
         db_table = 'person' # Le doy de nombre 'person' a nuestra tabla en la Base de Datos 