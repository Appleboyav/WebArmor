import json
from datetime import datetime


# Data to be written
dictionary = {
    "name": "sathiyajith",
    "rollno": 56,
    "cgpa": 8.6,
    "phonenumber": "9976770500",
    "list": [1, 2, 3, 4, 5]
}

dictionary_2 = {
    "name": "asdasdasdasd",
    "rollno": 44444,
    "cgpa": 8.64,
    "phonenumber": "9976770500",
    "list": [1, 2, 4, 5]
}

# Serializing json
# json_object = json.dumps(dictionary, indent=4)

# Writing to sample.json
# with open("sample.json", "a") as outfile:
#     outfile.write(json_object)
#
# json_object = json.dumps(dictionary_2, indent=4)
# with open("sample.json", "a") as outfile:
#     outfile.write(json_object)

test_dict = {"Date": f"{datetime.now().strftime('%d-%m-%Y')} ~ {datetime.now().strftime('%H:%M:%S')}"}
json_object = json.dumps(test_dict, indent=4)
with open("sample.json", "w") as outfile:
    outfile.write(json_object)
