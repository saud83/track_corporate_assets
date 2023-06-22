from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Device(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='devices')
    name = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Log(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='logs')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='logs')
    check_out_date = models.DateTimeField()
    return_date = models.DateTimeField()

    def __str__(self):
        return f"{self.device} - {self.employee}"