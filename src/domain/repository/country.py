"""
Repositories
"""
from database import mongodb
from domain.model import Country

def find_all():
    """ Find all Country Models"""
    countries = []

    db_con = mongodb.Connection().get_instance()
    cursor = db_con.countries.find()

    for document in cursor:
        country = Country(document['name'])
        countries.append(country)

    return countries
