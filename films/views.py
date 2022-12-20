from django.shortcuts import render
from .models import Category, Films
from django.http import HttpResponseRedirect, HttpResponseNotFound
  
print(Films.objects.all())  

def index(request):
    films = Films.objects.all()
    return render(request, "index.html", {"films": films})
 

def add(request):
    add_categories() 
 

    if request.method == "POST":
        films = Films.objects.create(
            release_date = request.POST.get("release_date"),
            name = request.POST.get("name"),
            category_id = request.POST.get("category"),
            actors = request.POST.get("actors"),
            show_date = request.POST.get("show_date"),
            )
        
        films.save()
        return HttpResponseRedirect("/")
        

    categories = Category.objects.all()
    return render(request, "add.html", {"categories": categories})
    
 

def edit(request, pk):
    try:
        films = Films.objects.get(pk=pk)
 
        if request.method == "POST":
            films.name = request.POST.get("name")
            films.actors = request.POST.get("actors")
            films.category_id = request.POST.get("category")
            films.show_date = request.POST.get("show_date")
            films.release_date = request.POST.get("release_date")
            films.save()
            return HttpResponseRedirect("/")
        else:
            categories = Category.objects.all()
            return render(request, "edit.html", {"films": films, "categories": categories})
    except Films.DoesNotExist:
        return HttpResponseNotFound("<h2>Films not found</h2>")
     

def delete(request, pk):
    try:
        films = Films.objects.get(pk=pk)
        films.delete()
        return HttpResponseRedirect("/")
    except Films.DoesNotExist:
        return HttpResponseNotFound("<h2>Films not found</h2>")
 

def add_categories():
      
     if Category.objects.all().count() == 0:
          Category.objects.create(name = "Боевик")
          Category.objects.create(name = "Детектив")
          Category.objects.create(name = "Комедия")
          Category.objects.create(name = "Драма")
