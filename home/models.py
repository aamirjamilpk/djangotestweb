from django.db import models

# Create your models here.

class Information(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    nic = models.CharField(max_length=13, null=True, blank=True)
    phoneNumber = models.CharField(max_length=13, null=True, blank=True)

    class Meta :
        verbose_name_plural = 'Info'

    def __str__(self):
        return '{0}| {1}'.format(self.name,self.age)


