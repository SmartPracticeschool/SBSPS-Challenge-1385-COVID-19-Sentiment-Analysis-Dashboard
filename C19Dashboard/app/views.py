from __future__ import unicode_literals
from django.views import View
from django.http import JsonResponse
from django.http import Http404
from django.shortcuts import render


class Home(View):
    def get(self, request):
        file = open('app/static/JSONS/SentimentScores.json')
        sScoresObj = file.read()
        file.close()
        file = open('app/static/JSONS/ThreeWaySentiment.json')
        sObj = file.read()
        file.close()
        file = open('app/static/JSONS/HastagFrequencyGraph.json')
        hash = file.read()
        file.close()
        file = open('app/static/JSONS/PieChart.json')
        pie = file.read()
        file.close()
        return render(request, 'main.html', {'sObj': sObj, 'hash': hash, 'pie': pie, 'CS': sScoresObj})


class SentimentGraph(View):
    def get(self, request):
        file = open('app/static/JSONS/IBMWatson.json')
        sgObj = file.read()
        file.close()
        file = open('app/static/JSONS/IbmWatsonBar.json', 'r')
        bObj = file.read()
        file.close()
        return render(request, 'SG.html', {'sgObj': sgObj, 'bObj': bObj})


class C19Updates(View):
    def get(self, request):
        return render(request, 'C19.html')


def health(request):
    state = {"status": "UP"}
    return JsonResponse(state)


def handler404(request):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)
