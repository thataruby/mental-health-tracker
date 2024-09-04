from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306173113',
        'name': 'Athazahra Nabila Ruby',
        'class': 'PBP KKI'
    }

    return render(request, "main.html", context)