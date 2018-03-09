"""
MongoDB Connection
"""
import logging
from pymongo import MongoClient
from tornado.options import options


class Connection:
    """ Connection """
    _instance = None
    client = None

    @classmethod
    def get_instance(cls):
        """ Singleton  """
        if cls._instance is None:
            cls._instance = cls().connect(options.mongoDb)
        return cls._instance.client[options.mongoDbDatabase]

    def connect(self, connection_string=''):
        """ Create MongoClient Instance """
        logging.info("New MongoClient Instance")
        self.client = MongoClient(connection_string)
        return self.client[options.mongoDbDatabase]

    def close(self):
        """ Close MongoDB Connection """
        logging.info("Close MongoDB Connection")
        self.client.close()
