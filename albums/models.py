from django.db import models
from django.core.validators import RegexValidator
from django.db.models.fields import DateTimeField

# Create your models here.
class Album(models.Model):
    year_regex = RegexValidator(
        regex=r'^\d{4}$',
        message="Album year must be entered in the format: 'XXXX'.")

    title = models.CharField(max_length=255, null=True, blank=True)
    artist = models.CharField(max_length=255)
    year_released = models.CharField(max_length=4,
                                    validators=[year_regex],
                                    null=True,
                                    blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"