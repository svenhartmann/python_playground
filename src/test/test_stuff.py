"""
Test
"""
import unittest
from domain.model import Person, Developer


class TestSimplecalc(unittest.TestCase):
    """TestCase"""
    def test_create_person(self):
        """Create person from String"""
        person = Person.from_string('Hans;Wurst')
        self.assertEqual(person.say_hello(), 'Hi my name is Hans Wurst')


    def test_create_developer(self):
        """Create person from String"""
        developer = Developer('Hans', 'Wurst', 100000)
        self.assertEqual(developer.say_hello(),
                         'Hi my name is Hans Wurst and i earn 100000 € per year.')

        self.assertTrue(issubclass(Developer, Person))

        self.assertEqual(repr(developer), "Developer('Hans', 'Wurst', '100000')")
        self.assertEqual(str(developer), "Hans Wurst")

        developer.fullname = 'Hans Peter'
        self.assertEqual(developer.fullname, 'Hans Peter')
        self.assertNotEqual(str(developer), "Hans Wurst")
