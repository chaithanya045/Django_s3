from distutils.command import upload
from django.db import models
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your models here.
class BlogPost(models.Model):
    title=models.CharField(max_length=255)
    body=models.TextField()
    image=models.FileField(upload_to='Blog_images/')

    def __str__(self):
        return self.title
#   def delete(request, id): 
#        post = post.objects.filter(pk=id).delete()
#       return HttpResponseRedirect(reverse('posts.views.all_posts'))
    def delete(self):
        self.image.delete(save=False)
        super().delete()
        


    