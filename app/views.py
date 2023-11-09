from django.shortcuts import render

# Create your views here.
def python(request):
  return render(request,'python.html')
def sql(request):
  return render(request,'sql.html')
def django(request):
  return render(request,'django.html')
def web(request):
  return render(request,'web.html')