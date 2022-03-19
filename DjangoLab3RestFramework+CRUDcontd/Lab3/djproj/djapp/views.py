from django.shortcuts import render , HttpResponse
from django.shortcuts import redirect
from .models import Student,Track
from .forms import StudentForm
from .serializers import StudentSerializer
#rest apis imports
from rest_framework.decorators import api_view
from rest_framework.response import Response # for retruning rest reponse

#REST  APIS VIEWS HERE!
@api_view(['GET']) # use decorator for telling interpter that it is not http response  # post and get and del only allowed method
def api_students_all(request):
    student =  Student.objects.all() # select * from student
    st_ser = StudentSerializer(student,many=True) # hal el data de btrg3 lsit of objects wala object wa7ed bs?
    return Response(st_ser.data)
@api_view(['GET'])
def api_students_show(request,st_id):
    st= Student.objects.get(id=st_id)
    st_ser = StudentSerializer(st, many=False)
    return  Response(st_ser.data) #return rest reponse not http
@api_view(['POST'])
def api_students_add(request):
    st_ser=StudentSerializer(data=request.data)
    if st_ser.is_valid():
        st_ser.save()
        return redirect('api-all')
@api_view(['POST'])
def api_students_edit(request,st_id):
    st = Student.objects.get(id=st_id)
    st_ser = StudentSerializer(data=request.data,instance=st)
    if st_ser.is_valid():
        st_ser.save()
        return redirect('api-all')
@api_view(['DELETE']) #del method cannot be used with redirect
def api_students_del(request ,st_id):
    st=Student.objects.all()
    st.delete()
    return Response('Student deleted successfully')







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
def stAdd(request):
    form = StudentForm()
    if(request.method=='POST'):
    #     check the user submit an input data in the form -- USR click save
        form=StudentForm(request.POST)
    #     mtm3l4 create L form fdya , e3mlha bel data el user 3mlha submit
        if form.is_valid():
            form.save()
            return  redirect('home')
    context = {'form':form}
    return render(request, 'djapp/forms.html' , context)
def stEdit(request,st_id):
    st = Student.objects.get(id=st_id)
    form=StudentForm(instance=st) # form fields de e3mlha populate bel feilds bta3 student eli ana gbto b query men model
    if request.method == 'POST': #7sl submit
        form = StudentForm(request.POST,instance=st)
        if form.is_valid():
            form.save()
            return redirect('home') # home page de feha all data



    context = {'form': form}
    return render(request, 'djapp/forms.html', context)