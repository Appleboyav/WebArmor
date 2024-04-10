import requests

from Attack import base_attack
from Helpers import helper_generic_tags


class CSRF(base_attack.Attack):
    def __init__(self, url: str):
        super().__init__(url)

    def scan(self):
        cookies_dict: dict = {
            "security": "low"
            # "security": "medium"
            # "security": "high"
            # "security": "impossible"
        }

        csrf_variations_list: list = ['anticsrf', 'CSRFToken', '__RequestVerificationToken', 'csrfmiddlewaretoken', 'authenticity_token',
                'OWASP_CSRFTOKEN', "user_token", 'anoncsrf', 'csrf_token', '_csrf', '_csrfSecret', '__csrf_magic', 'CSRF', '_token',
                '_csrf_token', 'hidden']

        current_password_variations_list: list = ["Current Password", "Existing Password", "Current Account Password",
                                 "Old Password", "Previous Password", "Password Confirmation"]

        with requests.Session() as sess:
            sess.cookies.update(cookies_dict)

            url_to_scan_res = sess.get(self.url)
            # print(url_to_scan_res.text)

        forms = helper_generic_tags.GetGenericTags.get_tags(url_to_scan_res.text, tag_type="form")

        for form in forms:
            # print(form)

            # region Check if any kind of "current pass" is in the form text
            fl_curr_pass_in_form = CSRF.is_curr_pass_text_in_form(current_password_variations_list, str(form))
            # endregion

            # region Check if any kind of "csrf token" is in the input tags inside the form
            input_tags_in_form = helper_generic_tags.GetGenericTags.get_tags(str(form), tag_type="input")
            fl_csrf_token_in_form = CSRF.is_csrf_token_in_input_tags(input_tags_in_form, csrf_variations_list)
            # endregion

            attack_res = CSRF.check_attack_success(fl_curr_pass_in_form, fl_csrf_token_in_form)

            return attack_res

    @staticmethod
    def check_attack_success(fl_curr_pass_in_form: bool, fl_csrf_token_in_form: bool):

        if fl_curr_pass_in_form and fl_csrf_token_in_form:
            return False, "Website IS NOT vulnerable to CSRF attack!"
        # this elif wil never occur
        elif fl_curr_pass_in_form and not fl_csrf_token_in_form:
            return False, "Website IS NOT vulnerable to CSRF attack!"
        elif not fl_curr_pass_in_form and fl_csrf_token_in_form:
            return True, "Website IS vulnerable to CSRF attack!"
        elif not fl_curr_pass_in_form and not fl_csrf_token_in_form:
            return True, "Website IS vulnerable to CSRF attack!"


    @staticmethod
    def is_curr_pass_text_in_form(current_password_variations_list: list, form: str) -> bool:
        fl_curr_pass_in_form = False

        for curr_pass_text in current_password_variations_list:
            if curr_pass_text.lower() in form.lower():
                fl_curr_pass_in_form = True
                break

        return fl_curr_pass_in_form


    @staticmethod
    def is_csrf_token_in_input_tags(input_tags: list, csrf_variations: list) -> bool:
        fl_csrf_token_in_form = False

        for input_tag in input_tags:
            for csrf_text in csrf_variations:
                if csrf_text in str(input_tag):
                    fl_csrf_token_in_form = True
                    break

        return fl_csrf_token_in_form


# def main():
#     # http://127.0.0.1/DVWA/vulnerabilities/csrf/
#     csrf_obj = CSRF("http://127.0.0.1/DVWA/vulnerabilities/csrf/")
#
#     print(f"csrf_obj.scan() returned -> {csrf_obj.scan()}")
#
#
# if __name__ == '__main__':
#     main()
