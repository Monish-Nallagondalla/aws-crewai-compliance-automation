import os
import sys
import warnings
from datetime import datetime
from compliance_assistant.crew import ComplianceAssistant

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

topic = os.environ.get('TOPIC')
if topic is None:
    raise Exception("TOPIC is not defined. Please add the topic as an argument")


def run():
    """
    Run the compliance assistant
    """
    input = {
        "topic": topic,
        
    }