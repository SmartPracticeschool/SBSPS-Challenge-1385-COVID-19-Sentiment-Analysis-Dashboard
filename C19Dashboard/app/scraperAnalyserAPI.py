import json
from apscheduler.schedulers.background import BackgroundScheduler
import GetOldTweets3 as got
import datetime
import numpy as np
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import re
import emoji
import pytz
ist = pytz.timezone('Asia/Kolkata')

def data_pre_processing(data_frame_arg):
    """
    adds 'clean_text' column to data_frame_arg passed as argument,
    removes URLs,    coverts unicode Emoji to CLDR short name,
    replaces '&' with 'and', performs other text formatting.
    """

    data_frame_arg["clean_text"] = data_frame_arg["text"].to_numpy()

    def removeURLs(str):
        return re.sub(r'https?://\S+', ' ', str)

    data_frame_arg["clean_text"] = data_frame_arg["clean_text"].apply(lambda tweet: removeURLs(tweet))

    def proc(text):
        text = emoji.demojize(text, use_aliases=True, delimiters=('', '')).replace('_', ' ').replace('&', 'and') \
            .replace('.', '. ').replace(',', ', ').replace('#', '# ').replace('?', '? ').replace('!', '! ').replace('&',
                                                                                                                    'and')
        return re.sub(r'\s+', ' ', text)

    data_frame_arg["clean_text"] = data_frame_arg["clean_text"].apply(lambda tweet: proc(tweet))


def get_score_df(data_frame_arg):
    """
    Performs VADER Sentiment Analysis.
    adds 'pos', 'neg', 'neu', 'compound', 'result' colmns to data_frame_arg passed as argument.
    """
    sia = SentimentIntensityAnalyzer()
    scores_ = data_frame_arg["text"].apply(lambda tweet: sia.polarity_scores(tweet))
    scores_df_ret = pd.DataFrame(list(scores_))
    scores_df_ret['result'] = scores_df_ret['compound'].apply(
        lambda res: 'neutral' if res == 0 else ('positive' if res > 0 else 'negative'))
    for col in scores_df_ret:
        data_frame_arg[col] = scores_df_ret[col].to_numpy()


def scrape():
    """
    Fetches 500 tweets with predefined search query between yesterday and today.
    Returns Pandas DataFrame.
    """
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(
        '#lockdownindia OR #indialockdown OR #coronavirusindia OR #coronavirusinindia OR #coronaindia OR #covid19india OR #covid_19india OR #covid2019india OR #covidindia OR #indiafightscorona OR #indiafightscovid19 OR #indiafightscovid2019 OR #indiafightscovid OR #lockdown21 OR #indialockdown2 OR #indialockdown3 OR #indialockdown4 OR #indiaunlock OR #unlockindia OR #lockdownextensionindia OR #lockdowneffect') \
        .setSince((datetime.datetime.now(tz=ist) - datetime.timedelta(days=1)).strftime("%Y-%m-%d")) \
        .setUntil((datetime.datetime.now(tz=ist)).strftime("%Y-%m-%d")) \
        .setLang('en') \
        .setEmoji('unicode') \
        .setMaxTweets(500)

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
    return news_df


def update():
    """
    Updates JSON files after scraping, preprocessing, sentiment-analysis
    """
    with open('app/static/JSONS/ThreeWaySentiment.json') as f:
        data = json.load(f)
    if data['date'][-1] == (datetime.datetime.now(tz=ist)-datetime.timedelta(days=1)).strftime("%Y-%m-%d"):
        return

    print('Update process has started at: {}'.format(str(datetime.datetime.now(tz=ist))))
    tweet_df = scrape()
    if len(tweet_df.index) == 0:
        print('Scraping Failed at: {} '.format(str(datetime.datetime.now(tz=ist))))        
        return
    
    print('Succesfully scraped {} tweets for {} at: {}'.format(len(tweet_df.index), (datetime.datetime.now(tz=ist)-datetime.timedelta(days=1)).strftime("%Y-%m-%d"), str(datetime.datetime.now(tz=ist))))
    data_pre_processing(tweet_df)
    print('Succesfully preprocessed dataset at: {}'.format(str(datetime.datetime.now(tz=ist))))
    get_score_df(tweet_df)
    print('Succesfully performed sentiment analysis on dataset at: {}'.format(str(datetime.datetime.now(tz=ist))))
    # ThreeWaySentiment.json update
    with open('app/static/JSONS/ThreeWaySentiment.json') as f:
        data = json.load(f)
    dictResult = dict(tweet_df['result'].value_counts())
    data['date'].append((datetime.datetime.now(tz=ist) - datetime.timedelta(days=1)).strftime("%Y-%m-%d"))
    data['neg'].append(int(dictResult['negative']))
    data['neu'].append(int(dictResult['neutral']))
    data['pos'].append(int(dictResult['positive']))
    with open('app/static/JSONS/ThreeWaySentiment.json', 'w') as json_file:
        json.dump(data, json_file)
            
    print('Succesfully updated ThreeWaysentiment.json at: {}'.format(str(datetime.datetime.now(tz=ist))))

    # PieChart.json update
    with open('app/static/JSONS/PieChart.json') as f:
        data = json.load(f)
    dictResult = dict(tweet_df['result'].value_counts())
    data['values'][0] += int(dictResult['positive'])
    data['values'][1] += int(dictResult['negative'])
    data['values'][2] += int(dictResult['neutral'])
    with open('app/static/JSONS/PieChart.json', 'w') as json_file:
        json.dump(data, json_file)
            
    print('Succesfully updated PieChart.json at: {}'.format(str(datetime.datetime.now(tz=ist))))

    # SentimentScores.json update
    with open('app/static/JSONS/SentimentScores.json') as f:
        data = json.load(f)
    data['dates'].append(((datetime.datetime.now(tz=ist) - datetime.timedelta(days=1)).strftime("%B %d")))
    data['compound'].append(tweet_df['compound'].mean())
    data['pos'].append(tweet_df['pos'].mean())
    data['neg'].append(tweet_df['neg'].mean())
    with open('app/static/JSONS/SentimentScores.json', 'w') as json_file:
        json.dump(data, json_file)

    print('Succesfully updated SentimentScores.json at: {}'.format(str(datetime.datetime.now(tz=ist))))

    # HastagFrequencyGraph.json and TotalFrequency.json update
    with open('app/static/JSONS/TotalFrequency.json') as f:
        data = json.load(f)
    z = []
    for x in tweet_df[tweet_df['hashtags'].notna()]['hashtags']:
        if x == 'NaN':
            continue
        for y in x.replace(' ', '').split('#')[1:]:
            z.append(y)
    dict2 = dict(pd.Series(z).value_counts())

    for key in dict2:
        if data.get(key) == None:
            data.update({key:int(dict2[key])})
        else :
            data[key] += int(dict2[key])
    data = dict(sorted(data.items(), key = lambda x : x[1], reverse=True))

    with open('app/static/JSONS/TotalFrequency.json', 'w') as json_file:
        json.dump(data, json_file)

    with open('app/static/JSONS/HastagFrequencyGraph.json') as f:
        data2 = json.load(f)
    data2['xaxis'] = list(data.keys())[:10]
    data2['yaxis'] = list(data.values())[:10]
    with open('app/static/JSONS/HastagFrequencyGraph.json', 'w') as json_file:
        json.dump(data2, json_file)
    print('Succesfully updated TotalFrequency.json and HastagFrequencyGraph.json at: {}'.format(str(datetime.datetime.now(tz=ist))))