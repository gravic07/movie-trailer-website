#!/usr/bin/python

import stewedTomatoes
import media

# Create Movie object in this pattern:
# movieTitle = media.Movie(
#     "Title of Movie",
#     "Description of the movie.",
#     "Movie poster img url",
#     "YouTube trailer URL",
#     "Release date")


# Create Toy Story Movie object
toyStory = media.Movie(
				"Toy Story",
				"A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.",
				"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
				"https://www.youtube.com/watch?v=KYz2wyBy3kc",
				"November 22, 1995")

# Create Avatar Movie object
avatar = media.Movie(
				"Avatar",
				"A Paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
				"http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
				"https://www.youtube.com/watch?v=_Tkc5pQp_JE",
				"December 18, 2009")

# Create Matrix Movie object
matrix = media.Movie(
				"The Matrix",
				"A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
				"http://ia.media-imdb.com/images/M/MV5BMTkxNDYxOTA4M15BMl5BanBnXkFtZTgwNTk0NzQxMTE@._V1_SX214_AL_.jpg",
				"https://www.youtube.com/watch?v=m8e-FF8MsqU",
				"March 31, 1999")

# Create Back to the Future Movie object
backToTheFuture = media.Movie(
				"Back to the Future",
				"A young man is accidentally sent 30 years into the past in a time-traveling DeLorean invented by his friend, Dr. Emmett Brown, and must make sure his high-school-age parents unite in order to save his own existence.",
				"http://ia.media-imdb.com/images/M/MV5BMjA5NTYzMDMyM15BMl5BanBnXkFtZTgwNjU3NDU2MTE@._V1_SX214_AL_.jpg",
				"https://www.youtube.com/watch?v=qvsgGtivCgs",
				"July 3, 1985")

# Create Batman Begins Movie object
batmanBegins = media.Movie(
				"Batman Begins", 
				"After training with his mentor, Batman begins his war on crime to free the crime-ridden Gotham City from corruption that the Scarecrow and the League of Shadows have cast upon it.",
				"http://ia.media-imdb.com/images/M/MV5BNTM3OTc0MzM2OV5BMl5BanBnXkFtZTYwNzUwMTI3._V1_SX214_AL_.jpg",
				"https://www.youtube.com/watch?v=vak9ZLfhGnQ",
				"June 15, 2005")

# Create Casino Movie object
casino = media.Movie(
				"Casino",
				"Greed, deception, money, power, and murder occur between two mobster best friends and a trophy wife over a gambling empire.",
				"http://ia.media-imdb.com/images/M/MV5BMTMzMjkwMTk4Nl5BMl5BanBnXkFtZTYwNjYxMjk5._V1_SX214_AL_.jpg",
				"https://www.youtube.com/watch?v=QiZvG_jcX0g",
				"November 22, 1995")

# Add the Movie objects you would like included on the website
# to the array below
movies = [toyStory, avatar, matrix, backToTheFuture, batmanBegins, casino]

# Creates and opens website with movies
stewedTomatoes.open_movies_page(movies)