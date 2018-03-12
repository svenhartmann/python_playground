"""
Domain models
"""

# pylint: disable=too-few-public-methods

class AbstractMongoModel:
    """ Yolo """


class Country(AbstractMongoModel):
    """ Country """

    def __init__(self, document):
        if document.get('_id') is not None:
            self.uid = document['_id']
        self.name = document['name']
        if document.get('capital') is not None:
            # oh boy..
            if isinstance(document.get('capital'), AbstractMongoModel):
                self.capital = document['capital'].__dict__
            else:
                self.capital = City(document['capital'])


class City(AbstractMongoModel):
    """ City """

    def __init__(self, document):
        if document.get('_id') is not None:
            self.uid = document['_id']
        self.name = document['name']
