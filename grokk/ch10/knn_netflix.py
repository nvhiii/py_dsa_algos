# i am trying to understand this knn netflix rec engine algo

import numpy as np
from collections import Counter

# Sample data: Each user has rated shows from 1 to 5.
# Rows represent users, and columns represent shows
# 0 means the user hasn’t rated that show.
ratings = {
    'User1': [5, 3, 0, 1],
    'User2': [4, 0, 0, 1],
    'User3': [1, 1, 0, 5],
    'User4': [1, 0, 4, 4],
    'User5': [0, 1, 5, 4]
}

# Convert the ratings into a list of lists
user_ratings = list(ratings.values())
user_names = list(ratings.keys())

# Define a function to calculate Euclidean distance between two users
def euclidean_distance(user1, user2):
    distance = np.sqrt(sum((np.array(user1) - np.array(user2)) ** 2))
    return distance

# Function to find K-nearest neighbors
def find_neighbors(target_user_index, K):
    distances = []
    target_ratings = user_ratings[target_user_index]
    
    for i, ratings in enumerate(user_ratings):
        if i != target_user_index:  # Don’t calculate distance to self
            dist = euclidean_distance(target_ratings, ratings)
            distances.append((i, dist))
    
    # Sort by distance and take the K nearest
    distances.sort(key=lambda x: x[1])
    neighbors = [user_names[i[0]] for i in distances[:K]]
    return neighbors

# Recommend shows for a user based on their K-nearest neighbors
def recommend_shows(target_user_index, K):
    neighbors = find_neighbors(target_user_index, K)
    neighbor_indices = [user_names.index(neighbor) for neighbor in neighbors]
    
    # Get all shows the neighbors have rated highly
    show_recommendations = []
    for neighbor_index in neighbor_indices:
        neighbor_ratings = user_ratings[neighbor_index]
        for i, rating in enumerate(neighbor_ratings):
            if rating >= 4 and user_ratings[target_user_index][i] == 0:  # Recommend if high-rated and not watched
                show_recommendations.append(i)
    
    # Recommend the most frequently rated shows
    recommended_shows = [show for show, count in Counter(show_recommendations).most_common()]
    return recommended_shows

# Example usage:
target_user = 'User1'
target_user_index = user_names.index(target_user)
K = 2

recommendations = recommend_shows(target_user_index, K)
print(f"Recommendations for {target_user}: Show indices {recommendations}")
