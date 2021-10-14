from django.http.response import HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

from suitsapi.models import Quotes

@csrf_exempt
def getAllQuotes(request):
    allquotes = Quotes.objects.all()
    quotesList = []
    for quote in allquotes:
        currentQuote = {'id':quote.id,
        'title':quote.title,
        'text':quote.text}
        quotesList.append(currentQuote)
    return JsonResponse({'result':quotesList})

@csrf_exempt
def getDelQuote(request,id):
    if request.method == 'GET':
        currentQuote = Quotes.objects.get(pk=id)
        quote = {'id':currentQuote.id,
        'title':currentQuote.title,
        'text':currentQuote.text}
        return JsonResponse(quote)
    elif(request.method == 'DELETE'):
        deleteQuote = Quotes.objects.get(pk=id).delete()
        return JsonResponse({'result':'Deleted Successfully'})
    else:
        return HttpResponseNotFound("Page Not Found!!")

@csrf_exempt
def addQuote(request):
    if request.method == 'POST':
        quote = json.loads(request.body.decode('utf-8'))
        addQuote = Quotes.objects.create(title=quote["title"], text=quote["text"])
        return JsonResponse({'result':'Added Successfully'})
    else:
        return HttpResponseNotFound("Page Not Found!!")


