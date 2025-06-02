from django.shortcuts import render, redirect
from .models import Workout
from .forms import WorkoutForm

#handles form submission, retrieves the workouts, and sends the data to the html template
def workout_log(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('workout-log')
    else:
        form = WorkoutForm()
    #calculated fields
    workouts = Workout.objects.all().order_by('-date')
    total_reps = sum(w.sets * w.reps for w in workouts)
    total_duration = sum(w.duration_minutes or 0 for w in workouts)
    #sends data to html template
    return render(request, 'workouts/log.html', {
        'form': form,
        'workouts': workouts,
        'total_reps': total_reps,
        'total_duration': total_duration
    })
