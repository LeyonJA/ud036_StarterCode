# Class that provides information about movies.

import webbrowser

class Movie():
    # Stores common information for a movie thumbnail.
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Plays the movie's trailer in web-browser.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
