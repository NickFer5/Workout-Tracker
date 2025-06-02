# Workout-Tracker
Simple django web app that serves as a workout tracker. Contains fields for exercise name, sets, reps, and total time spent during the exercise.
## Functionality
Log Workouts - Records Exercise Name, Sets, Reps, and Total Duration.
History - Workouts are displayed in a reverse order with the most recent being at the top.
Calculated Fields - Total Reps provides the product of the sets and reps for a given workout. Total Duration gives the sum of all the workout durations.

### Built using Python 3.13, Django 5.2.1, and SQlite(Django default)

### Reproductibility Instructions
1. Clone the Git Repository: git clone https://github.com/NickFer5/Workout-Tracker.git
2. Make sure you are in the main project directory(fitness_tracker)
3. Enter virtual environment: python -m venv (venv_name)
4. Activate by following this path: (venv_name)\Scripts\activate
5. Make your migrations so the migration files will be created
6. Migrate to your DB using the migration plan
7. Run the Web App: python manage.py runserver
8. Ctrl + Click Local Address or Copy Paste into a browser
