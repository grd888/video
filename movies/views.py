from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
  context = {
    'movies': ['Gladiator', 'Inception', 'Interstellar'],
  }
  return render(request, 'movies/index.html', context)

def about(request):
  return render(request, 'movies/about.html', {})