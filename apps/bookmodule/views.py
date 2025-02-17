from django.http import HttpResponse
from django.shortcuts import render  # ✅ Ensure this is imported

# Create your views here.

def index(request):
    return HttpResponse("Hello, world!")



def index(request):
    name = request.GET.get("name") or "world!"
    return HttpResponse("Hello, " + name)



def index2(request, val1=0):
    return HttpResponse("value1 = " + str(val1))



def index(request):
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html")

from django.http import HttpResponse

def index2(request, val1):
    if not isinstance(val1, int):  # ✅ Check if val1 is NOT an integer
        return HttpResponse("Error, expected val1 to be an integer", status=400)  # ✅ Return an error response

    return HttpResponse(f"value1 = {val1}")  # ✅ Display the value





def index(request):
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html" , {"name": name})



def viewbook(request, bookId):
    # Simulating a database with book details
    book1 = {'id': 123, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley'}
    book2 = {'id': 456, 'title': 'Secrets of Reverse Engineering', 'author': 'E. Eilam'}

    # Find the book by ID
    targetBook = None
    if book1['id'] == bookId:
        targetBook = book1
    if book2['id'] == bookId:
        targetBook = book2

    # Pass book data to the template
    context = {'book': targetBook}
    return render(request, 'bookmodule/show.html', context)  # ✅ Ensure this path is correct
