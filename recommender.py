import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# load data
ratings = pd.read_csv("data/u.data", sep="\t", names=["user_id","item_id","rating","timestamp"])
movies = pd.read_csv("data/u.item", sep="|", encoding="latin-1",
                     names=["item_id","title","release_date","video_release","imdb_url"] + [str(i) for i in range(19)])

data = pd.merge(ratings, movies, on="item_id")


# collaborative filtering
pivot = data.pivot_table(index='user_id', columns='title', values='rating').fillna(0)
similarity = cosine_similarity(pivot.T)

# recommendation function
def collaborative_recommend(movie_name):
    idx = list(pivot.columns).index(movie_name)
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:6]
    return [pivot.columns[i[0]] for i in scores]


# Content-Based Filtering
movies['tags'] = movies['title']

tfidf = TfidfVectorizer(stop_words='english')
vectors = tfidf.fit_transform(movies['tags'])

sim = cosine_similarity(vectors)

def content_recommend(movie_name):
    idx = movies[movies['title'] == movie_name].index[0]
    scores = list(enumerate(sim[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:6]
    return movies.iloc[[i[0] for i in scores]]['title'].tolist()