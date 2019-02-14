from django.db import models
from django.utils.text import slugify


class categories(models.Model):
    name = models.CharField(max_length=120)
    image = models.FileField(null=True,blank=True)
    slug = models.SlugField(unique=True,editable=False,max_length=200)

    def __str__(self):
        return self.name

    def get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        counter = 1

        while categories.objects.filter(slug=unique_slug).exists():
            unique_slug = slug + "_" + str(counter)
            counter += 1

        return unique_slug

    def save(self,*args,**kwargs):
        self.slug = self.get_unique_slug()

        return super(categories,self).save(*args,**kwargs)
