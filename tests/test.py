import unittest 
from speciallecture.ss2022 import Person

class Testing(unittest.TestCase):
    def test_setter(self):
        person = Person()
        val1 = person.set_name("Sihabul")
        self.assertEqual(val1, 0)
        val2 = person.set_name("Sihabul 2")
        self.assertEqual(val2, 1)
    # TODO(geguileo): Once we drom support dor MySQL 5.5 we can simplify this
    def test_getter(self):
        person = Person()
        person.set_name("Sihabul")
        person.set_name("Sihabul 2")
        self.assertEqual(person.get_name(0), "Sihabul")
        self.assertEqual(person.get_name(1), "Sihabul 2")
        


            