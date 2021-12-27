from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files import File


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

def compress(image):
    im = Image.open(image)
    # create a BytesIO object
    im_io = BytesIO() 
    # save image to BytesIO object
    im.save(im_io, 'JPEG', quality=50) 
    # create a django-friendly Files object
    new_image = File(im_io, name=image.name)
    return new_image
   
class PublishedArticles (models.Model):
    title = models.CharField(max_length=200, default="")
    author = models.CharField(max_length=200,default="",editable=False)
    abstract = RichTextField(blank=True, null=True, verbose_name='Publication List')
    publish_on = models.DateTimeField( blank = False)
    updated_on = models.DateTimeField(auto_now = True)
    created_on = models.DateTimeField(auto_now_add =True)
    status = models.IntegerField(choices=STATUS, default = 1)
    total_views=models.IntegerField(default=0)
    class Meta:
        ordering = []
        verbose_name = 'Published Article'
        verbose_name_plural = 'Published Articles'

    def __str__(self):
        return self.note