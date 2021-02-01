from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from testapp.models import student
from . import forms
from django.contrib.auth.decorators import login_required
# Create your views here.
def amoo(request):
    st=forms.students()
    if request.method=='POST':
        st=forms.students(request.POST)
        if st.is_valid():
            st.save(commit=True)
            return a(request)
    return render(request,'a.html',{"student":st})

def amo(request):
    a=student.objects.all()
    return render(request,'a1.html',{'a':a})
def a(request):
    st=forms.students()
    return render(request,'a.html',{'student':st})
def d(request,id):
    print("umesh")
    st=student.objects.get(id=id)
    st.delete()
    return redirect('/a1')
