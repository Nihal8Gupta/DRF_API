from django.db import models

# Create your models here.
class Employee(models.Model):
    Eid = models.IntegerField(primary_key=True)
    Ename = models.CharField(max_length=200)
    Eloc = models.CharField(max_length=200)
    Ejob = models.CharField(max_length=200)
    Esal = models.IntegerField()

    def __str__(self) -> str:
        return self.Ename
    
'''
{
"Eid":1,
"Ename":"Nihal",
"Eloc":"Bangalore",
"Ejob":"Python Full Stack",
"Esal":300000

}
'''