"""
Domain models
"""

# pylint: disable=too-few-public-methods

class AbstractMongoModel:
    """ Yolo """
    pass


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

    instances = 0

    def __init__(self, document):
        type(self).instances += 1

        if document.get('_id') is not None:
            self.uid = document['_id']
        self.name = document['name']

class Person:
    """ Person """
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    @classmethod
    def from_string(cls, name_str):
        """ Create new instance from string """
        firstname, lastname = name_str.split(';')
        return cls(firstname, lastname)

    def say_hello(self):
        """ be a good guy and say hello """
        return "Hi my name is {} {}".format(self.firstname, self.lastname)


class Developer(Person):
    """ Developer """
    def __init__(self, firstname, lastname, pay):
        super().__init__(firstname, lastname)
        self.pay = pay

    @property
    def fullname(self):
        """ Method as property """
        return '{} {}'.format(self.firstname, self.lastname)

    @fullname.setter
    def fullname(self, fullname):
        """ Setter """
        firstname, lastname = fullname.split(' ')
        self.firstname = firstname
        self.lastname = lastname

    def say_hello(self):
        hello_str = super().say_hello()
        return hello_str + ' and i earn {} € per year.'.format(self.pay)

    def __repr__(self):
        return "Developer('{}', '{}', '{}')".format(self.firstname, self.lastname, self.pay)

    def __str__(self):
        return self.fullname
