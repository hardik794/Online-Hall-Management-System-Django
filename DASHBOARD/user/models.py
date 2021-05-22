from django.db import models

# Create your models here.

class History(models.Model):
    id=models.AutoField(primary_key=True)
    VanueUname=models.CharField(max_length=100)
    UserUname=models.CharField(max_length=100)
    VenueName=models.CharField(max_length=100,default="Nothing")
    Name=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    Number=models.CharField(max_length=100)
    Date=models.DateField()
    Time=models.CharField(max_length=100)
    Packege=models.CharField(max_length=100)
    Service = models.CharField(max_length=100)
    Status=models.CharField(max_length=10,default="Pending")

class Vanues(models.Model):
    VanueID = models.AutoField(primary_key=True)  # Field name made lowercase.
    VanueName = models.CharField(max_length=100)  # Field name made lowercase.
    VanueAddress = models.TextField()  # Field name made lowercase.
    Description = models.TextField()  # Field name made lowercase.
    Contact = models.CharField(max_length=10)  # Field name made lowercase.
    VanueType = models.CharField(max_length=30)  # Field name made lowercase.
    VanueBudget = models.CharField(max_length=30)  # Field name made lowercase.
    Image = models.ImageField(upload_to='pics')  # Field name made lowercase.
    PerDayRent = models.CharField(max_length=100)  # Field name made lowercase.
    PricePerDish = models.CharField(max_length=100)  # Field name made lowercase.
    MusicRent = models.CharField(max_length=100)  # Field name made lowercase.
    CateresRent = models.CharField(max_length=100)  # Field name made lowercase.
    DecoretionPrice = models.CharField(max_length=100)  # Field name made lowercase.
    ServiceRent = models.CharField(max_length=100)  # Field name made lowercase.
    # Status = models.CharField(max_length=30)  # Field name made lowercase.
    username = models.CharField(max_length=30)
