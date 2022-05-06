from django.db import models
import datetime as dt

# Create your models here.
class Certificate(models.Model):
    sdate = dt.datetime.now()
    mydate = sdate.strftime('%d-%m-%Y')
    newdate = sdate.strptime(mydate, '%d-%m-%Y')

    register_number=models.CharField(max_length=20,primary_key=True)
    student_name=models.CharField(max_length=20)
    course=models.CharField(max_length=30)
    joined_date=models.DateTimeField(default=newdate)
    end_date=models.DateTimeField()
    exam_date=models.DateTimeField()
    Marks=models.IntegerField()
    Grade=models.CharField(max_length=10)

    def __str__(self):
        return f'{self.register_number}-{self.student_name}'





