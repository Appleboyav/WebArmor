import requests
from typing import Dict

from Helpers import helper_generic_tags


class DVWA:
    @staticmethod
    def get_user_token(login_page_url) -> str:
        with requests.Session() as sess:
            res = sess.get(login_page_url)
            cookies = helper_generic_tags.GetGenericTags.get_tags(res.text, "input", {"type": "hidden"})
            user_token = cookies[0]["value"]

        return user_token

    @staticmethod
    def get_login_cookies(login_page_url: str, level: int = 0) -> Dict[str, str]:
        security_level = ["low", "medium", "high", "impossible"]

        login_cookies = {
            "PHPSESSID": DVWA.get_user_token(login_page_url),
            "security": security_level[level]
        }

        return login_cookies
