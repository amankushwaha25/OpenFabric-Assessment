import os
import warnings
from typing import Dict

from openfabric_pysdk.utility import SchemaUtil

from ontology_dc8f06af066e4a7880a5938933236037.simple_text import SimpleText

from openfabric_pysdk.context import Ray, State
from openfabric_pysdk.loader import ConfigClass
import json
from transformers import pipeline

question_answerer = pipeline("question-answering", model="kushwahaaman/my_awesome_qa_model", token='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')


############################################################
# Callback function called on update config
############################################################
def config(configuration: Dict[str, ConfigClass], state: State):
    # TODO Add code here
    pass


############################################################
# Callback function called on each execution pass
############################################################
def execute(request: SimpleText, ray: Ray, state: State) -> SimpleText:
    #load the context
    with open('context_file.json', "r") as file:
        context = json.load(file)
    output = []
    
    for text in request.text:
        output.append(question_answerer(question=text, context=context)['answer'])

    return SchemaUtil.create(SimpleText(), dict(text=output))
