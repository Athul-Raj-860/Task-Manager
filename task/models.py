from django.db import models

class Task(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Status = models.CharField(max_length=255)
    TaskAssignedDate = models.DateField()
    TaskCompleteDate =models.DateField()

    class Meta:
        db_table="DB_Tasks"
# Create your models here.
