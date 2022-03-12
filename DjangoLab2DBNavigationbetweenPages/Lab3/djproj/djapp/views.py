from django.shortcuts import render , HttpResponse
from django.shortcuts import redirect
from .models import Student,Track
# Create your views here.
def home(request):
    # return HttpResponse('Hello frm cloud function')
    students = Student.objects.all()
    context = {'all_stds': students} #we can render many var keyAndValue
    return  render(request,'djapp/home.html',context)
def show(request,st_id):
    # st=Student.objects.all()[0]
    st = Student.objects.get(id = st_id)
    # fname=st.fname
    context = {'st':st}
    # return HttpResponse("this is go func")
    # return HttpResponse(fname)
    return render(request,'djapp/show.html',context)
def stDEL(request,st_id):
    st=Student.objects.get(id = st_id)
    st.delete()
    return redirect('home') #bta5od url link tro7 redirect 3leh