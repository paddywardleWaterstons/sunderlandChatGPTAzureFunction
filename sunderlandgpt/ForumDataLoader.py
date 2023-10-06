import azure.functions as func
from .HTTPRequests import HTTPRequests

class ForumDataLoader:

    azureFunc = "https://getcommentsfuncs.azurewebsites.net/api/scrape?threadUrl="

    def __init__(self, forum:str):

        self.data = self.call_func(forum)

    def call_func(self, forum:str):

        return HTTPRequests().get(self.azureFunc + forum).json()
    
    def get_data(self):

        return self.data