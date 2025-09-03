from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '246409542',
        'name': 'Rafasya Muhammad Subhan',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
# Create your views here.
