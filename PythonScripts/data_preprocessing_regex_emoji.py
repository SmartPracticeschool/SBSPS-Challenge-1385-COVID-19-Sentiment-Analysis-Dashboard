#!pip install emoji
import emoji
import re
import pandas as pd
from google.colab import drive
pd.set_option('display.max_columns', None)

drive.mount('drive')

df = pd.read_csv('drive/My Drive/colab_drive/ibm_hackathon_2020/final_lockdown_tweets/MarchFinal.csv')
df = df.append(pd.read_csv('drive/My Drive/colab_drive/ibm_hackathon_2020/final_lockdown_tweets/AprilFinal.csv'), ignore_index=True)
df = df.append(pd.read_csv('drive/My Drive/colab_drive/ibm_hackathon_2020/final_lockdown_tweets/MayFinal.csv'), ignore_index=True)
df.head()

df["clean_text"] = df["text"].to_numpy()
df.head()

#Removing URLs
def removeURLs(str):
    return re.sub(r'https?://\S+', ' ', str)

df["clean_text"] = df["clean_text"].apply(lambda tweet: removeURLs(tweet))
df.head()

# remove emoji followed by replacing unwanted characters and text-formatting
def proc(text):
    text = emoji.demojize(text, use_aliases=True, delimiters=('','')).replace('_', ' ').replace('&', 'and').replace('.', '. ').replace(',', ', ').replace('#', '# ').replace('?', '? ').replace('!', '! ').replace('&', 'and')
    return re.sub(r'\s+', ' ', text)

df["clean_text"] = df["clean_text"].apply(lambda tweet: proc(tweet))
df.head()

print(df['text'][3])
print(df["clean_text"][3])