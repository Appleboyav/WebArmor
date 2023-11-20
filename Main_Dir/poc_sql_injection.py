import helper_inte_links
import pandas as pd
import helper_labels

def main():
    # region comented code
    
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

    # endregion

    # region else
    """
    TODO: create a list of functions that attack a certain url with sql injection attack.
    i wrote to Liza the level on how i think (avior) to create the attack. so if needed i'll send you this on whatsapp. 
    ! DONT DELETE ANYTHING WITHOUT ASKING EVERY FILE IS IMPORTANT!!!
    """

    # ! TODO: change to login with user-agent
    # TODO: https://stackoverflow.com/questions/65392187/beautifulsoup-not-reading-the-same-source-html-code

    # ? ---------------------------------------------------------------

    # url = 'http://alf.nu/alert1?world=alert&level=alert0'
    # input_tags = helper_lables.function(url)
    
    # if input_tags:
    #     print(len(input_tags))
    #     print(input_tags)
    # else:
    #     print(input_tags)

    #endregion

    #region Main
    
    links = helper_inte_links.GetLink.get_internal_links()
    print(links)

    #endregion
    

if __name__ == '__main__':
    main()
