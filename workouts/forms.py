from django import forms
from .models import Workout

#creates form that is tied to the workout db model so user input can be captured
class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['exercise_name', 'sets', 'reps', 'duration_minutes']
