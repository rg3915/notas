from django.db import models


class Grade(models.Model):
    name = models.CharField('nome', max_length=50)
    grade1 = models.DecimalField('A1', max_digits=3, decimal_places=1)
    grade2 = models.DecimalField('A2', max_digits=3, decimal_places=1)

    class Meta:
        ordering = ('name',)
        verbose_name = 'nota'
        verbose_name_plural = 'notas'

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            'pk': self.pk,
            'name': self.name,
            'grade1': self.grade1,
            'grade2': self.grade2,
        }
