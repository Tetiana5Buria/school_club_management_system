import uuid
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.contrib.auth.models import User

# Валідатор для імен
validator = RegexValidator(
    regex=r'^[A-Za-zА-Яа-яіІїЇєЄґҐ\'\-]+$',
    message="Поле повинно містити лише літери."
)
inn_validator = RegexValidator(
    regex=r'^\d{10}$',
    message="ІПН повинен містити рівно 10 цифр."
)


min_age = 3
max_age = 129

class Student(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    student_id = models.CharField(
        "ІПН",
        max_length=10,
        unique=True,
        validators=[inn_validator],
        null=True

    )
    first_name = models.CharField("Ім'я", max_length=100, validators=[validator])
    last_name = models.CharField("Прізвище", max_length=100, validators=[validator])
    age = models.IntegerField("Вік", validators=[
        MinValueValidator(min_age, message=f"Вік не може бути меншим за {min_age} років."),
        MaxValueValidator(max_age, message=f"Вік не може перевищувати {max_age} років.")
    ])
    class_name = models.CharField("Номер класу", max_length=5)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Club(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField("Назва", max_length=100)
    description = models.TextField("Опис")

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Учень")
    club = models.ForeignKey(Club, on_delete=models.CASCADE, verbose_name="Гурток")
    date_joined = models.DateField("Дата приєднання", auto_now_add=True)


    class Meta:
        unique_together = ('student', 'club')
        verbose_name = "Реєстрація"
        verbose_name_plural = "Реєстрації"

    def __str__(self):
        return f"{self.student} -> {self.club}"