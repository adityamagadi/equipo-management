from django.db import models

class marks(models.Model):
	name=models.CharField(max_length=60)
	marks=models.IntegerField()

class guide_marks(models.Model):
	name1=models.CharField(max_length=60)
	name2=models.CharField(max_length=60)
	name3=models.CharField(max_length=60)
	name4=models.CharField(max_length=60)
        usn1=models.CharField(max_length=10)
	usn2=models.CharField(max_length=10)
	usn3=models.CharField(max_length=10)
	usn4=models.CharField(max_length=10)        
	
        projectname=models.CharField(max_length=60)
        marks1=models.IntegerField()
        marks2=models.IntegerField()
        marks3=models.IntegerField()
        marks4=models.IntegerField()
        
