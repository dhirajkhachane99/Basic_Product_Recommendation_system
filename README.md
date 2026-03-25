# Product Recommendation System

A **Product Recommendation System** that suggests products/movies based on user input using **Collaborative Filtering** and **Content-Based Filtering**. Built with Python, pandas, scikit-learn, and Streamlit, this project is designed as a virtual internship submission.

##  Objective

Recommend relevant products to users based on:

- Their own choices (content similarity)  
- Other users’ behavior (collaborative filtering)


##  Tools & Libraries

- Python 3.x  
- pandas  
- scikit-learn  
- Streamlit  
- matplotlib (for data analysis)  

##  Project Structure :-
Product Recommendation System/
│
|---data/
│ ├--- u.data # User ratings
│ |--- u.item # Product/movie data
│
├---notebooks/
│ |--- analysis.ipynb # Data analysis and insights
│
|--- recommender.py # Recommendation logic
|--- app.py # Streamlit app
|--- requirements.txt
|--- report.txt # Project report
|--- README.md

##  Dataset
We use **MovieLens 100K dataset**:
- Ratings: `u.data` (user_id, item_id, rating)  
- Products/Movies: `u.item` (product/movie details)
**Dataset Link:** [MovieLens 100K](https://files.grouplens.org/datasets/movielens/ml-100k.zip)

##  Features
1. **Content-Based Filtering:**  
   Recommends products/movies similar to the input based on product attributes.

2. **Collaborative Filtering:**  
   Recommends products/movies based on what similar users liked.

3. **Search & Input:**  
   Users can search and select a product/movie for recommendations.

4. **Export Recommendations:**  
   Export recommended items to a CSV file.

5. **Data Analysis:**  
   Jupyter Notebook includes rating distribution, top products, and insights.

##  How to Run
1. Install dependencies:
```bash
pip install -r requirements.txt

##  Run the streamlit App
streamlit run app.py