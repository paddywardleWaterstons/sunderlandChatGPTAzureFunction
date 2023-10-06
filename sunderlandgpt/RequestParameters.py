import azure.functions as func

class RequestParameters:

    def __init__(self, req: func.HttpRequest):
        
        self.forum_name = req.params.get('forum_url', "https://www.readytogo.net/smb/threads/prediction-league-sunderland-afc-vs-watford.1617127/")

    def get_forum_name(self):

        return self.forum_name