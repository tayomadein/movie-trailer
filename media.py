"""This is a module for handling different media types"""

import webbrowser


class Movie():
    """This is a class for creating and storing detsils of my favourite movies"""

    # Constructor for the movie class - creates instances of class Movie
    def __init__(self, movie_title, movie_storyline, poster_image,
                 youtube_trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer

    def show_trailer(self):
        '''Funtion to show movie trailer when called'''
        webbrowser.open(self.trailer_youtube_url)
