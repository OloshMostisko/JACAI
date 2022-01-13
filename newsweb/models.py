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

class ArticleType(models.Model):
    articleType = models.CharField(max_length=100, unique=True, default="")
    order = models.CharField(max_length=3, blank=False, default="", unique=True)
    slug = models.SlugField(default="", unique=True)


    class Meta:
        ordering = ["-order"]
        verbose_name = 'Article Type'
        verbose_name_plural = 'Article Types'

    def __str__(self):
        return self.title

    def get_absoulte_url(self):
        return reverse('articleType', kwargs={"pk": self.pk})
    
class ResearchInterest(models.Model):
    researchInterest = models.CharField(max_length=100, unique=True, default="")
    order = models.CharField(max_length=3, blank=False, default="", unique=True)
    slug = models.SlugField(default="", unique=True)


    class Meta:
        ordering = ["-order"]
        verbose_name = 'Research interest'
        verbose_name_plural = 'Research interests'

    def __str__(self):
        return self.title

    def get_absoulte_url(self):
        return reverse('research_Interest', kwargs={"pk": self.pk})

class Citation(models.Model):
    Google_Scholar_Link = models.CharField(max_length=300, default="")
    crossRef = models.CharField(max_length=300, default="")
    

    class Meta:
        verbose_name ="Citation"
        verbose_name_plural ="Citations"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Citation_detail", kwargs={"pk": self.pk})
 
class Issue(models.Model):
    issue_no =  models.IntegerField(default = 1)
    volume = models.ForeignKey(ArticleType, on_delete= models.SET_NULL, verbose_name ="Volume No", blank = False)
    class Meta:
        verbos = "Issue"
        verbose_name_ = "Issues"
        
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        reverse("Issue_detail", kwargs={"pk": self.pk})
   
    
class Volume (models.Model):
    volume_no =  models.IntegerField(default = 1)

    class Meta:
        verbose_name = "Volume "
        verbose_name_plural ="Volume s"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Volume _detail", kwargs={"pk": self.pk})
class Author(models.Model):
    author =  models.CharField(max_length=200, default="")
    weblink = models.CharField(max_length=200, default="")
    
    

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Author_detail", kwargs={"pk": self.pk})


class PublishedArticles (models.Model):
    title = models.CharField(max_length=200, default="")
    author = models.ManyToManyField(Author,verbose_name ="Authors", blank = False)
    abstract = RichTextField(blank=True, null=True, verbose_name='Publication List')
    article_Type = models.ForeignKey(ArticleType, on_delete= models.SET_NULL, verbose_name ="Article Type", blank = False)
    academicEditor = models.CharField(max_length=200, default="")
    volume_NO = models.ForeignKey(Volume, on_delete= models.SET_NULL, verbose_name ="Volume NO", blank = False)
    permissions = models.CharField(max_length=200, default="")
    researchInterest = models.ManyToManyField(ResearchInterest, blank=True, null=True)
    Received = models.DateTimeField(auto_now_add =True)
    Revised =  models.DateTimeField(blank = True)
    Accepted = models.DateTimeField( blank = True)
    Published = models.DateTimeField( blank = True)
    citations =  models.ForeignKey(Citation, on_delete= models.SET_NULL, verbose_name ="Citations", blank = False)
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