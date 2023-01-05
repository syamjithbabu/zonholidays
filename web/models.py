from django.db import models
from versatileimagefield.fields import VersatileImageField

# Create your models here.

class Blog(models.Model):
    blog_type = models.CharField(max_length=100)
    blog_image = VersatileImageField('Blog Image',upload_to = 'image/testimagemodel/')
    blogger_name = models.CharField(max_length=100)
    blog_date = models.DateField()
    blog_title = models.CharField(max_length=200)
    blog_content = models.TextField()

    def __str__(self):
        return str(self.blogger_name)

class Place(models.Model):
    place_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.place_name)

class Gallery(models.Model):
    image = VersatileImageField('Image',upload_to = 'image/testimagemodel/')
    place = models.ForeignKey(Place,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return str(self.place)

class Service(models.Model):
    service_image = VersatileImageField('Image',upload_to = 'image/testimagemodel/')
    service_name = models.CharField(max_length=100)
    service_details = models.TextField()

    def __str__(self):
        return str(self.service_name)

class Testimonial(models.Model):
    image = VersatileImageField('Image',upload_to = 'image/testimagemodel/')
    review = models.TextField()
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

class TourType(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return str(self.type)

class Package(models.Model):
    place_name = models.CharField(max_length = 100)
    tour_type = models.ForeignKey(TourType,on_delete=models.CASCADE,null=True)
    package_details = models.TextField()
    image_1 = VersatileImageField('Image1',upload_to = 'image/testimagemodel/')
    image_2 = VersatileImageField('Image2',upload_to = 'image/testimagemodel/')
    image_3 = VersatileImageField('Image3',upload_to = 'image/testimagemodel/')
    image_4 = VersatileImageField('Image4',upload_to = 'image/testimagemodel/')
    image_5 = VersatileImageField('Image5',upload_to = 'image/testimagemodel/')
    image_6 = VersatileImageField('Image6',upload_to = 'image/testimagemodel/')
    total_days = models.CharField(max_length = 100)
    group_size = models.CharField(max_length=100)
    number_of_days = models.IntegerField()
    number_of_nights = models.IntegerField()
    rate = models.CharField(max_length=100)

    def __str__(self):
        return str(self.place_name)