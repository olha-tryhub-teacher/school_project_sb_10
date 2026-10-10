from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Ім'я")
    last_name = models.CharField(max_length=50, verbose_name="Прізвище")
    class_name = models.CharField(max_length=10, verbose_name="Клас")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Teacher(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Ім'я")
    last_name = models.CharField(max_length=50, verbose_name="Прізвище")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Subject(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва предмета")
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        verbose_name="Вчитель"
    )

    def __str__(self):
        return self.name


class Grade(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        verbose_name="Учень"
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        verbose_name="Предмет"
    )
    value = models.PositiveIntegerField(verbose_name="Оцінка")
    date = models.DateField(auto_now_add=True, verbose_name="Дата")

    def __str__(self):
        return f"{self.student} — {self.subject}: {self.value}"