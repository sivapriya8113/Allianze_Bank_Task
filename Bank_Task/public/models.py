from django.db import models

# Create your models here.

class banks(models.Model):
    name = models.CharField(max_length=500)
    id = models.IntegerField(null=False,primary_key=True)


class branches(models.Model):
    ifsc = models.CharField(max_length=11,null=False,primary_key=True)
    bank_id =models.ForeignKey(banks, on_delete=models.CASCADE)
    branch = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=26)


class bank_branches(models.Model):
    ifsc = models.CharField(max_length=11)
    bank_id = models.ForeignKey(banks, on_delete=models.CASCADE)
    branch = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=26)
    bank_name = models.CharField(max_length=49)





