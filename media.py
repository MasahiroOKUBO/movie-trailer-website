import webbrowser
import video

class Movie(video.Video):
    """This class provides a way to store movie and tv related information"""

    def __init__(self, title, duration, rating, storyline, poster_image, trailer_youtube):
        print("Child Constructor Called")
        video.Video.__init__(self, title, duration, rating)
        self.storyline = storyline
        self.poster_image = poster_image
        self.trailer_youtube = trailer_youtube

    def show_trailer_youtube(self):
        webbrowser.open(self.trailer_youtube)

    def show_poster_image(self):
        webbrowser.open(self.poster_image)

    def show_info(self):
        print("Title is - " + self.title)
        print("Duration is - " + str(self.duration))
        print("Rating is - " + self.rating)
        print("Storyline is - " + self.storyline)
