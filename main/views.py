from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306275254',
        'name': 'Abby Shelley Tampubolon',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
