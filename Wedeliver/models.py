from django.db import models


# Create your models here.


class Contact (models.Model):
    sno = models.AutoField(primary_key=True)
    name1 = models.CharField(max_length=255)
    email1 = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    describe = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True , blank=True)



    def __str__(self):
        return "Massage From " + self.name1
    