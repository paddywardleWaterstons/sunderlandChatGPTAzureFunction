import openai
import time
import os

class OpenAICaller:

    def __init__(self):

        self.api_type = os.environ["API_TYPE"]
        self.api_base = os.environ["API_BASE"]
        self.api_version = os.environ["API_VERSION"]
        self.api_key = os.environ["OPEN_AI_KEY"]

    def openai_params(self):

        openai.api_type = self.api_type
        openai.api_base = self.api_base
        openai.api_version = self.api_version
        openai.api_key = self.api_key

    def chat(self, system_message, user_message):

        response = openai.ChatCompletion.create(
            engine="gpt-4",
            messages = [{"role":"system","content":system_message}, {"role":"user", "content": user_message}],
            temperature=0.7,
            max_tokens=800,
            top_p=0.95,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None)
        
        return response
    
    def chat_iterator(self, system_message:str, user_full:str):

        resp_full = []

        for i, user in enumerate(user_full):

            resp = self.chat(system_message, str(user))
            
            # index into json to get response and add to list
            resp_full.append(resp["choices"][0]["message"])
        
        return resp_full