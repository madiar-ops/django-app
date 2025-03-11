from django.shortcuts import render, get_object_or_404
from .models import Vacancy  # Corrected import

def home(request):
    return render(request, "home.html")

def post_list(request):
    vacancies = Vacancy.objects.all()
    return render(request, "post_list.html", {"vacancies": vacancies})

def vacancy_detail(request, id):
    vacancy = get_object_or_404(Vacancy, id=id)
    return render(request, "vacancies/vacancy_detail.html", {"vacancy": vacancy})
# Create your views here.
