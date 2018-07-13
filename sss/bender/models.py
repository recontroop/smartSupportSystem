from django.db import models

class Data(models.Model):
	data_id = models.AutoField(primary_key=True)
	problem_keywords = models.CharField(max_length=4096)
	solution = models.CharField(max_length=2048)