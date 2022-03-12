from re import T
from django.contrib import admin
from .models import Student, Track
# Register your models here.


class CustomStudent(admin.ModelAdmin):
    fieldsets = (
        ['Student Information' , {'fields':['fname' ,'lname' , 'age']}] ,
        ['Scholarship info' , {'fields' : ['st_track']}]
    #     awl element fel list byb2a shayel label bta3
    )
    list_display = ('fname','lname','age','st_track','is_adult') # keda hy3rd eli fields eli gwa el object
    # men 8ero hyb2a esm col student
    search_fields = ('fname','lname' ,'st_track__track_name')
    list_filter = ('age','st_track__track_name')
class InlineStudent(admin.StackedInline):

#     eli byn-heirt men el stackInline da byb2a ynf3 y3mlo inject
    model = Student
    extra = 1
# bydefault 3  ,, Form htkrr kam mra
class CustomTrack(admin.ModelAdmin):
    inlines = [InlineStudent]

######################################
admin.site.register(Student , CustomStudent)
admin.site.register(Track , CustomTrack)