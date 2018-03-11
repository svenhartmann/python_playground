"""
Domain models
"""

# pylint: disable=too-few-public-methods


class Country:
    """ Country """

    def __init__(self, document):
        if document.get('_id') is not None:
            self.uid = document['_id']
        self.name = document['name']

class City:
    """ City """

    def __init__(self, document):
        if document.get('_id') is not None:
            self.uid = document['_id']
        self.name = document['name']
