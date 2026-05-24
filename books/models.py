from django.db import models

# Create your models here.
class book(models.Model):
    movie = models.CharField(max_length=20)
    director = models.CharField(max_length=30)
    duration = models.FloatField()
    status = models.BooleanField()

    def __str__(self):
        return f'{self.title} -by {self.author} with {self.pages} pages {self.status}'
    



class Note(models.Model):

    title = models.CharField(
        max_length=100
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        return self.title