from django.db import models

class Lecture(models.Model):
    link = models.URLField()
    date = models.DateField(default='2023-01-01')
    start_time = models.TimeField(default='09:00')
    end_time = models.TimeField(default='10:00')

    def __str__(self):
        return f"Lecture on {self.date} from {self.start_time} to {self.end_time}"

