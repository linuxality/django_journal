from django.db import models

# Create your models here.
# Step 5: Import the User model
from django.contrib.auth.models import User

# Create your models here.
# Step 5: Includes the ForeignKey(User), ImageField & DateField
class Event(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    eventdate = models.DateField(blank=True, null=True)
    rating = models.DecimalField(max_digits=10, decimal_places=3)
    image = models.ImageField(upload_to='uploads')

    def __str__(self):
        return self.title
