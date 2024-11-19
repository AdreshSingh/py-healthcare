from django.db import models

# Create your models here.
class FormModel(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    file=models.FileField(upload_to='uploads',blank=True,null=True)