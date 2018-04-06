import webbrowser

class Movie():

    valid_ratings = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, plot_summary, movie_trailer, poster_image):
      self.title = movie_title
      self.trailer_youtube_url = movie_trailer
      self.poster_image_url = poster_image
      self.storyline = plot_summary

    def show_trailer(self):
        webbrowser.open(self.trailer_url)
