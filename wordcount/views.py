from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html')

def count(request):
    text = request.GET['fulltext']
    listaPalavras = text.split()

    wordcounter = {}

    for word in listaPalavras:
        if word in wordcounter:
            wordcounter[word] += 1
        else:
            wordcounter[word] = 1


    sortedwords = sorted(wordcounter.items(), key=operator.itemgetter(0), reverse=True)

    print(wordcounter.items())


    return render(request, 'count.html', {'texto':text,'count':len(listaPalavras),
    'sortedwords':sortedwords})


def about(request):
    return render(request, 'about.html')
