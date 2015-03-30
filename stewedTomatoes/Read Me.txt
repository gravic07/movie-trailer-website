Stewed Tomatoes
Version 1.0



System requirements:
Python 2.79 (can be downloaded at https://www.python.org/downloads/)



How to use:
run favoriteMovies.py file and Stewed Tomatoes website opens (in new tab if possible)



How to Edit Movies:
To alter the movies that are populated, open the favoriteMovies.py file in a Python editor and use it to remove existing Movie() objects or add new ones.  See the notes in the favoriteMovies.py file for further instructions.



Stewed Tomatoes consists of three files:
	media.py
	stewedTomatoes.py
	favoriteMovies.py

media.py - creates the Movie() class which contains class variables: style, storyline, poster_image_url, trailer_youtube_url, releaseDate.

stewedTomatoes.py - contains the open_movies_page() function which when called creates a website containing the information passed in from Movie() object(s).

favoriteMovies.py - contains all of the Movie() objects to be displayed on the website and calls the open_movies_page() function from the stewedTomatoes.py file.



Created for Udacity Nanodegree. Original code for the stewedTomatoes.py file was given to my through the Udacity Nanodegree program and has been altered for this project.