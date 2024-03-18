

class Attack:
    def __init__(self, url):
        self.url = url

    def scan(self):
        print(f"Scanning from function: '{Attack.scan.__name__}'\nclass: {self.__class__.__name__}\nurl:'{self.url}'\n")

        # pass

