import webbrowser


class Movie():
    """Contains all information of a favourite movie"""
    def __init__(self, title, storyline, image, trailer):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = image
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        """Opens the classes trailer property as a url in the users default browser"""
        webbrowser.open(self.trailer)
