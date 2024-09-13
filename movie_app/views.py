from django.shortcuts import render,redirect

from .forms import *

# Create your views here.



def index_view(request):
    return render(request,'index.html')


def add_movie_view(request):
    form=MovieForm()
    if request.method == 'POST':
        form=MovieForm(request.POST)
        if form.is_valid:
            form.save(commit=True)
            return redirect('index/')
        else:
            return redirect('addmovie/')
    return render(request,'addmovie.html',{'form':form})


def list_view(request):
    Movies=Movie.objects.all().order_by('rating')
    return render(request,'listmovie.html',{'movies_list':Movies})