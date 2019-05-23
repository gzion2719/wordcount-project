import operator

from django.http import HttpResponse
from django.shortcuts import render

def home ( request):
    return render (request, 'home.html' )

def count (request):
    fulltext=request.GET['fulltext']
    wordList=fulltext.split()
    wordCountDict={}

    for word in wordList:
        if word in wordCountDict:
            # increase
            wordCountDict[word] +=1
        else:
            #add to dictionary
            wordCountDict[word] = 1

    sortedWord = sorted(wordCountDict.items(), key= operator.itemgetter(1), reverse=True)


    return render(request, 'count.html', {'fulltext' : fulltext,
                                          'count':len(wordList),
                                          'sortedWords' : sortedWord})

def about (request):
    return render(request, 'about.html')
