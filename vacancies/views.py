from django.shortcuts import render, get_object_or_404
from .models import Vacancy  # Corrected import

def home(request):
    return render(request, "home.html")
def home(request):
    vacancies = Vacancy.objects.all()  # Получаем все вакансии
    return render(request, "home.html", {"vacancies": vacancies})  # Передаем вакансии в контекст


def post_list(request):
    vacancies = Vacancy.objects.all()
    return render(request, "post_list.html", {"vacancies": vacancies})

def vacancy_detail(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    # Your logic to render the vacancy detail
    return render(request, 'vacancy_detail.html', {'vacancy': vacancy})
# Create your views here.
