from django.db import models

# Create your models here.
class Video(models.Model):
	videoUpload = models.FileField(upload_to='videos//%Y/%m/%d')