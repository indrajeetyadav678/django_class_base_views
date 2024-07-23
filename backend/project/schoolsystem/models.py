from django.db import models

# Create your models here.


class Departmentmodel(models.Model):
    dep_id = models.CharField(max_length=250)
    dep_name = models.CharField(max_length=250)
    def __str__(self):
        return self.dep_name
    
    class Meta:
        db_table="Department"
        # app_label = 'schoolstystem'



class Studentmodel(models.Model):
    name=models.CharField(max_length=255)
    father_name=models.CharField(max_length=255)
    classes =models.CharField(max_length=255)
    fees = models.IntegerField()
    dep_name=models.ForeignKey(Departmentmodel, on_delete=models.CASCADE, related_name='dep_names', db_constraint=False, null=True)
    def __str__(self):
        return self.name
    
    class Meta:
        db_table='student'
        # app_label = 'schoolstystem'
    

