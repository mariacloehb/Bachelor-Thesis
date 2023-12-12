import pickle
import pandas as pd

# Load the data from the pickle file
with open("./retrieved_video_2022_key_fastfashion.pickle", "rb") as file:
    data = pickle.load(file)

# Convert 'Video Likes' to Numeric for sorting
data['Video Likes'] = pd.to_numeric(data['Video Likes'], errors='coerce')

# Sort the data by 'Video Likes' in descending order
sorted_data = data.sort_values(by='Video Likes', ascending=False)

# Save the sorted data back into the pickle file
sorted_data.to_pickle("./sorted_retrieved_video_2022_key_fastfashion.pickle")

# Display the top entries of the sorted data
print(sorted_data[['Video Title', 'Video Description', 'Video Likes']].head(10))
