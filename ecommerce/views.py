from django.shortcuts import render



# Create your views here.
def index(request):
    '''products = Products.objects.all()'''
    return render(request, 'index.html', )
