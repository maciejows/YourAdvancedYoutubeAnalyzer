from YourAdvancedYoutubeAnalyzer.Backend.data import Data

class api:
    def __init__(self):
        self.data = ''
        self.url = ''

    def setter(self,url):
        self.url = url
        self.data = Data(url)

    def getter(self):
        return self.url