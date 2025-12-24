from django.db import models
from doctors.models import Doctor
# Create your models here.
class Listing(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    district = models.CharField(max_length=50)
    description= models.TextField(blank=True)
    services = models.TextField(blank=True)
    service = models.IntegerField()
    room_type = models.CharField(max_length=200, default='')
    rooms= models.CharField(max_length=2)
    professions = models.CharField(max_length=200, default='')
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-list_date']
        indexes = [models.Index(fields=['list_date'])]
    def __str__(self):
        return self.title