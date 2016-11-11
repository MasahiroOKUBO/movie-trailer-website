class Video():
    """This class Define video type contents."""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, title, duration, rating):
        self.title = title
        self.duration = duration
        self.rating = rating

    def show_info():
        print("Title is - " + self.title)
        print("Duration is - " + self.duration)
        print("Rating is - " + self.rating)
