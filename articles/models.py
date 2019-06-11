from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Articles(models.Model):
	title= models.CharField(max_length=100)
	slug= models.SlugField()
	body=models.TextField()
	date=models.DateTimeField(auto_now_add=True)
	thumb=models.ImageField(upload_to='images/',default = 'images/default.png',blank=True)
	author = models.ForeignKey(User,default=None,on_delete=models.PROTECT)
	pdf = models.FileField(upload_to='documents/',default='documents/DbConnect.java',blank=True)
	def __str__(self):
		return self.title

	def snippet(self):
		return self.body[:50] + "..."

	def delete(self,*args,**kwargs):
		self.pdf.delete()
		self.thumb.delete()
		super().delete(*args,**kwargs)
	
