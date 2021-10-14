from django.db import models

class Quotes(models.Model):
    id = models.BigAutoField(primary_key= True, unique=True, null=False)
    title = models.CharField(max_length=20,null=True)
    text = models.CharField(max_length=20,null=True)