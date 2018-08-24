from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):

    return render(request, 'home.html', {'hi': 'this is raj'})


def count(request):

    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    wcdict = {}
    for word in wordlist:
        lowword = word.lower()
        if lowword in wcdict:
            #increase
            wcdict[lowword] += 1
        else:
            #add to dict
            wcdict[lowword]=1
    return render(request, 'count.html', {'fulltext': fulltext, 'count':len(wordlist),'worddict': wcdict.items()})

def about(request):

    return render(request, 'about.html', {'hi': 'this is raj'})
