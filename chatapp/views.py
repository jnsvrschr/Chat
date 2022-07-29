from django.shortcuts import render
from .models import Bericht
from django.shortcuts import redirect

# Create your views here.
def index(request):
    print(request.user)
    if request.user.is_authenticated:
        if request.method == 'POST':
            record = Bericht(inhoud=request.POST['tekst'], verzender=request.user)
            record.save()
        context = {
            'chatgeschiedenis': Bericht.objects.all().values()
        }
        return render(request, 'index.html', context)
    else:
        return redirect('accounts/login/')