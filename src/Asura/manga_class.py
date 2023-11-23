
class Manga:
    def __init__(self, infos):
        self.title = None
        self.type = None
        self.status = None
        self.chapters = None
        self.note = None

        i = 0

        if (infos[i] == "DROPPED"):
            self.status = "DROPPED"
            i = i + 1
        elif (infos[i] == "COMPLETED"):
            self.status = "COMPLETED"
            i = i + 1
        else:
            self.status = "ONGOING"

        if (i < len(infos) and infos[i]):
            self.type = infos[i]
            i = i + 1
        if (i < len(infos) and infos[i]):
            self.title = infos[i]
            i = i + 1
        if (i < len(infos) and infos[i]):
            self.chapters = infos[i].split(" ")[1]
            i = i + 1
        if (i < len(infos) and infos[i]):
            self.note = infos[i]

        for (key, val) in self.__dict__.items():
            if (val == None):
                self.__dict__[key] = "N/A"

    def __str__(self):
        value = ""
        for (key, val) in self.__dict__.items():
            if (val):
                value = value + key + ": "+val+"\n"
        return value




