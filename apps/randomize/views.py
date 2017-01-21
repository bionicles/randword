from django.shortcuts import render, redirect
import random, string

def randomword(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# Create your views here.
def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 1
    else:
        request.session['counter'] = request.session['counter'] + 1
    fred = {'counter':request.session['counter'], 'word':randomword(14)}
    return render(request, 'randomize/index.html', context=fred)

def generate(request):
    return redirect('/')
