from django.db import models

# Create your models here.
class Track(models.Model):
    track_name=models.CharField(max_length=20)
    def __str__(self):
        return self.track_name

class Student(models.Model):
    fname=models.CharField(max_length=20, null=True)
    lname=models.CharField(max_length=20, default='Ahmed')
    age=models.IntegerField()
# FK will be found in many side
    st_track =  models.ForeignKey(Track , on_delete=models.CASCADE)
    def __str__(self):
        return self.fname + ' ' + self.lname
    def is_adult(self):
        if self.age > 8 :
            return True
        else :
            return False
    is_adult.boolean = True
    is_adult.short_description = 'Graduated Student' #Esm el column el 25ir eli hyzher