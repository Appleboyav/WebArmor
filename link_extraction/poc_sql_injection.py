import extract_links_with_validation_final
import pandas as pd

def main():
    links = extract_links_with_validation_final.get_internal_links()

    df = pd.DataFrame(links)
    print(df)

    # print("_"*25)
    # print(f"internal links are: {links}")
    
    '''
    TODO: create a list of functions that attack a certain url with sql injection attack.
    i wrote to Liza the level on how i think (avior) to create the attack. so if needed i'll send you this on whatsapp. 
    DONT DELETE ANYTHING WITHOUT ASKING EVERY FILE IS IMPORTANT!!!
    '''

if __name__ == '__main__':
    main()
