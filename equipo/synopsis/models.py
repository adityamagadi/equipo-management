from django.db import models

class Synopsis(models.Model):
	synfile=models.FileField(upload_to='synopsis/%Y/%m/%d')
