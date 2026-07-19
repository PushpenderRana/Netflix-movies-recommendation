import pickle

movies = pickle.load(open("backend/models/movies.pkl", "rb"))

print(movies.columns.tolist())