from django.db import models

# Create your models here.

class UserHistory(models.Model):
    VanueUname = models.CharField(db_column='VanueUname', max_length=100)  # Field name made lowercase.
    UserUname = models.CharField(db_column='UserUname', max_length=100)  # Field name made lowercase.
    Name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    Email = models.CharField(db_column='Email', max_length=100)  # Field name made lowercase.
    Number = models.CharField(db_column='Number', max_length=100)  # Field name made lowercase.
    Date = models.DateField(db_column='Date')  # Field name made lowercase.
    Time = models.CharField(db_column='Time', max_length=100)  # Field name made lowercase.
    Packege = models.CharField(db_column='Packege', max_length=100)  # Field name made lowercase.
    Service = models.CharField(db_column='Service', max_length=100)  # Field name made lowercase.
    Status = models.CharField(db_column='Status', max_length=10)  # Field name made lowercase.
    VenueName = models.CharField(db_column='VenueName', max_length=100 ,default='Nothing')  # Field name made lowercase.

    class Meta:
        db_table = 'user_history'