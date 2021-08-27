from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Tree(models.Model):
    LEVEL_CHOICES = (
        (1, 'Rookie'),
        (2, 'Medium'),
        (2, 'Expert'),
    )

    TYPE_CHOICES = (
        (1, 'Musical video'),
        (2, 'Movie'),
        (3, 'TV show'),
        (4, 'Other'),
    )

    title = models.CharField(max_length=100)
    url = models.URLField(max_length=100, blank=True, null=True)
    content = models.TextField()
    level = models.IntegerField(default=1, choices=LEVEL_CHOICES,
                                validators=[MinValueValidator(1), MaxValueValidator(3),])
    type = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)], choices=TYPE_CHOICES)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'trees_trees'
