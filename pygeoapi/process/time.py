import logging

from pygeoapi.process.base import BaseProcessor, ProcessorExecuteError
import datetime

LOGGER = logging.getLogger(__name__)

#: Process metadata and description
PROCESS_METADATA = {
    'version': '0.2.0',
    'id': 'time',
    'title': {
        'en': 'time'
    },
    'description': {
        'en': 'sends back current time'
        
    },
    'jobControlOptions': ['sync-execute', 'async-execute'],
    'keywords': ['example', 'time'],
    'links': [{
        'type': 'text/html',
        'rel': 'about',
        'title': 'information',
        'href': 'https://example.org/process',
        'hreflang': 'en-US'
    }],
    'inputs': {
        'name': {
            'title': 'Name',
            'description': 'The name of the person or entity that you wish to'
                           'be echoed back as an output',
            'schema': {
                'type': 'string'
            },
            'minOccurs': 0,
            'maxOccurs': 1,
            'metadata': None,  # TODO how to use?
            'keywords': ['full name', 'personal']
        }
    },
    'outputs': {
        'echo': {
            'title': 'time',
            'description': 'time',
            'schema': {
                'type': 'object',
                'contentMediaType': 'application/json'
            }
        }
    },
    'example': {
        'inputs': {
            'name': 'hans'
        }
    }
}




class TimeProcessor(BaseProcessor):
    """Time Processor example"""

    def __init__(self, processor_def):
        """
        Initialize object

        :param processor_def: provider definition

        :returns: pygeoapi.process.time.TimeProcessor
        """

        super().__init__(processor_def, PROCESS_METADATA)

    def execute(self, data):

        mimetype = 'application/json'
        name = data.get('name')

        if name is None:
            #raise ProcessorExecuteError('Cannot process without a name')
            name = 'Günther'


        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        value = f'Hello {name}! Currently it is {time}'.strip()

        outputs = {
            'id': 'echo',
            'value': value
        }

        return mimetype, outputs

    def __repr__(self):
        return f'<TimeProcessor> {self.name}'