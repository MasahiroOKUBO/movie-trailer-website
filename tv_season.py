import webbrowser
import video


class TvSeason(video.Video):
    """This class provides a way to store tv season information"""

    def __init__(self, title, duration, rating, storyline, main_image, trailer_youtube, season, episode, tv_station):
        video.Video.__init__(self, title, duration, rating)
        self.storyline = storyline
        self.main_image = main_image
        self.trailer_youtube = trailer_youtube
        self.season = season
        self.episode = episode
        self.tv_station = tv_station

    def show_poster_image(self):
        webbrowser.open(self.main_image)

    def show_trailer_youtube(self):
        webbrowser.open(self.trailer_youtube)

    def get_local_listing(self):
        print(episode)

    def show_info(self):
        print("Title is - " + self.title)
        print("Duration is - " + str(self.duration))
        print("Rating is - " + self.rating)
        print("Storyline is - " + self.storyline)
        print("TV station is - " + self.tv_station)
