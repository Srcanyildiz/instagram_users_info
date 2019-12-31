##Import packages

import numpy as np
import pandas as pd 
import requests # First I need to fetch the link
from bs4 import BeautifulSoup

##let's work on Instagram

user_names = ["srcanyildiz","therock","leomessi","neymarjr","jlo"] 

insta_data=[]
for i in range(0,len(user_names)):
    url = 'https://www.instagram.com/' + user_names[i]
    dt1_tr = requests.get(url).text
    insta_data.append(dt1_tr)

name = []
surname = []
followers =[]
following = []
int_user = []

for i in range(0,len(insta_data)):
    soup_tr = BeautifulSoup(insta_data[i],'lxml')
    df_tr = soup_tr.find('meta', property ="og:description").get("content")
    ing = df_tr.partition(' ')[0]
    wer = df_tr.partition(' ')[2].partition(' ')[2].partition(' ')[0]
    soup_tr = soup_tr.html.head.title.get_text().rsplit("• ",1)[0]
    na = soup_tr.split(" ",1)[0].replace('\n','')
    su = soup_tr.partition('(')[0].split(" ",1)[1].replace(' ',"")
    int_u = soup_tr.rsplit(" ", 2)[-2].replace('(@','').replace(')','').replace('\n','').replace('@','')
    int_user.append(int_u)
    name.append(na)
    surname.append(su)
    followers.append(ing)
    following.append(wer)

##if you call below instagram dataframe you will get your users info
instagram = pd.DataFrame({'name': name,'surname': surname,'User':int_user,'followers': followers, 'following': following})
