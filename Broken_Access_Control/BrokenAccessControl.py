import requests

def fetch_main_js(url):
    response = requests.get(url + '/main.js')
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch main.js. Status code: {response.status_code}")

def find_admin_path(content, word, num_characters=10):
    path = []
    index = content.find(word)
    while index != -1:
        end_index = index + len(word) + num_characters
        path.append(content[index:end_index])
        index = content.find(word, end_index)
    return path[0][6:-1]

def get_into_administration_path(url):
    response = requests.get(url)
    print(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch main.js. Status code: {response.status_code}")


def main():

    website_url = "https://juice-shop.herokuapp.com"
    #get the contenet of main.js
    main_js_content = fetch_main_js(website_url)

    if main_js_content:
        # trying to find a admin page:
        word_to_find = 'path:"admin'
        administraionPath = website_url + '/#/' + find_admin_path(main_js_content, word_to_find)

        #find username and password of admin:





    else:
        print("Failed to fetch main.js.")

if __name__ == "__main__":
    main()