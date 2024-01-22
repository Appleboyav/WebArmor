from bs4 import BeautifulSoup as bs


class GetGenericTags:
    @staticmethod
    def get_tags(html_page: str, tag_type: str, tag_attrs: dict) -> list(set()):
        """
        This function will return a list(set()) of specified the tag_type.
        
        Params: 
            - html_page: str
            - tag_type: str
            - tag_attrs: dict
        
        Return:
            - A list(set()) of the specified tag_type.
        """
        soup_obj = bs(html_page, 'html.parser')

        if tag_attrs:
            ls_tags = soup_obj.find_all(tag_type, tag_attrs)
        else: 
            ls_tags = soup_obj.find_all(tag_type)

        return list(set(ls_tags))
