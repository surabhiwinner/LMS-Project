from django.db import models

from courses.models import BaseClass

# Create your models here.

class AreaOfExpertise(BaseClass):

    area = models.CharField(max_length=30)

    def __str__(self):
        return self.area
    
    class Meta:

        verbose_name = 'Area of Expertise'

        verbose_name_plural = 'Area of Expertise'

class Instructors(BaseClass):

    profile = models.OneToOneField('authentication.Profile', on_delete=models.CASCADE)

    name = models.CharField(max_length=50)

    image = models.ImageField(upload_to='instructor-images/')

    description = models.TextField()

    area_of_expertise =models.ForeignKey('AreaOfExpertise', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
    
    class Meta:

        verbose_name = 'Instructors'

        verbose_name_plural = 'Instructors'