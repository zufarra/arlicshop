from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name' : 'Zufar Romli Amri',
        'class': 'PBP D',
    }

    return render(request, "main.html", context)