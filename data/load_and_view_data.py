import pickle

with open("data/retrieved_video_2022_key_fastfashion.pickle", "rb") as file:
    data = pickle.load(file)

print(data)  # Or perform other analyses or visualizations as needed