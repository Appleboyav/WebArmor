from bs4 import BeautifulSoup

class GenericGetTags:
    @staticmethod
    def get_tags(html_page: str, tag_type: str, tag_attrs: dict) -> list(set()):
        """
        This function will return a set(list()) of specified the tag_type.
        
        Params: 
            - html_page: str
            - tag_type: str
            - tag_attrs: dict
        
        Returns:
            - A list(set()) of the specified tag_type.
        """
        soup_obj = BeautifulSoup(html_page, 'html.parser')

        if tag_attrs:
            ls_tags = soup_obj.find_all(tag_type, tag_attrs)
        else: 
            ls_tags = soup_obj.find_all(tag_type)

        return list(set(ls_tags))

