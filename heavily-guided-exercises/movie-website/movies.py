import webbrowser

class Video():
    """
    This class lets you construct Video objects containing the video's:
    title
    duration
    """

    def __init__(self, video_title, video_duration):
        self.title = video_title
        self.duration = video_duration

class Movie(Video):
    """
    This class lets you construct Movie objects containing the movie's:
    title
    trailer url
    poster url
    storyline summary
    duration
    """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, plot_summary, movie_trailer, poster_image, movie_duration):
        Video.__init__(self, movie_title, movie_duration)
        self.trailer_youtube_url = movie_trailer
        self.poster_image_url = poster_image
        self.storyline = plot_summary

    def show_trailer(self):
        webbrowser.open(self.trailer_url)
