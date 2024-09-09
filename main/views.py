from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name' : 'playstation',
        'price': '60000',
        'description': '4 hours'
    }

    return render(request, "main.html", context)