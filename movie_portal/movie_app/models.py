from django.db import models

# Create your models here.

class Cineprof(models.Model):

    """
    To store the details of the cine proffessionals
    """

    name = models.CharField(max_length=200)
    profile = models.TextField()
    dob = models.DateField()

    def __str__(self):
        return self.name

class Movie(models.Model):
    """
    To store information about movies
    """

    title = models.CharField(max_length=200)
    plot = models.TextField()
    cast = models.ManyToManyField(Cineprof, related_name="movie_cast")
    producer = models.ForeignKey(Cineprof, related_name="movie_producer", on_delete=models.CASCADE)
    director = models.ForeignKey(Cineprof, related_name="movie_director", on_delete=models.CASCADE)

class Moviereview(models.Model):

    """
    To store movie reviews
    """
    movie = models.ForeignKey(Movie, related_name="movie_review", on_delete=models.CASCADE)
    review = models.TextField()