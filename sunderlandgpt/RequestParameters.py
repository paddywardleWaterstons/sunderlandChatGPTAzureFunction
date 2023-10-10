import azure.functions as func

class RequestParameters:

    def __init__(self, req: func.HttpRequest):
        
        self.forum_name = req.params.get('threadUrl', "https://www.readytogo.net/smb/threads/prediction-league-sunderland-afc-vs-watford.1617127/")
        self.chunk_size = req.params.get("chunkSize", 1)

    def get_forum_name(self):

        return self.forum_name
    
    def get_chunk_size(self):

        return self.chunk_size