from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def home(request) :
    return render(request, 'index.html')

def show(request) :
    
    if request.method == 'POST':
        
        text = request.POST.get('text_input')
    
        context_new = {
            'classification' : "FAKE",
            'sentiment' : 45,
            'bias' : 32,
            'clickbait' : 23,
            'related_1' : 'random text of length 5000 works wonder over the horizon of the morning dawn',
            'related_2' : 'this one is a small its to show the versatality of the project',
            'related_3' : 'the world doesnt revolve around the certain someone so you better stop the execution of the project',
            'related_4' : 'India is the civilization that is unbeatable and will prevail above everyone else',
            'related_5' : text,
        }

        return render(request, 'result.html', context=context_new)