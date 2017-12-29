from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.db.models import permalink
from markdown import markdown
from django.utils import timezone
VIEWABLE_STATUS=[3,4]


class ViewableManager(models.Manager):
    def ge_query_set(self):
        default_queryset = super(ViewableManager,self).get_queryset()
        return default_queryset.filter(status__in = VIEWABLE_STATUS)


class Story(models.Model):
    STATUS_CHOICES= (
        (1,"Need Edit"),
        (2,"Need Approval"),
        (3,"Published"),
        (4,"Archived"),
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    category = models.ForeignKey("Category")
    makedown_content = models.TextField()
    html_content = models.TextField(editable=False)
    owner = models.ForeignKey(User)
    status = models.IntegerField(choices=STATUS_CHOICES,default=1)
    created = models.DateTimeField(auto_now_add=True)
    modified= models.DateTimeField(auto_now=True)
    class Meta:
        ordering =['modified']
        verbose_name_plural= '新闻故事'
    admin_objects = models.Manager()
    objects = ViewableManager()

    def save(self,*args,**kwargs):
        self.html_content = markdown(self.makedown_content)
        self.modified= timezone.now()
        super(Story,self).save(*args,**kwargs)

    @permalink
    def get_absolute_url(self):
        return ('cms-story',None,{'slug':self.slug})

    def __str__(self):
        return self.title


class Category(models.Model):
    label = models.CharField(max_length=64)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural="分类"

    def __str__(self):
        return self.label
