import requests

from Attack import base_attack
from Helpers import helper_generic_tags


class CSRF(base_attack.Attack):
    def __init__(self, url: str):
        super().__init__(url)

    def scan(self):
        flag_curr_pass = False
        flag_user_token = False
        desc_str_curr_pass = ""
        desc_str_user_token = ""

        cookies_dict = {
            "security": "impossible"
        }
        csrf_list = ['anticsrf', 'CSRFToken', '__RequestVerificationToken', 'csrfmiddlewaretoken', 'authenticity_token',
                'OWASP_CSRFTOKEN', "user_token", 'anoncsrf', 'csrf_token', '_csrf', '_csrfSecret', '__csrf_magic', 'CSRF', '_token',
                '_csrf_token', 'hidden']

        password_field_labels_list = ["Current Password", "Existing Password", "Current Account Password",
                                 "Old Password", "Previous Password", "Password Confirmation"]

        with requests.Session() as sess:
            sess.cookies.update(cookies_dict)

            url_to_scan_res = sess.get(self.url)
            print(url_to_scan_res.text)
            forms = helper_generic_tags.GetGenericTags.get_tags(url_to_scan_res.text, tag_type="form")

            for form in forms:
                print("_"*40)
                print(f"form.prettify(): {form.prettify()}")
                print("_"*40)
                print(f"type(form): {type(form)}")
                print("_" * 40)

                print(f"form.text.lower(): {form.text.lower()}")
                print(f"len(form.text.lower()): {len(form.text.lower())}")

                for item in password_field_labels_list:
                    print(f"item.lower(): {item.lower()}")
                    if item.lower() in form.text.lower():
                        flag_curr_pass = False
                        desc_str_curr_pass = f"exited at ({item.lower()} in {form.text.lower()}) {'website is not vulnerable to CSRF'.upper()}"
                    else:
                        flag_curr_pass = True
                        desc_str_curr_pass = f"{'website is vulnerable to CSRF 1'.upper()}"
                        return flag_curr_pass, desc_str_curr_pass

                input_tags = helper_generic_tags.GetGenericTags.get_tags(str(form), tag_type="input")

                print(f"input_tags: {input_tags}")
                print("_" * 40)
                print(f"len(input_tags): {len(input_tags)}")
                print("_" * 40)

                for input_tag in input_tags:
                    print(f"input_tag['name']: {input_tag['name']}")
                    print("_" * 40)

                    for csrf_input_name in csrf_list:
                        if input_tag['name'].lower() == csrf_input_name.lower():
                            flag_user_token = False
                            desc_str_user_token = f"exited at ({input_tag['name'].lower()} == {csrf_input_name.lower()}) {'website is not vulnerable to CSRF'.upper()}"
                        else:
                            flag_user_token = True
                            desc_str_user_token = f"{'website is vulnerable to CSRF 2'.upper()}"
                            return flag_user_token, desc_str_user_token

            return [(flag_curr_pass, desc_str_curr_pass), (flag_user_token, desc_str_user_token)]

    @staticmethod
    def check_str_in_form_child(input_tag, psw_label: list, csrf_list: list) -> bool:
        # if CSRF.check_str_in_form_child(input_tag, password_field_labels_list, csrf_list):
        ...




def main():
    # http://127.0.0.1/DVWA/vulnerabilities/csrf/
    csrf_obj = CSRF("http://127.0.0.1/DVWA/vulnerabilities/csrf/")

    print(f"csrf_obj.scan() returned -> {csrf_obj.scan()}")


if __name__ == '__main__':
    main()
