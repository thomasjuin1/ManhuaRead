
class Manga:
    def __init__(self):
        self.title = None
        self.type = None
        self.status = None
        self.chapters = None
        self.note = None
        self.link = None
        self.image = None
        self.synopsis = None
        self.genres = None

    def __str__(self):
        value = ""
        for (key, val) in self.__dict__.items():
            if (val.__class__ == list):
                value = value + key + ": "
                for genre in val:
                    value = value + genre
                    if (genre != val[-1]):
                        value = value + ", "
                continue
            if (val):
                value = value + key + ": "+val+"\n"
        return value




