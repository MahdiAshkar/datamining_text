import pandas as pd
from hazm import word_tokenize, Stemmer, Lemmatizer
import nltk

data = pd.read_csv('edit_tabnak_news.csv')
with open("stopwords.txt", encoding='utf-8') as stopwords_file:
    stopwords = stopwords_file.readlines()
stopwords = [stopword.replace('\n', '') for stopword in stopwords]

nltk.download('stopwords')
nltk_stopwords = nltk.corpus.stopwords.words('english')
stopwords.extend(nltk_stopwords)
len(stopwords)

stemmer = Stemmer()
lem = Lemmatizer()
dataset = pd.DataFrame(columns=('title_lead', 'category'))
for index, row in data.iterrows():
    title_lead = row['title']+' '+row['lead']
    title_lead_tokenized = word_tokenize(title_lead)
    title_lead_filtered = [
        w for w in title_lead_tokenized if not w in stopwords]
    title_lead_filtered_stemmed = [
        stemmer.stem(w) for w in title_lead_filtered]
    title_lead_filtered_lemmatized = [
        lem.lemmatize(w).replace('#', ' ') for w in title_lead_filtered_stemmed]
    dataset.loc[index] = {
        "title_lead": ' '.join(title_lead_filtered_stemmed)+' '+' '.join(title_lead_filtered_lemmatized),
        'category': row['category']
    }

dataset.to_csv('clean_tabnak_news.csv')
