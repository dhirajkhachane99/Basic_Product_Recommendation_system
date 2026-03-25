import streamlit as st
from recommender import collaborative_recommend, content_recommend
import pandas as pd

st.set_page_config(page_title="Product Recommender", layout="wide")
st.title("Product Recommendation System")

# Load movies/products
movies = pd.read_csv("data/u.item", sep="|", encoding="latin-1",
                     names=["item_id","title","release_date","video_release","imdb_url"] + [str(i) for i in range(19)])

movie_list = movies['title'].tolist()

# Search box
selected_movie = st.selectbox("Select a product/movie:", movie_list)

# Choose recommendation type
method = st.radio("Recommendation Method:", ["Collaborative", "Content"])

# Recommendation button
if st.button("Get Recommendations"):
    if method == "Collaborative":
        recs = collaborative_recommend(selected_movie)
    else:
        recs = content_recommend(selected_movie)

    st.subheader("Recommended Products:")
    cols = st.columns(3)
    for i, r in enumerate(recs):
        with cols[i % 3]:
            st.write("👉", r)
            # Optional: Add placeholder image (if dataset has no image)
            st.image("https://via.placeholder.com/150", width=120)

# Export CSV
if st.button("Export Recommendations"):
    df = pd.DataFrame(recs, columns=["Recommendations"])
    df.to_csv("recommendations.csv", index=False)
    st.success("Recommendations exported as CSV")