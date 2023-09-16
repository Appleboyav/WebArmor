import helper_link
import pandas as pd
import helper_lables

def main():
    # links = helper_link.get_internal_links()

    # # df = pd.DataFrame(links)
    # # print(df)

    # print("_"*25)
    # print(f"internal links are: {links}")
    # print("_"*25)
    
    # input_labels = helper_link.get_input_tags(links)
    # print(input_labels)

    # url = "https://www.hacksplaining.com/exercises/sql-injection#/fourth-login-attempt"
    # input_labels = helper_link.get_one_page_input_labels(url)
    # print("input_labels: ", input_labels)

    # TODO: change to login with user-agent

    url = 'https://www.instagram.com/accounts/login/'
    input_tags = helper_link.get_input_tags_from_url(url)

    if input_tags:
        print(len(input_tags))
        print(input_tags)
    else:
        print("no tags")

    '''
    TODO: create a list of functions that attack a certain url with sql injection attack.
    i wrote to Liza the level on how i think (avior) to create the attack. so if needed i'll send you this on whatsapp. 
    DONT DELETE ANYTHING WITHOUT ASKING EVERY FILE IS IMPORTANT!!!
    '''

if __name__ == '__main__':
    main()
