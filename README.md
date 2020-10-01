<b>TITLE : Movie Trailer Website An Amazing Project <br>
AUTHOR : Ellis Enobun<br>
PYTHON VERSION : Python 3.5<br>
PROJECT : A python file generating a html web page<br>
CODE CHECKER: PEP8</b>

<b> Description:</b> A server-side code that stores a list of movies, including box art, imagery, a movie trailer URL, and serve this data as web page; allowing visitors to review their movies and watch trailers.

In this readme file, I explain in detail how our website; fresh_tomatoes.py functions with media.py and entertainment.py 
to display movie title, poster_image, and trailer. I later on explained how i reconfigured the fresh_tomatoes.py
file to include Moive_reviews, and a "About Udacity" link to Udacity website. Finally, i explained how to run this program.

# PLAN INFO

<b>Programming Foundations with Python</b>

We started off with a plan:

1. Go to the website
2. See all of the movies displayed
3. Click on one to play it's trailer

It's pretty simple in terms of concept, but how about implementation?

<b>Class structure</b>

We will need classes to build this movie website. We want our Movie class to be a template for a generic movie, and then create instances of that class like this:

love_and_basketball = Movie()

and add details to each specific movie. So, we first need to come up with a list of properties that we think every movie should have:

1. title
2. trailer
3. storyline
4. poster_image
5. reviews

# CODING EXPLAINED:

We will leave out some things like cast and box office numbers, since the things we listed above will be enough to get started. As far as methods we need to write, for now let's focus on:

    show_trailer()

<b>Defining our class</b>

We created a file called media.py. Inside of it, start our Movie class by typing:

    class Movie():

We Created a second file, called entertainment.py and connected it to the media.py file.

    import media

love_and_basketball = media.Movie()

What was happening behind the scenes was that a function named __init__ was being called. This function creates a new instance of the class by creating space in the computer's memory for that instance.

We need that function for our Movie class too! Note that another word for that __init__ function is the constructor, 
since it "constructs" an instance of our class. Before we begin, you may be wondering what the deal is with the two
underscores before and after the name "init". It's just a convention, actually: 
Python leads and follows names it doesn't want to conflict with user defined variables and functions 
with two underscores.

Let's define __init__. It will be defined like any other function in Python, with one small difference: we need to pass in the word self, which is a reference to the object being created (in one case, that could be toy_story), as the first parameter.

Note- Using self is simply convention; here's an excerpt from the Python docs explaining it:

Often, the first argument of a method is called self. 
This is nothing more than a convention: the name self has absolutely no special meaning to Python. 
Note, however, that by not following the convention your code may be less readable to other Python programmers, 
and it is also conceivable that a class browser program might be written that relies upon such a convention.

Here's our new class:

    class Movie():
        def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
            self.title = title
            self.storyline = storyline
            self.poster_image_url = poster_image_url
            self.trailer_youtube_url = trailer_youtube_url

A lot of this may look pretty odd, for example, this new self.thing syntax. 
What we are doing is passing in 4 pieces of information to the __init__ function, and 
then setting those to things called instance variables. So, when we pass in a title, and 
assign its value to self.title, we are saying "this movie's title is the title we passed in". 
This will make a lot more sense in a second.

Going back to our other file:

    import media
    
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

    print (love_and_basketball.title)

    >>> "Love and Basketball (2000)"

This applies to .storyline

What's going on behind the scenes?

When we run this code:

love_and_basketball = media.Movie() several things happen.

__init__ gets called
All references to self inside of __init__ point to love_and_basketball
The variables associated with the instance toy_story get assigned values:
love_and_basketball.title becomes "Love and Basketball"
love_and_basketball.storyline becomes "Monica (Sanaa Lathan) and Quincy (Omar Epps) are two childhood friends who..."
etc...

The same is used to create the other movies like christ_passion and why_did_i_get_married?

Now we know what is happening when we create an instance of Movie!

<b>Showing Trailers</b>

We defined our show_trailer method inside of the Movie class. 
Methods defined inside of a class are called instance methods.

    import webbrowser
    
    class Movie():
        def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
            self.title = title
            self.storyline = storyline
            self.poster_image_url = poster_image_url
            self.trailer_youtube_url = trailer_youtube_url
    
        def show_trailer(self):
            webbrowser.open(self.trailer_url)

Notice that we had to pass self in again; this is true of all instance methods. 
We modifed our other file a bit to see things working:

    import media
    
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

    love_and_basketball.show_trailer()

The web browser should open with the trailer playing!



# Creating the Movie Website

We used this file (called fresh_tomatoes.py) in our own entertainment code. 
Let's create a list of movies that we are going to use:

    import fresh_tomatoes
    
    movies = [love_and_basketball, christ_passion, why_did_i_get_married?]
    fresh_tomatoes.open_movies_page(movies)

# Note: 

The original fresh_tomatoes.py file was reconfigured by me, to display more content.

# Changes Made to the orginal fresh_tomatoes.py file:

1. The header_title was changed from its original heading to "Movie Review"
    
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="utf-8">
                    <title> Movie Review!</title>

2. Added "About Udacity" navigation as my reference to this project under the main_page_content. 
This links user to the main Udaity page.

              main_page_content = '''
                <body>
                ......
                  <!-- Main Page Content -->
                  <div class="container">
                    <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
                      <div class="container">
                        <div class="navbar-header">
                          <a class="navbar-brand" href="#"> Moive Trailer Project |</a>
                          <a class="navbar-brand" href="http://www.udacity.com"> About Udacity</a>

3. Added "movie storyline" to the code which enables the web page display the storyline of each movie.

          movie_tile_content = '''
          <div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
              <img src="{poster_image_url}" width="220" height="342">
              <h2>{movie_title}</h2>
          <div align="justify">
              {movie_storyline}
          </div>
          </div>
          

# HOW TO RUN THE PROGRAM!!!

1. Ensure that you have Python 2.7 or later installed.  

2. To turn this program into a movie website, ensure  that you download the fresh_tomatoes.py file. It is already
available for download here. However, make sure the files (movie.py, entertainment.py, and fresh_tomatoes.py) are present in the same folder.

3. Open these files using IDLE.

4. You can edit the file contents following the instructions here, or the ‘#’ and “”” comments given in the code.

5. Save your work (if any editing was done), and run the entertainment.py file. It will generate the HTML page or Website [fresh_tomatoes.html], using the fresh_tomatoes.py file.


 
