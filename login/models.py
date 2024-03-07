from django.db import models



class Regi(models.Model):
  name=models.CharField(max_length=255)
  addres=models.CharField(max_length=255)
  gender=models.CharField(max_length=255)
  skills=models.CharField(max_length=255,default="")
  email=models.EmailField(max_length=254)
  password=models.CharField(max_length=50)
  
class State(models.Model):
  id=models.AutoField(primary_key=True)
  state=models.CharField(max_length=255)
  
class District(models.Model):
  id=models.AutoField(primary_key=True)
  district=models.CharField(max_length=255)
  state=models.ForeignKey(State,on_delete=models.CASCADE)