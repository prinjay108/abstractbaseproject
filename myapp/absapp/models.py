from django.db import models
#********** abstract base clsss model ************

# Create your models here.
class Infodetails(models.Model):
    name=models.CharField(max_length=50)
    date=models.DateField()
    age=models.IntegerField()
    class Meta:
        abstract =True


class Student(Infodetails):
    fees=models.IntegerField()


class Teacher(Infodetails):
    salary=models.IntegerField()


class Contractor(Infodetails):
    payment=models.IntegerField()