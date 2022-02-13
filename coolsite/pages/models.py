from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=150, verbose_name="Имя")
    rate = models.IntegerField(verbose_name="Рейтинг")
    year = models.IntegerField(verbose_name="Стаж")
    salary = models.IntegerField(verbose_name="Ставка")
    place = models.ForeignKey("Place", on_delete=models.PROTECT, null=True, verbose_name="Место занятий (id)")
    subject = models.ForeignKey("Subject", on_delete=models.PROTECT, null=True, verbose_name="Предмет (id)")

    def __str__(self):
        return f"({self.id}) {self.name}"

    class Meta:
        verbose_name = "Учитель"
        verbose_name_plural = "Учителя"


class Subject(models.Model):
    title = models.CharField(max_length=150, verbose_name="Предмет", db_index=True)

    def __str__(self):
        return f"({self.id}) {self.title}"

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"


class Place(models.Model):
    title = models.CharField(max_length=150, verbose_name="Место занятий", db_index=True)

    def __str__(self):
        return f"({self.id}) {self.title}"

    class Meta:
        verbose_name = "Место занятий"
        verbose_name_plural = "Места занятий"