from django.shortcuts import render

# Create your views here.
def index(request):
    """Meal planner app homepage."""
    return render(request, 'mealplanner_app/index.html')