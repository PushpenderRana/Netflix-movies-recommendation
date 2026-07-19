# 🎬 Netflix Movie Recommendation System

A Machine Learning-based Netflix Movie Recommendation System that recommends similar movies based on movie metadata such as genres, keywords, cast, crew, and overview.

The system uses **Content-Based Filtering** with **Cosine Similarity** to find movies similar to the user's selected movie.

---

## 🚀 Features

- 🎥 Recommend Top 5 Similar Movies
- 🖼️ Display Movie Posters
- 📖 Movie Overview with "Read More"
- ⭐ Movie Ratings
- 🎭 Genres, Cast & Director Information
- ⚡ Fast Recommendation using Cosine Similarity
- 🎨 Interactive Streamlit User Interface

---

## 📂 Project Structure

```
Netflix-Movie-Recommendation/
│
├── backend/
│   ├── data/
│   ├── models/
│   ├── services/
│   ├── routes/
│   ├── sentiment/
│   ├── utils/
│   └── app.py
│
├── frontend/
│   └── app.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🛠️ Tech Stack

### Frontend
- Streamlit

### Backend
- Flask

### Machine Learning
- Python
- Pandas
- NumPy
- Scikit-Learn

### Recommendation Algorithm
- Content-Based Filtering
- CountVectorizer
- Cosine Similarity

### Dataset
- TMDB 5000 Movies Dataset
- TMDB 5000 Credits Dataset

---

## 📊 Workflow

1. Load Movie Dataset
2. Data Cleaning
3. Feature Engineering
4. Combine Important Features
   - Genres
   - Keywords
   - Cast
   - Crew
   - Overview
5. Vectorization using CountVectorizer
6. Compute Cosine Similarity
7. Recommend Top Similar Movies
8. Display Movie Details in Streamlit

---

## 🧠 Machine Learning Pipeline

```
Movie Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
Tags Creation
      │
      ▼
CountVectorizer
      │
      ▼
Feature Vectors
      │
      ▼
Cosine Similarity Matrix
      │
      ▼
Movie Recommendation
```

---

## 📦 Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/Netflix-Movie-Recommendation.git
cd Netflix-Movie-Recommendation
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Backend

```bash
python backend/app.py
```

Backend will run at

```
http://127.0.0.1:5000
```

---

## ▶️ Run Frontend

```bash
streamlit run frontend/app.py
```

---

## 📸 Screenshots

### Home Page

_Add Screenshot Here_

### Recommendation Results

_Add Screenshot Here_

---

## 📁 Dataset

TMDB 5000 Movie Dataset

Contains:

- Movie Title
- Genres
- Overview
- Cast
- Crew
- Keywords
- Release Date
- Rating

---

## 🔍 Recommendation Logic

The recommendation system follows these steps:

- Convert movie metadata into text tags.
- Vectorize tags using **CountVectorizer**.
- Calculate **Cosine Similarity** between movies.
- Recommend the Top 5 most similar movies.

---

## 📈 Future Improvements

- Hybrid Recommendation System
- User Authentication
- Movie Search Autocomplete
- Watchlist Feature
- Personalized Recommendations
- Deep Learning-based Recommendations
- Deploy using Docker
- CI/CD Integration

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Add new feature"
```

4. Push branch

```bash
git push origin feature-name
```

5. Create a Pull Request

---

## 👨‍💻 Author

**Pushpender Rana**

- GitHub: https://github.com/PushpenderRana
- LinkedIn: https://www.linkedin.com/in/pushpenderrana/

---

## ⭐ Support

If you found this project useful, please give it a ⭐ on GitHub.

---
