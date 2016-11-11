class Video():
    """This class Define video type contents."""
    VALID_RATINGS = ["G","PG","PG-13","R"]

    def __init__(self, title, duration, rating):
        print("Parent Constructor Called")
        self.title = title
        self.duration = duration
        self.rating = rating
        # if rating in VALID_RATINGS :
        #     self.rating = rating
        # else:
        #     print("ERROR:invalid rating!")


    def show_info():
        print("Title is - " + self.title)
        print("Duration is - " + self.duration)
        print("Rating is - " + self.rating)
