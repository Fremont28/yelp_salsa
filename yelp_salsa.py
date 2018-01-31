#scraping la salsa (yelp)
#import libraries
import urllib.request as request
from bs4 import BeautifulSoup
import re
import nltk 
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
import gensim 
import requests
import string 

#beautiful soup for scraping 
url_yelp2="https://www.yelp.com/biz/la-salsa-los-angeles-9?start={}"
html_yelp2=request.urlopen(url_yelp2)
soup_yelp=BeautifulSoup(html_yelp2)
#get url
urls_yelpy=soup_yelp.find_all(href=re.compile("/biz/la-salsa-los-angeles-9"))
urls_yelpy
#grab info
soup_div=soup_yelp.find_all('div')
soup_div1=soup_yelp.find_all('div',class_=re.compile('media-story'))

#a. loop (gathers user infromation-reviews,friends,photos,location)
yelp_salsa=[]
for f in soup_div1:
    print(f.get_text()) 
    yelp_salsa.append(f.get_text())

#convert list to string
yelp_salsa_string="".join(str(x) for x in yelp_salsa)
yelp_salsa_string
#clean-up the string
yelp_salsa_clean=str.replace(yelp_salsa_string,"\n","")
yelp_salsa_clean

#b. loop (gathers text of the yelp review)
soup_div2=soup_yelp.findAll('div',attrs={"class":"review-content"})
salsa_text=[]
for f in soup_div2:
    print(f.find('p').text)
    salsa_text.append(f.get_text)

#convert list (of reviews) to a string 
yelp_review_string="".join(str(x) for x in salsa_text)
yelp_review_string 
#tokenize the yelp review text
yelp_review_list=tokenize.sent_tokenize(yelp_review_string)
#sentiment analyzer (Vader sentiment analysis)
sid=SentimentIntensityAnalyzer()
yelp_score=[] 
for x in yelp_review_list:
    print(x)
    ps=sid.polarity_scores(x)
    for k in sorted(ps):
        print('{0}: {1}, '.format(k, ps[k]), end='')
        yelp_score.append(ps) 

#compute the average comopund 'sentiment' score
cs=0
for i in range(len(yelp_score)):
    cs +=yelp_score[i]["compound"]
cs/len(yelp_score) #0.23 average compound score

