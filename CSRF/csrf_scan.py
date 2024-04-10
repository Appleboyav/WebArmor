import requests

from Attack import base_attack
from Helpers import helper_generic_tags

#TODO: finish CSRF
"""
check why its not fully working
"""


class CSRF(base_attack.Attack):
    def __init__(self, url: str):
        super().__init__(url)

    def scan(self):
        # flag_curr_pass = False
        # flag_user_token = False
        # desc_str_curr_pass = ""
        # desc_str_user_token = ""
        fl_csrf_token_in_form = False
        fl_curr_pass_in_form = False


        cookies_dict: dict = {
            # "security": "low"
            # "security": "medium"
            # "security": "high"
            "security": "impossible"
        }

        csrf_list_variations_list: list = ['anticsrf', 'CSRFToken', '__RequestVerificationToken', 'csrfmiddlewaretoken', 'authenticity_token',
                'OWASP_CSRFTOKEN', "user_token", 'anoncsrf', 'csrf_token', '_csrf', '_csrfSecret', '__csrf_magic', 'CSRF', '_token',
                '_csrf_token', 'hidden']

        current_password_variations_list: list = ["Current Password", "Existing Password", "Current Account Password",
                                 "Old Password", "Previous Password", "Password Confirmation"]

        with requests.Session() as sess:
            sess.cookies.update(cookies_dict)

            url_to_scan_res = sess.get(self.url)
            print(url_to_scan_res.text)
            forms = helper_generic_tags.GetGenericTags.get_tags(url_to_scan_res.text, tag_type="form")

            for form in forms:
                print("_"*40)
                print(f"form.prettify():\n{form.prettify()}")
                print("_"*40)
                print(f"type(form): {type(form)}")
                print("_" * 40)

                print(f"form.text.lower(): {form.text.lower()}")
                print(f"len(form.text.lower()): {len(form.text.lower())}")

                # region Check if any kind of "current pass" is in the form text
                # TODO: clean code before pushing
                for curr_pass_text in current_password_variations_list:
                    print(f"[{curr_pass_text.lower()}]")  # TODO: remove after

                    if curr_pass_text.lower() in form.text.lower():
                        fl_curr_pass_in_form = True
                        break

                        # if fl_curr_pass_in_form:
                        #     return True, "inside form"

                    # fl_curr_pass_in_form = False

                # if not fl_curr_pass_in_form:
                #     return False, "not inside form"
                # endregion


                # region Check if any kind of "csrf token" is in the input tags inside the form
                input_tags_in_form = helper_generic_tags.GetGenericTags.get_tags(str(form), tag_type="input")
                # print("sep")
                # for item in input_tags_in_form:
                #     print(type(item))

                for input_tag in input_tags_in_form:
                    # print(type(str(input_tag)))
                    for csrf_text in csrf_list_variations_list:
                        # print(type(csrf_text))
                        if csrf_text in str(input_tag):
                            fl_csrf_token_in_form = True
                            break

                return f"\ncurr pass in form: {fl_curr_pass_in_form}\ncsrf in input tag: {fl_csrf_token_in_form}"
                # endregion

                # for item in password_field_labels_list:
                #     print(f"item.lower(): {item.lower()}")
                #     if item.lower() in form.text.lower():
                #         flag_curr_pass = False
                #         desc_str_curr_pass = f"exited at ({item.lower()} in {form.text.lower()}) {'website is not vulnerable to CSRF'.upper()}"
                #     else:
                #         flag_curr_pass = True
                #         desc_str_curr_pass = f"{'website is vulnerable to CSRF 1'.upper()}"
                #         return flag_curr_pass, desc_str_curr_pass

                # print("_" * 40)
                # input_tags = helper_generic_tags.GetGenericTags.get_tags(str(form), tag_type="input")
                #
                # print(f"input_tags: {input_tags}")
                # print("_" * 40)
                # print(f"len(input_tags): {len(input_tags)}")

                # print("_" * 40)
                #
                # # for input_tag in input_tags:
                # #     print(f"input_tag['name']: {input_tag['name']}")
                # #     print("_" * 40)
                # #
                # #     for csrf_input_name in csrf_list:
                # #         if input_tag['name'].lower() == csrf_input_name.lower():
                # #             flag_user_token = False
                # #             desc_str_user_token = f"exited at ({input_tag['name'].lower()} == {csrf_input_name.lower()}) {'website is not vulnerable to CSRF'.upper()}"
                # #         else:
                # #             flag_user_token = True
                # #             desc_str_user_token = f"{'website is vulnerable to CSRF 2'.upper()}"
                # #             return flag_user_token, desc_str_user_token
                #
                # for input_tag in input_tags:
                #     for item_csrf_list in csrf_list:
                #         if item_csrf_list in str(input_tag):
                #             return f"Website is NOT vulnerable to csrf:\n{input_tag}\n{item_csrf_list}"
                #
                # return f"Website IS vulnerable to csrf in the following form:\n{form.prettify()}"

            """
            if "some_current_password" in form:
                flag_curr_pass_in_form = True
                
            if "some_csrf_token" in input tag:
                flag_csrf_in_token = True
                
            return flag_csrf_in_token and flag_curr_pass_in_form??
            """

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
