from django.db import models

# Create your models here.

class Users(models.Model):

    PROFESSION = (
        ('S', 'Student'),
        ('P', 'Professor'),
        ('A', 'Admin'),
    )

    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=500)
    password = models.CharField(max_length=500)
    profession = models.CharField(max_length=1, choices=PROFESSION)
    acc_status = models.BooleanField()
    id_card = models.FileField()

    def __str__(self):
        return self.name + ' is a `' + self.profession + '` with email '+ self.email
    