from Attack import base_attack

URL = "https://example.com/"


class TestAttack(base_attack.Attack):
    def __init__(self, url):
        super().__init__(url)

    def scan(self):
        print(f"Scanning from function: '{TestAttack.scan.__name__}'\nClass: {self.__class__.__name__}\nUrl:'{self.url}'\n")


# def main():
#     object_test_attack = TestAttack(URL)
#
#     object_test_attack.scan()
#
#
# if __name__ == "__main__":
#     main()
