import os
import warnings
from typing import Dict

from openfabric_pysdk.utility import SchemaUtil

from ontology_dc8f06af066e4a7880a5938933236037.simple_text import SimpleText

from openfabric_pysdk.context import Ray, State
from openfabric_pysdk.loader import ConfigClass
import json
from transformer import pipeline


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

    # instantiate the fine tuned pipeline
    model = pipeline("question-answering", model="my_awesome_qa_model")

    #load the context
    with open('context_file', "r") as file:
        context = json.load(file)
    output = []

    # iterate over the text to generate the answer
    for text in request.text:
        answer = model(question = text, context = context)
        output.append(answer)
    return SchemaUtil.create(SimpleText(), dict(text=output))
