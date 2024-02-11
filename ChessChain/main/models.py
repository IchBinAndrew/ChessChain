from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS_TYPES = (
    ('custom', 'Пользовательская'),
    ('lesson', 'Урок')
)
class Room(models.Model):
    title = models.CharField(max_length=50)
    creation_time = models.DateTimeField(auto_now=True)
    max_amount_of_members = models.IntegerField()
    private = models.BooleanField()
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    status = models.CharField(verbose_name='Статус', max_length=6, choices=STATUS_TYPES)
    def __str__(self):
        return self.title