# Create your views here.
# def moviehome(request):
#     searchTerm=request.GET.get("searchMovie")
#     return render(request, 'moviehome.html',{'searchTerm':searchTerm})
#     # return HttpResponse("<h1>hello<h1>")

# def moviehome(request) :
#     searchTerm = request.GET.get('searchMovie')
#     if searchTerm:
#         movies=Movie.objects.filter(title__contains=searchTerm)
#     else:
#         movies=Movie.objects.all()
#     return render(request, 'moviehome.html',
#                 {'searchTerm':searchTerm, 'movies':movies})