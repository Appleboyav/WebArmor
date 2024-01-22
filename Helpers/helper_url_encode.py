import urllib.parse


def __add_plus_between_pairs(input_list, item_to_add="+") -> list:
    result_list = []
    for i in range(len(input_list) - 1):
        result_list.append(input_list[i])
        result_list.append(item_to_add)
    result_list.append(input_list[-1])
    return result_list


def __html_url_encode(my_list) -> str:
    encoded_str = ""

    for item in my_list:
        if item == "+":
            encoded_str += item
        if item != "+":
            encoded_str += urllib.parse.quote(item)

    return encoded_str


def run_encode(sqli_payload):
    ls_splitted = sqli_payload.split(" ")
    list_with_separators = __add_plus_between_pairs(ls_splitted)

    encoded_url = __html_url_encode(list_with_separators)
    return encoded_url
