from django.db import models

# Create your models here.


class WhoAreYou(models.Model):
    Who_are_you= models.CharField(max_length=100)
    greeting = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    profile = models.ImageField(upload_to='details/admin_details')
    # resume =  models.ImageField(upload_to='details/admin_details')
    
    
class socialMedia(models.Model):
    facebook_url = models.URLField(null=True, blank=True)
    twitter_url = models.URLField(null=True, blank=True)
    linkedin_url = models.URLField(null=True, blank=True)
    skype_url = models.URLField(null=True, blank=True)
    github_url = models.URLField(null=True, blank=True)  
    
    
    
    
    
    
class AboutMe(models.Model):
    title= models.CharField(max_length=100)
    about= models.TextField(max_length=200)
    asmpe =  models.FileField(upload_to='details/pdfs/')
    # profile= models.ImageField(upload_to='details/admin_details')
    


    