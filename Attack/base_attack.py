

class Attack:
    def __init__(self, url):
        self.url = url

    def scan(self):
        print(f"Scanning from function: '{Attack.scan.__name__}'\nClass: {self.__class__.__name__}\nUrl:'{self.url}'\n")

        # pass

