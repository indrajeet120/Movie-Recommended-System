# 🎬 Movie Recommendation System

A content-based Movie Recommendation System built using **Python**, **Machine Learning**, and **Streamlit**. The application recommends movies similar to the one selected by the user and displays the movie poster, release year, and IMDb rating using the OMDb API.

## 🚀 Demo

You can deploy the application on Streamlit Community Cloud or run it locally.

## ✨ Features

* Recommend 5 similar movies based on the selected movie.
* Displays movie posters.
* Shows release year and IMDb rating.
* Interactive and user-friendly Streamlit interface.
* Uses a content-based recommendation algorithm with cosine similarity.

## 🛠️ Tech Stack

* Python
* Streamlit
* Pandas
* Scikit-learn
* Pickle
* Requests
* OMDb API

## 📂 Project Structure

```text
Movie-Recommended-System/
│
├── app.py
├── requirements.txt
├── README.md
├── artificats/
│   ├── movi_list.pkl
│   └── similarity.pkl
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
└── Recommender System.ipynb
```

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/indrajeet120/Movie-Recommended-System.git
cd Movie-Recommended-System
```

### Create a virtual environment

```bash
python -m venv env
```

Activate the environment:

**Windows**

```bash
env\Scripts\activate
```

**Linux/macOS**

```bash
source env/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app.py
```

or

```bash
python -m streamlit run app.py
```

## 📊 Dataset

The project uses the following datasets:

* TMDB 5000 Movies Dataset
* TMDB 5000 Credits Dataset

## 🤖 Recommendation Algorithm

1. Data preprocessing and cleaning.
2. Feature engineering using genres, keywords, cast, crew, and overview.
3. Text vectorization using CountVectorizer.
4. Cosine similarity computation.
5. Recommend the top 5 most similar movies.

## 🖼️ Movie Posters & Ratings

Movie posters, release year, and IMDb ratings are fetched dynamically using the **OMDb API**.

## 📦 Large Model File

The similarity matrix (`similarity.pkl`) is larger than GitHub's file size limit and is therefore downloaded automatically when the application starts (or hosted externally).

## 📸 Screenshots

Add screenshots of the application here.

Example:

```
screenshots/
├── home.png
├── recommendation.png
```

## 🔑 Environment Variables

Replace the OMDb API key in `app.py` with your own key.

```python
OMDB_API_KEY = "YOUR_API_KEY"
```

You can obtain a free API key from the OMDb website.

## 📈 Future Improvements

* User authentication
* Movie search with autocomplete
* Genre-based recommendations
* Hybrid recommendation system
* Deep learning-based recommendations
* Movie trailers
* Watchlist functionality

## 👨‍💻 Author

**Indrajeet Yadav**

* GitHub: https://github.com/indrajeet120


