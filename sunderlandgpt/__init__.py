import logging

import azure.functions as func

import json
import os

from .InputBinding import InputBinding
from .DataLoader import DataLoader
from .ForumDataLoader import ForumDataLoader
from .RequestParameters import RequestParameters
from .OpenAICaller import OpenAICaller

def main(req: func.HttpRequest) -> func.HttpResponse:

    reqParams = RequestParameters(req)
    trainingData = DataLoader("data/InputJson.json")
    forumData = ForumDataLoader(reqParams.get_forum_name())

    openaiModel = OpenAICaller()
    openaiModel.openai_params()
    system_message = f"Assistant is an AI chatbot that helps users turn a natural language list into JSON format. After users input a json with the football scores and goalscorers you output the label as shown in the examples below. Where the Sunderland players are: Anthony Patterson,Nathan Bishop,Daniel Ballard,Jenson Seelt,Luke O'Nien,Aji Alese,Nectarios Triantis,Dennis Cirkin,Timothée Pembélé,Trai Hume,Niall Huggins,Pierre Ekwah,Dan Neil,Jay Matete,Corry Evans,Chris Rigg,Ellis Taylor,Jobe Bellingham,Adil Aouchiche,Abdoullah Ba,Alex Pritchard,Bradley Dack,Jack Clarke,Jewison Bennette,Jack Diamond,Patrick Roberts,Nazariy Rusyn,Luís Semedo,Eliezer Mayenda,Mason Burstow \n Where input is the example inputs and label is the example outputs. {str(trainingData.get_data())}"

    chat_resp = openaiModel.chat_iterator(system_message, forumData.get_data()[:5])

    return func.HttpResponse(json.dumps(chat_resp), mimetype="application/json")