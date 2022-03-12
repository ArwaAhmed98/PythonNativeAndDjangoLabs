from django import  forms
from  .models import Student ,Track
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        # fields=('fname','lname','age','st_track')
        fields = '__all__'

class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        # fields=('fname','lname','age','st_track')
        fields = '__all__'
