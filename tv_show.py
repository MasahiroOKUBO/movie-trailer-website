import webbrowser
import video

class TvShow(video.Video):
    """This class provides a way to store tv show related information"""

    def __init__(self, title, duration, rating, storyline, main_image, trailer_youtube, season, episode, tv_station):
        print("Child Constructor Called")
        video.Video.__init__(self, title, duration, rating)
        self.storyline = storyline
        self.main_image = main_image
        self.trailer_youtube = trailer_youtube
        self.season = season
        self.episode = episode
        self.tv_station = tv_station

    def get_local_listing(self):
        print(episode)

    def show_info(self):
        print("Title is - " + self.title)
        print("Duration is - " + str(self.duration))
        print("Rating is - " + self.rating)
