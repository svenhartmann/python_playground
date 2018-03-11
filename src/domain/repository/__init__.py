"""
Repositories
"""
from bson.objectid import ObjectId
from database import mongodb
from domain.model import Country, City

# pylint: disable=too-few-public-methods


class AbstractMongoRepository:
    """ Abstract Repository """
    model_cls = None
    table = ''

    def find_all(self):
        """ Find all """
        db_con = mongodb.Connection().get_instance()

        documents = []
        for document in db_con[self.table].find():
            model = self.model_cls(document)
            documents.append(model)

        return documents

    def find_one(self, _id):
        """ Find one domain model by id """
        db_con = mongodb.Connection().get_instance()
        return self.model_cls(db_con[self.table].find_one({'_id': ObjectId(_id)}))

    def save(self, document):
        """ Persist a domain model """
        db_con = mongodb.Connection().get_instance()
        return db_con[self.table].insert_one(document.__dict__).inserted_id


class CountryRepository(AbstractMongoRepository):
    model_cls = Country
    table = 'countries'


class CityRepository(AbstractMongoRepository):
    model_cls = City
    table = 'cities'