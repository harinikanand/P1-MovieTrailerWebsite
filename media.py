import webbrowser #Import webbrowser module which is used to show the trailer of the movie

class Movie():
    """ This Class stores movie information namely title, storyline,
poster URL, Youtube trailer URL, actors, release date, rating"""

    
    # init function to instantiate an instance of Movie Class
    def __init__(self, movie_title, movie_storyline, movie_poster_image, movie_trailer_youtube_url, movie_actors, movie_release_date, movie_rating):

        # title, storyline, poster_image_url and trailer_youtube_url are instance variables of Class Movie
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_image
        self.trailer_youtube_url = movie_trailer_youtube_url
        self.actors = movie_actors
        self.release_date = "Release Date: " + movie_release_date
        self.rating = "Rating: "+ movie_rating

    # instance method of Class Movie that shows the trailer of the movie instance invoking this method
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
    
