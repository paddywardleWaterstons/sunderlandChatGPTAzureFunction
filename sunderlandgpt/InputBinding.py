import os
import azure.functions as func
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

class InputBinding:

    def __init__(self, containerName: str):
        
        self.containerName = containerName
        self.connectionString = os.environ["AzureWebJobsStorage"]
        
    def createBlobClient(self, endpoint):

        blobServiceClient = BlobServiceClient.from_connection_string(self.connectionString)

        blobClient = blobServiceClient.get_blob_client(container=self.containerName, blob=endpoint)

        return blobClient
    
    def downloadBlob(self, blobClient: BlobClient):

        data = blobClient.download_blob()

        return data

    def getContainerName(self):

        return self.containerName
    
    def getConnectionString(self):

        return self.connectionString


    

