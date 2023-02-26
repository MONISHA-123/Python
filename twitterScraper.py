
import streamlit as st
import datetime
import csv
import pandas as pd
import snscrape.modules.twitter as sntwitter

def uploadDatabase():
    pass
def downloadToCsv(df):
    return df.to_csv().encode('utf-8')


def downloadToJson():
    pass

def scrapetwitterData(title,tweet_count):
    scraper = sntwitter.TwitterSearchScraper(title)
    data = []
    i = 0
    for tweet in scraper.get_items():
        i = i + 1
        data.append({'ID': tweet.id, 'URL': tweet.url, 'Tweet Content': tweet.rawContent, 'Tweeted On': tweet.date,
                     'User': tweet.user, 'Reply Count': tweet.replyCount, 'Retweet Count': tweet.retweetCount,
                     'Language': tweet.lang, 'Source': tweet.sourceLabel, 'Like Count': tweet.likeCount})
        if (i > tweet_count):
            break
    df = pd.DataFrame(data)
    st.dataframe(df)
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button('Upload to Database'):
            uploadDatabase()

    with col2:
        csv = downloadToCsv(df)
        if st.download_button(
                label="Download data as CSV",
                data=csv,
                file_name='df.csv',
                mime='text/csv',
            ):
            pass

    with col3:
        if st.button('Download to JSON'):
            downloadToJson()

def stremlitCustom():
    st.title('My Streamlit App')
    st.write('Welcome to my app!')
    title = st.text_input('hashtag', '#python')
    print(title)
    d1 = st.date_input(
        "Start date",
        datetime.date(2019, 7, 6))
    d2 = st.date_input(
        "End date",
        datetime.date(2019, 7, 6))

    tweet_count = st.number_input('Tweet Count', 12)
    if st.button('Search'):
        scrapetwitterData(title,tweet_count)

stremlitCustom()


