from django.db import models

class Airport(models.Model):
    code = models.CharField(max_length=10, unique=True)
    
    def __str__(self):
        return self.code

class FlightRoute(models.Model):
    DIRECTION_CHOICES = (
        ('LEFT', 'Left'),
        ('RIGHT', 'Right'),
    )

    # The starting point
    source = models.ForeignKey(Airport, related_name='routes_out', on_delete=models.CASCADE)

    destination = models.ForeignKey(Airport, related_name='routes_in', on_delete=models.CASCADE)
    
    direction = models.CharField(max_length=5, choices=DIRECTION_CHOICES)
    distance_km = models.IntegerField(help_text="Distance in KM")
    duration_mins = models.IntegerField(help_text="Duration in Minutes")

    def __str__(self):
        return f"{self.source} -> {self.destination} ({self.direction})"