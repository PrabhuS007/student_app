from django.db import models

# Create your models here.
class student(models.Model):
    sname=models.CharField(max_length=20,blank=False,null=False)
    semail=models.EmailField()
    sage=models.IntegerField()
    sgender=models.CharField(max_length=20,blank=False,null=False)
    simage=models.ImageField(upload_to='pics',blank=True,null=True)
    def __str__(self):
        return self.sname