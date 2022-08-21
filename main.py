import pandas
import random
import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import LabelEncoder

movies_data = pandas.read_csv("movies.csv")
user_ratings = pandas.read_csv("ratings.csv")

selected_user = int(input("user id:\n"))

user_ratings.drop("timestamp", axis=1, inplace=True)

# Columns
# user_ids = user_ratings.iloc[:, :-1].values
# movie_id = user_ratings.iloc[:, 1].values
# rating = user_ratings.iloc[:, 2].values

user_contents = []
for index, row in user_ratings.iterrows():
    if row["userId"] == selected_user:
        user_contents.append((row['movieId'], row['rating']))

movie_rating = []
for movie in user_contents:
    movie_rating.append(movie[1])

movie_ids = []
for movie in user_contents:
    movie_ids.append(movie[0])

random_picks = []
for i in range(0, 2):
    pick = random.choice(movie_ids)
    random_picks.append(pick)


counter = 0
movies_selected = []
for index, row in movies_data.iterrows():
    if row["movieId"] == movie_ids[counter]:
        movies_selected.append(row["genres"].split("|")[0])
        if counter < (len(movie_ids)-1):
            counter += 1
    else:
        pass


counter = 0
similar_users = []
for index, row in user_ratings.iterrows():
    if row["movieId"] == random_picks[counter]:
        similar_users.append(row["userId"])
        if counter < (len(random_picks)-1):
            counter += 1
    else:
        pass


def find_movies(selected_user):
    user_contents = []
    for index, row in user_ratings.iterrows():
        if row["userId"] == selected_user:
            user_contents.append((row['movieId'], row['rating']))

    movie_ids = []
    for movie in user_contents:
        movie_ids.append(movie[0])

    movie_ratings = []
    for movie in user_contents:
        movie_ratings.append(movie[1])

    return movie_ids[0:10]
    # return movie_ids[0:50]



bunch = []
for user in similar_users[0:10]:
    movie_list = find_movies(user)
    bunch.append(movie_list)




new_list = [[]]
for i in bunch:
    for item in i:
        new_list[0].append(item)
print(new_list)

similarity_metrics = []
counter = 5
starting_counter = 0
for i in new_list[0][0:100]:

    # print(new_list[0][starting_counter:counter])
    # print([movie_ids[starting_counter:counter]])

    if starting_counter != 100:
        # similarity_metrics.append(cosine_similarity([new_list[0][starting_counter:counter]], [movie_ids[starting_counter:counter]]))
        # if cosine_similarity([new_list[0][starting_counter:counter]], [movie_ids[starting_counter:counter]])[0][0] > 0.85:
        if cosine_similarity([new_list[0][starting_counter:counter]], [movie_ids[starting_counter:counter]])[0][0] > 0.85:
            print("Recomended Movies")
            # print(cosine_similarity([new_list[0][starting_counter:counter]], [movie_ids[starting_counter:counter]])[0][0])
            recomended_movies = []
            for index, row in movies_data.iterrows():
                if row["movieId"] in new_list[0][starting_counter:counter] or row["movieId"] in movie_ids[starting_counter:counter]:
                    recomended_movies.append(row["title"])
            print(recomended_movies)
            break
        else:
            starting_counter += 5
            counter = starting_counter + 5




# list_one = [(23.0, "389"), (12.0, "13358")]
# list_two = [(68.0, "2391"), (19.0, "834")]
# print(cosine_similarity(list_one, list_two))



# TODO #1 Pick out 3 random samples from movie ids and iterate over dataset until users found with same intrests
# TODO #2 Find the similarity between the factors for collaboratiave based filtering using cosine based similarity
# TODO #3 Use the K - nearest neighbors clustering algorithim and reverse cosine similarity

