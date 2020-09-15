from django.db import models

# Create your models here.
class QuestionBank(models.Model):
    YEAR = (
       
        ('BE', 'BE'),
    )

    SUBJECT = (
        ('SMQA', 'Software Metrics and Quality Assurance'),
        ('CD', 'Compiler Design'),
        ('ES', 'Embedded System'),
    )

    UNIT = (
        ('1', 'I'),
        ('2', 'II'),
        ('3', 'III'),
        ('4', 'IV'),
        ('5', 'V'),
    )



    question = models.CharField(max_length=1000)
    
    
    subject = models.CharField(max_length=4, choices=SUBJECT)
    year = models.CharField(max_length=2, choices=YEAR)
    unit = models.CharField(max_length=4, choices=UNIT)
    
   

    # def __str__(self):
    #     return self.name + ' is a `' + self.profession + '` with email '+ self.email