from django.db import models

# Create your models here.
GENDER_CHOICES=[ ('M', 'Male'), ('F','Female'),]
   


class Student(models.Model):
    name= models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    roll= models.IntegerField(unique=True)
    grade= models.IntegerField()
    email=models.EmailField(max_length=150)
    gender= models.CharField(choices=GENDER_CHOICES,max_length=6, null=True, default='Male')
    add_date= models.DateField(auto_now_add=True, null=True)
    dob= models.DateField("Date of Birth(mm/dd/yyyy)",null= True, auto_now_add=False, auto_now=False)
    pic= models.ImageField(upload_to= 'images/', null=True)
    
    
    def __str__(self):
        return self.name 
    
    