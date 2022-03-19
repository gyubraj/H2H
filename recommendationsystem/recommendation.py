import pandas as pd
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import RegexpTokenizer
import re

from sklearn.metrics.pairwise import cosine_similarity
from django_pandas.io import read_frame

from property.models import Property



def initRecommend(recommendFor):

    query = Property.objects.all()

    df = read_frame(query, fieldnames=['id', 'name', 'address','type','city','nearest_landmark'])

    df['finalExtractedMeasureWord'] = consideredField(df)
    df['finalExtractedMeasureWord'] = df.finalExtractedMeasureWord.apply((nonAsciiRemove))

    df['finalExtractedMeasureWord'] = df.finalExtractedMeasureWord.apply(func = removeStopWords)

    df['finalExtractedMeasureWord'] = df.finalExtractedMeasureWord.apply(func = toLoweCase)

    df['finalExtractedMeasureWord'] = df.finalExtractedMeasureWord.apply(func=removePunctuations)
    df['finalExtractedMeasureWord'] = df.finalExtractedMeasureWord.apply(func=removeHtml)


    df.reset_index(level = 0, inplace = True) 
    indices = pd.Series(df.index, index = df['name'])

    print(indices)

    # here for H2H, recommendation will be done as accoridng to different fields (ie fields convert to vector(i use tfidf))
    tf = TfidfVectorizer(analyzer='word', ngram_range=(2, 2), min_df = 1, stop_words='english')
    tfidf_matrix = tf.fit_transform(df['finalExtractedMeasureWord'])

    simi = cosine_similarity(tfidf_matrix, tfidf_matrix)

    index = indices[recommendFor]

    extractedSim = list(enumerate(simi[index])) #pairwsie similarity scores 

    extractedSim = sorted(extractedSim, key=lambda x: x[1], reverse=True) #sorting result 

    extractedSim = extractedSim[1:4]  #recommended 3 places

    roomIndices = [i[0] for i in extractedSim]

    recommended = df[['id','name', 'type']].iloc[roomIndices]

    idList=[]
    for i in recommended['id']:
        idList.append(i)

    # connection.close
    return idList




def removeStopWords(text):
    text = text.split()
    stops = set(stopwords.words("english"))
    text = [w for w in text if not w in stops]
    text = " ".join(text)
    return text

def nonAsciiRemove(s):
    return "".join(i for i in s if  ord(i)<128)

def toLoweCase(text):
    return text.lower()

def removePunctuations(text):
    tokenizer = RegexpTokenizer(r'\w+')
    text = tokenizer.tokenize(text)
    text = " ".join(text)
    return text

def removeHtml(text):
    html_pattern = re.compile('<.*?>')
    return html_pattern.sub(r'', text)


def consideredField(df):
    data=[]
    for i in range(0, df.shape[0]):
        data.append(df['address'][i]+ ' '+ df['city'][i]+ ' ' + df['name'][i] + ' ' + df['nearest_landmark'][i] + ' ' + df['type'][i])
    return data