from django.db import models

# Create your models here.
class Profile(models.Model):
	picture=models.ImageField(upload_to='imgfolder')
