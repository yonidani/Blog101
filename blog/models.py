
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date, date
from ckeditor.fields import RichTextField
class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    #body = models.TextField()
    post_date = models.DateField(auto_now_add=True)

    #content = models.TextField()
    #pub_date = models.DateTimeField('date published')


    def __str__(self):
        return self.title + '|' + str(self.author)
    def get_absolute_url(self):
        #return reverse('article_detail', args=(str(self.id)))
        return reverse('home')
        # Create your models here.
