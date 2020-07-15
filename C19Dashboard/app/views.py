from __future__ import unicode_literals
from django.views import View
from django.http import JsonResponse
from django.http import Http404
from django.shortcuts import render
import json
import GetOldTweets3 as got
import pandas as pd
from .scraperAnalyserAPI import data_pre_processing
from .scraperAnalyserAPI import get_score_df


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
        file = open('app/static/JSONS/states_data.json')
        state_data = file.read()
        file.close()
        return render(request, 'main.html',
                      {'sObj': sObj, 'hash': hash, 'pie': pie, 'CS': sScoresObj, 'state_data': state_data})


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


def AutoUpdate(request, *args):
    data = open('app/static/JSONS/update.json')
    data = json.loads(data.read())
    return JsonResponse(data)


def UserInfo(request, username):
    tweetCriteria = got.manager.TweetCriteria().setUsername(username) \
        .setMaxTweets(100)
    tweet = got.manager.TweetManager.getTweets(tweetCriteria)
    text_tweets = [[tw.username,
                    tw.text,
                    tw.date,
                    tw.retweets,
                    tw.favorites,
                    tw.mentions,
                    tw.hashtags] for tw in tweet]
    news_df = pd.DataFrame(text_tweets,
                           columns=['user', 'text', 'date', 'favorites', 'retweets', 'mentions', 'hashtags'])
    if len(news_df.index) == 0:
        dict1 = {"positive": 0, "negative": 0, "neutral": 0}
    else:
        data_pre_processing(news_df)
        get_score_df(news_df)
        dictResult = dict(news_df['result'].value_counts())
        dict1 = {"positive": int(dictResult.get('positive')), "negative": int(dictResult.get('negative')),
             "neutral": int(dictResult.get('neutral'))}
    return JsonResponse(dict1)


def LastPage(request):
    return render(request, 'last.html')
