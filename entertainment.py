__author__ = 'Ellis'
__version__ = 'python 3.5'
__Project__ = 'Making a Movie website:A python file generating a html web page'
# This code was tested by PEP8, a de-facto standard of Python
# entertainment.py file uses the content of media.py to define class movie

import media  # calls the contents of meda.py to define the class Movie.
import fresh_tomatoes  # takes in list of movies and output them in a website

"""So, here is my code for the class Movie, and behind it, is hidden the
other programming file (media.py), where we have defined multiple instances
(movie_title, movie_storyline, poster_image, and trailer_youtube)
of the class movie, namely love_and_basketball, christ_passion, and
why_did_i_get_married."""

love_and_basketball = media.Movie("Love and Basketball (2000)",
                                  "Monica (Sanaa Lathan) and Quincy "
                                  "(Omar Epps) "
                                  "are two childhood friends who both aspire"
                                  "to be professional basketball players."
                                  "Quincy, whose father, Zeke "
                                  "(Dennis Haysbert), plays for the "
                                  "Los Angeles Clippers, is a natural "
                                  "talent and a born leader. Monica is "
                                  "ferociously competitive but sometimes "
                                  "becomes overly emotional on the court. "
                                  "Over the years, the two begin to fall "
                                  "for each other, but their separate "
                                  "paths to basketball stardom threaten "
                                  "to pull them apart.",
                                  "https://upload.wikimedia.org/wikipedia/en/0/02/LBmoviePoster.jpg",  # noqa
                                  "https://www.youtube.com/watch?v=Ur83i6_BjbE")  # noqa

christ_passion = media.Movie("Passion of The Christ (2004)",
                             "In this version of Christ's crucifixion, based "
                             "on the New Testament, Judas expedites the "
                             "downfall of Jesus (Jim Caviezel) by handing "
                             "him over to the Roman Empire's handpicked "
                             "officials. To the horror of his mother, Mary "
                             "(Maia Morgenstern), "
                             "Magdalen (Monica Bellucci), whom he saved from "
                             "damnation, and his disciples, Jesus is "
                             "condemned to death. He is tortured as he drags "
                             "a crucifix to nearby Calvary, where he is "
                             "nailed to the cross. He dies, but not before "
                             "a last act of grace.",
                             "https://upload.wikimedia.org/wikipedia/en/6/61/Thepassionposterface-1-.jpg",  # noqa
                             "https://www.youtube.com/watch?v=4Aif1qEB_JU")

why_did_i_get_married = media.Movie("Why did i get Married? (2007)",
                                    "The difficulty of maintaining a solid "
                                    "relationship in modern times: Eight "
                                    "married friends take their annual "
                                    "reunion vacation in the Colorado "
                                    "mountains. Revelations of infidelity "
                                    "involving one pair shatter the amicable "
                                    "mood, forcing the remaining friends to "
                                    "take a hard look at the strength of "
                                    "their own marriages. The couples "
                                    "grapple with issues of commitment, "
                                    "love, betrayal and forgiveness as they "
                                    "try to move on with their lives.",
                                    "https://upload.wikimedia.org/wikipedia/en/2/23/Why_did_i_get_married_ver2.jpg",  # noqa
                                    "https://www.youtube.com/watch?v=xW1zSg6FLko")  # noqa

"""Here, i call the function 'open_movie_page', and place the list of movies
(love_and_basketball, christ_passion, and why_did_i_get_married) as inputs
to the function which translates it into a web page when we run the
entertainment.py, or fresh_tomatoes.py program."""

movies = [love_and_basketball, christ_passion, why_did_i_get_married]
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)  # calls the rating valid_rating in media.py
print(media.Movie.__doc__)  # calls the document contained in the class Media()
