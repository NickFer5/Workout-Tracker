from django.db import models

class Workout(models.Model):
    exercise_name = models.CharField(max_length=100)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    duration_minutes = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    def total_reps(self):
        return self.sets * self.reps

    def __str__(self):
        return f"{self.exercise_name} - {self.date}"

