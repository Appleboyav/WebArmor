import extract_links_with_validation_final
import pandas as pd
import helper

def main():
    # links = extract_links_with_validation_final.get_internal_links()

    # # df = pd.DataFrame(links)
    # # print(df)

    # print("_"*25)
    # print(f"internal links are: {links}")
    # print("_"*25)
    
    # input_labels = helper.get_input_tags(links)
    # print(input_labels)

    # url = "https://www.hacksplaining.com/exercises/sql-injection#/fourth-login-attempt"
    # input_labels = helper.get_one_page_input_labels(url)
    # print("input_labels: ", input_labels)

    url = 'https://www.instagram.com/accounts/login/'
    input_tags = helper.get_input_tags_from_url(url)

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
