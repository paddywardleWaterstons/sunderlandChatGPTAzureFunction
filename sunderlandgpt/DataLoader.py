import json

class DataLoader:

    def __init__(self, path:str):
        
        self.data = self.loader(path)

    def loader(self, path:str):

        with open(path, "r") as loader:
            data = json.load(loader)

        return data
    
    def get_data(self):

        return self.data
