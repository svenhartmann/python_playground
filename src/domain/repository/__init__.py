"""
Repositories
"""
from database import mongodb
from domain.model import Country

# pylint: disable=too-few-public-methods


class AbstractMongoRepository:
    """ Abstract Repository """
    model_cls = None
    table = ''

    def __init__(self, modelClass, table=''):
        self.table = table
        self.model_cls = modelClass

    def find_all(self):
        """ Find all """
        db_con = mongodb.Connection().get_instance()

        documents = []
        for document in db_con[self.table].find():
            model = self.model_cls(document)
            documents.append(model)

        return documents


class CountryRepository:
    """ Country Repository """
    abs_repo = None

    def __init__(self):
        self.abs_repo = AbstractMongoRepository(Country, "countries")

    def find_all(self):
        """ Find all Countries """
        return self.abs_repo.find_all()
