import requests
from Helpers import helper_generic_tags


def get_user_token(login_page_url) -> str:
    with requests.Session() as sess:
        res = sess.get(login_page_url)
        cookies = helper_generic_tags.GetGenericTags.get_tags(res.content, "input", {"type": "hidden"})
        user_token = cookies[0]["value"]

    return user_token
