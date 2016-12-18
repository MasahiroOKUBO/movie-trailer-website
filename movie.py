import webbrowser
import video


class Movie(video.Video):
    """

    This module provides a way to store Movie information.

    """

    def __init__(self, title, duration, rating, storyline, main_image, trailer_youtube):
        video.Video.__init__(self, title, duration, rating)
        self.storyline = storyline
        self.poster_image = main_image
        self.trailer_youtube = trailer_youtube

    def show_poster_image(self):
        webbrowser.open(self.main_image)

    def show_trailer_youtube(self):
        webbrowser.open(self.trailer_youtube)

    def show_info(self):
        print("Title is - " + self.title)
        print("Duration is - " + str(self.duration))
        print("Rating is - " + self.rating)
        print("Storyline is - " + self.storyline)
