__author__ = 'Ellis'
__version__ = 'python 3.5'
__Project__ = 'Making a Movie Website: A python file generating a html web page'
# media.py is the classMedia() file, a blueprint for the review website.
# This code was tested by PEP8, a de facto standard of Python

import webbrowser as wb
'''provides interface to allow displaying Web-based documents to users'''


class Movie():
    """This class provides a way to store more related information"""

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]  # to define specified ratings

    """We will define a function for the class Movie that creates a new
    instance of the class. The __init__ function creates space
    for that instance. The instance will have the format:
    movie_title, movie_storyline, poster_image and trailer_youtube."""

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube


    """when we pass in a title, and assign its value to self.title,
    we are saying "this movie's title is the title we passed in" see result
    in the file entertainment.py"""

    """Each instance method, whether it be init or show_trailer takes the
    first argument as, self. So I will add that. All, show_trailer has
    to do, is open the web browser, with the correct URL. And the link
    or the URL, is stored in the instance variable, trailer_youtube_url.
    The way to access this instance variable, is through self."""

    def show_trailer(self):
        wb.open(self.trailer_youtube_url)
