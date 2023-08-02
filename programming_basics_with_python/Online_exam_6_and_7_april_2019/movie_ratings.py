from sys import maxsize
chosen_movies = int(input())

max_rating, min_rating, counter, average_rating = -maxsize, maxsize, 0, 0
best_movie = ''
worst_movie = ''
total_rating = 0

for _ in range(chosen_movies):
    movie_name = input()
    movie_rating = float(input())

    counter += 1
    total_rating += movie_rating

    if movie_rating > max_rating:
        max_rating = movie_rating
        best_movie = movie_name
    elif movie_rating < min_rating:
        min_rating = movie_rating
        worst_movie = movie_name

    average_rating = total_rating / counter

print(f"{best_movie} is with highest rating: {max_rating:.1f}")
print(f"{worst_movie} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")
