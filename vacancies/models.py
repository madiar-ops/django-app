from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    description = models.TextField()
    experience = models.CharField(
    max_length=50,
    choices=[
        ('entry', 'Entry Level'),
        ('mid', 'Mid Level'),
        ('senior', 'Senior Level')
    ],
    default='entry'  # ✅ Add this default value
)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Correct reference
