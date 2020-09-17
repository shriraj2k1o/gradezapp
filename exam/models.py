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

    def __str__(self):
        return self.year+' - '+ self.subject +' - '+self.question
    

class Test(models.Model):
    NAME = (
        ('ISE I', 'ISE I'),
        ('ISE II', 'ISE II'),
        ('ISE III', 'ISE III'),
        ('ISE IV', 'ISE IV'),
        ('ISE V', 'ISE V'),
    )

    FLAGS = (
        ('T', 'T'),
        ('F', 'F'),
        ('D', 'D'),
    )

    test_name = models.CharField(max_length=10, choices=NAME)
    test_created = models.DateTimeField(auto_now=True,verbose_name="Test Created on")
    test_date = models.DateTimeField(verbose_name="Test Date")
    test_conducted = models.CharField(max_length=1, choices=FLAGS, default='F')
    test_duration = models.IntegerField(verbose_name="Test Duration in hrs", default=1)
    test_marks = models.IntegerField(default=10)

    test_question = models.ForeignKey(QuestionBank, on_delete=models.CASCADE)

    # class Meta:
    #     managed = False
    #     db_table = 'test'

    # def test_question(self):
    #         return QuestionBank.question