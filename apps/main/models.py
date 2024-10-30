from django.db import models

# Create your models here.
class My_student(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='имя'
    )
    surname = models.CharField(
        max_length=255,
        verbose_name='фамилия'
    )
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Cтуденты'
        