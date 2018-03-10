"""
Domain models
"""


class Country: # pylint: disable=too-few-public-methods
    """ Country """

    def __init__(self, document):
        self.uid = document['_id']
        self.name = document['name']
